# -*- coding: utf-8 -*-
"""
Hajj & Umrah Sentiment Analysis System — Flask backend API.

Run in VS Code:
    1) python -m venv venv
    2) venv\\Scripts\\activate      (Windows)   or   source venv/bin/activate   (Mac/Linux)
    3) pip install -r requirements.txt
    4) python app.py
    -> API runs on http://localhost:5000

Endpoints:
    GET    /api/health
    POST   /api/analyze                body: {"text": "..."}
    GET    /api/comments               query: search, sentiment, category, sort, page, per_page
    POST   /api/comments               body: {"text": "...", "category": "..."}
    PUT    /api/comments/<id>          body: {"text": "..."}
    DELETE /api/comments/<id>
    GET    /api/comments/export        query: format=csv
    GET    /api/dashboard/stats
    POST   /api/auth/login             body: {"email": "...", "password": "..."}
    POST   /api/auth/signup            body: {"name": "...", "email": "...", "password": "..."}
    POST   /api/auth/forgot-password   body: {"email": "..."}  (simulated — no email is actually sent)
    GET    /api/users
    POST   /api/users                  body: {"name","email","role","password"}
    PUT    /api/users/<id>             body: {"name","email","role"}
    DELETE /api/users/<id>

Default seeded login: admin@hajj.sa / admin123
"""
import os
import io
import csv
import sqlite3
from datetime import datetime, timedelta, timezone

from flask import Flask, request, jsonify, g, Response, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
import joblib

from lexicon import find_keywords
from train_model import train_and_save, MODEL_PATH
from dataset import TRAIN_DATA

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "hajj_umrah.db")
CATEGORIES = ["Services", "Crowd Management", "Transportation", "Food",
              "Staff Behavior", "Accommodation", "General"]

app = Flask(__name__, static_folder="static", static_url_path="/static")


@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

# ---- CORS (manual, no extra dependency required) ----
@app.after_request
def add_cors_headers(resp):
    resp.headers["Access-Control-Allow-Origin"] = "*"
    resp.headers["Access-Control-Allow-Headers"] = "Content-Type"
    resp.headers["Access-Control-Allow-Methods"] = "GET,POST,PUT,DELETE,OPTIONS"
    return resp


@app.route("/api/<path:_any>", methods=["OPTIONS"])
def options_handler(_any):
    return "", 204


# ---------------------------------------------------------------- #
# Database helpers (plain sqlite3 — no ORM dependency needed)
# ---------------------------------------------------------------- #
def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(_exc):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            category TEXT NOT NULL,
            sentiment TEXT NOT NULL,
            confidence REAL NOT NULL,
            keywords TEXT,
            created_at TEXT NOT NULL
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            role TEXT NOT NULL DEFAULT 'viewer',
            created_at TEXT NOT NULL
        )
    """)
    user_count = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    if user_count == 0:
        conn.execute(
            "INSERT INTO users (name, email, password_hash, role, created_at) VALUES (?,?,?,?,?)",
            ("Admin User", "admin@hajj.sa", generate_password_hash("admin123"), "admin",
             datetime.now(timezone.utc).isoformat()),
        )
        conn.commit()
        print("Seeded default login -> email: admin@hajj.sa  password: admin123")

    count = conn.execute("SELECT COUNT(*) FROM comments").fetchone()[0]
    if count == 0:
        # Seed the database with the labeled training examples so the
        # dashboard/comments pages have real, non-empty data on first run.
        for i, (text, label) in enumerate(TRAIN_DATA):
            category = CATEGORIES[i % len(CATEGORIES)]
            pos_hits, neg_hits = find_keywords(text)
            keywords = ",".join(pos_hits + neg_hits)
            confidence = 78.0 + (i % 15)
            created_at = (datetime.now(timezone.utc) - timedelta(hours=i * 6)).isoformat()
            conn.execute(
                "INSERT INTO comments (text, category, sentiment, confidence, keywords, created_at) "
                "VALUES (?,?,?,?,?,?)",
                (text, category, label, confidence, keywords, created_at),
            )
        conn.commit()
    conn.close()


# ---------------------------------------------------------------- #
# ML model loading (trains automatically the first time it's needed)
# ---------------------------------------------------------------- #
def load_model():
    model_path = os.path.join(BASE_DIR, MODEL_PATH)
    if not os.path.exists(model_path):
        print("No trained model found — training a fresh one now...")
        return train_and_save()
    return joblib.load(model_path)


MODEL = load_model()


def run_sentiment_analysis(text: str):
    probs = MODEL.predict_proba([text])[0]
    classes = list(MODEL.classes_)
    scores = {cls: round(float(p) * 100, 1) for cls, p in zip(classes, probs)}
    label = classes[int(probs.argmax())]
    confidence = scores[label]
    pos_hits, neg_hits = find_keywords(text)
    return {
        "label": label,
        "confidence": confidence,
        "scores": scores,
        "positive_keywords": pos_hits,
        "negative_keywords": neg_hits,
        "keywords": pos_hits + neg_hits,
    }


# ---------------------------------------------------------------- #
# Routes
# ---------------------------------------------------------------- #
@app.route("/api/health")
def health():
    return jsonify({"status": "ok", "model_classes": list(MODEL.classes_)})


@app.route("/api/analyze", methods=["POST"])
def analyze():
    data = request.get_json(force=True, silent=True) or {}
    text = (data.get("text") or "").strip()
    if not text:
        return jsonify({"error": "text is required"}), 400
    result = run_sentiment_analysis(text)
    return jsonify(result)


@app.route("/api/comments", methods=["GET"])
def list_comments():
    db = get_db()
    search = request.args.get("search", "").strip()
    sentiment = request.args.get("sentiment", "all")
    category = request.args.get("category", "all")
    sort = request.args.get("sort", "date")
    page = max(1, int(request.args.get("page", 1)))
    per_page = max(1, int(request.args.get("per_page", 10)))

    query = "SELECT * FROM comments WHERE 1=1"
    params = []
    if search:
        query += " AND (text LIKE ? OR keywords LIKE ?)"
        params += [f"%{search}%", f"%{search}%"]
    if sentiment != "all":
        query += " AND sentiment = ?"
        params.append(sentiment)
    if category != "all":
        query += " AND category = ?"
        params.append(category)

    order = "created_at DESC" if sort == "date" else "confidence DESC"
    rows = db.execute(query + f" ORDER BY {order}", params).fetchall()
    total = len(rows)
    start = (page - 1) * per_page
    page_rows = rows[start:start + per_page]

    return jsonify({
        "total": total,
        "page": page,
        "per_page": per_page,
        "items": [dict(r) for r in page_rows],
    })


@app.route("/api/comments", methods=["POST"])
def add_comment():
    data = request.get_json(force=True, silent=True) or {}
    text = (data.get("text") or "").strip()
    category = data.get("category") or "General"
    if not text:
        return jsonify({"error": "text is required"}), 400

    result = run_sentiment_analysis(text)
    db = get_db()
    cur = db.execute(
        "INSERT INTO comments (text, category, sentiment, confidence, keywords, created_at) "
        "VALUES (?,?,?,?,?,?)",
        (text, category, result["label"], result["confidence"],
         ",".join(result["keywords"]), datetime.now(timezone.utc).isoformat()),
    )
    db.commit()
    new_row = db.execute("SELECT * FROM comments WHERE id=?", (cur.lastrowid,)).fetchone()
    return jsonify(dict(new_row)), 201


@app.route("/api/comments/<int:comment_id>", methods=["PUT"])
def update_comment(comment_id):
    data = request.get_json(force=True, silent=True) or {}
    text = (data.get("text") or "").strip()
    if not text:
        return jsonify({"error": "text is required"}), 400
    result = run_sentiment_analysis(text)
    db = get_db()
    db.execute(
        "UPDATE comments SET text=?, sentiment=?, confidence=?, keywords=? WHERE id=?",
        (text, result["label"], result["confidence"], ",".join(result["keywords"]), comment_id),
    )
    db.commit()
    row = db.execute("SELECT * FROM comments WHERE id=?", (comment_id,)).fetchone()
    if not row:
        return jsonify({"error": "not found"}), 404
    return jsonify(dict(row))


@app.route("/api/comments/<int:comment_id>", methods=["DELETE"])
def delete_comment(comment_id):
    db = get_db()
    db.execute("DELETE FROM comments WHERE id=?", (comment_id,))
    db.commit()
    return jsonify({"deleted": comment_id})


@app.route("/api/comments/export")
def export_comments():
    fmt = request.args.get("format", "csv")
    db = get_db()
    rows = db.execute("SELECT * FROM comments ORDER BY created_at DESC").fetchall()

    if fmt == "csv":
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["id", "text", "category", "sentiment", "confidence", "created_at"])
        for r in rows:
            writer.writerow([r["id"], r["text"], r["category"], r["sentiment"], r["confidence"], r["created_at"]])
        return Response(
            output.getvalue(), mimetype="text/csv",
            headers={"Content-Disposition": "attachment;filename=comments.csv"},
        )
    return jsonify([dict(r) for r in rows])


def user_public(row):
    d = dict(row)
    d.pop("password_hash", None)
    return d


# ---- Authentication (simple, session-less: returns the user object) ---- #
@app.route("/api/auth/login", methods=["POST"])
def login():
    data = request.get_json(force=True, silent=True) or {}
    email = (data.get("email") or "").strip().lower()
    password = data.get("password") or ""
    db = get_db()
    row = db.execute("SELECT * FROM users WHERE lower(email)=?", (email,)).fetchone()
    if not row or not check_password_hash(row["password_hash"], password):
        return jsonify({"error": "Invalid email or password"}), 401
    return jsonify(user_public(row))


@app.route("/api/auth/signup", methods=["POST"])
def signup():
    data = request.get_json(force=True, silent=True) or {}
    name = (data.get("name") or "").strip()
    email = (data.get("email") or "").strip().lower()
    password = data.get("password") or ""
    if not name or not email or len(password) < 6:
        return jsonify({"error": "name, email and a password of 6+ characters are required"}), 400
    db = get_db()
    exists = db.execute("SELECT id FROM users WHERE lower(email)=?", (email,)).fetchone()
    if exists:
        return jsonify({"error": "An account with this email already exists"}), 409
    cur = db.execute(
        "INSERT INTO users (name, email, password_hash, role, created_at) VALUES (?,?,?,?,?)",
        (name, email, generate_password_hash(password), "viewer", datetime.now(timezone.utc).isoformat()),
    )
    db.commit()
    row = db.execute("SELECT * FROM users WHERE id=?", (cur.lastrowid,)).fetchone()
    return jsonify(user_public(row)), 201


@app.route("/api/auth/forgot-password", methods=["POST"])
def forgot_password():
    # NOTE: no email server is configured, so this only confirms whether the
    # flow ran — it does not actually send an email. Wire up an SMTP/email
    # provider (e.g. Flask-Mail) here for real password-reset emails.
    data = request.get_json(force=True, silent=True) or {}
    email = (data.get("email") or "").strip().lower()
    db = get_db()
    row = db.execute("SELECT id FROM users WHERE lower(email)=?", (email,)).fetchone()
    return jsonify({
        "message": "If this email is registered, a reset link would be sent to it."
        if row else "If this email is registered, a reset link would be sent to it."
    })


# ---- Users management ---- #
@app.route("/api/users", methods=["GET"])
def list_users():
    db = get_db()
    rows = db.execute("SELECT * FROM users ORDER BY created_at ASC").fetchall()
    return jsonify([user_public(r) for r in rows])


@app.route("/api/users", methods=["POST"])
def add_user():
    data = request.get_json(force=True, silent=True) or {}
    name = (data.get("name") or "").strip()
    email = (data.get("email") or "").strip().lower()
    role = data.get("role") or "viewer"
    password = data.get("password") or "changeme123"
    if not name or not email:
        return jsonify({"error": "name and email are required"}), 400
    db = get_db()
    if db.execute("SELECT id FROM users WHERE lower(email)=?", (email,)).fetchone():
        return jsonify({"error": "An account with this email already exists"}), 409
    cur = db.execute(
        "INSERT INTO users (name, email, password_hash, role, created_at) VALUES (?,?,?,?,?)",
        (name, email, generate_password_hash(password), role, datetime.now(timezone.utc).isoformat()),
    )
    db.commit()
    row = db.execute("SELECT * FROM users WHERE id=?", (cur.lastrowid,)).fetchone()
    return jsonify(user_public(row)), 201


@app.route("/api/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json(force=True, silent=True) or {}
    db = get_db()
    row = db.execute("SELECT * FROM users WHERE id=?", (user_id,)).fetchone()
    if not row:
        return jsonify({"error": "not found"}), 404
    name = data.get("name", row["name"])
    email = (data.get("email") or row["email"]).strip().lower()
    role = data.get("role", row["role"])
    db.execute("UPDATE users SET name=?, email=?, role=? WHERE id=?", (name, email, role, user_id))
    db.commit()
    row = db.execute("SELECT * FROM users WHERE id=?", (user_id,)).fetchone()
    return jsonify(user_public(row))


@app.route("/api/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    db = get_db()
    db.execute("DELETE FROM users WHERE id=?", (user_id,))
    db.commit()
    return jsonify({"deleted": user_id})


@app.route("/api/dashboard/stats")
def dashboard_stats():
    db = get_db()
    rows = db.execute("SELECT * FROM comments").fetchall()
    total = len(rows)
    pos = sum(1 for r in rows if r["sentiment"] == "positive")
    neg = sum(1 for r in rows if r["sentiment"] == "negative")
    neu = total - pos - neg

    by_category = {}
    for r in rows:
        c = by_category.setdefault(r["category"], {"total": 0, "positive": 0, "negative": 0, "neutral": 0})
        c["total"] += 1
        c[r["sentiment"]] = c.get(r["sentiment"], 0) + 1

    keyword_freq = {}
    for r in rows:
        if r["keywords"]:
            for kw in r["keywords"].split(","):
                kw = kw.strip()
                if kw:
                    keyword_freq[kw] = keyword_freq.get(kw, 0) + 1
    top_keywords = sorted(keyword_freq.items(), key=lambda x: x[1], reverse=True)[:12]

    return jsonify({
        "total": total, "positive": pos, "negative": neg, "neutral": neu,
        "positive_pct": round(pos / total * 100, 1) if total else 0,
        "negative_pct": round(neg / total * 100, 1) if total else 0,
        "neutral_pct": round(neu / total * 100, 1) if total else 0,
        "by_category": by_category,
        "top_keywords": top_keywords,
    })


MODEL = load_model()
init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
