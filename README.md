# Hajj & Umrah Sentiment Analysis — Backend (Flask + real ML model)

This is a **real** working backend: a scikit-learn model (TF-IDF + Multinomial
Naive Bayes, trained on `dataset.py`) served through a Flask REST API, backed
by a SQLite database (`hajj_umrah.db`, created automatically on first run).

It matches the design in the graduation project document (Chapter 1.6
Methodology: TF‑IDF feature extraction + Naive Bayes classification).

## 1. Open in VS Code
Open this `backend` folder in VS Code (`File → Open Folder…`).
Make sure the **Python extension** is installed.

## 2. Create a virtual environment
Open a terminal in VS Code (`` Ctrl+` ``) and run:

```bash
python -m venv venv
```

Activate it:
- Windows (PowerShell): `venv\Scripts\Activate.ps1`
- Windows (cmd): `venv\Scripts\activate.bat`
- macOS / Linux: `source venv/bin/activate`

VS Code may prompt "Select Interpreter" — choose the one inside `venv`.

## 3. Install dependencies
```bash
pip install -r requirements.txt
```

## 4. (Optional) Retrain the model
A model is trained automatically the first time you run `app.py` if
`model.pkl` doesn't exist yet. To retrain manually (e.g. after editing
`dataset.py`) and see accuracy/precision/recall:

```bash
python train_model.py
```

> The included dataset is intentionally small (~90 labeled examples) for
> demonstration. Accuracy will be limited — for a stronger model, replace
> `TRAIN_DATA` in `dataset.py` with a larger, real labeled dataset (hundreds/
> thousands of comments), which is exactly what your project proposes to
> collect in Graduation Project 2.

## 5. Run the API — and the full website
```bash
python app.py
```
The API starts at **http://localhost:5000** and auto-creates/seeds
`hajj_umrah.db` on first run.

**Open http://localhost:5000 in your browser** — this now serves a complete,
real, working website (login → dashboard → analyze comment → comments →
settings), built with React (via CDN, no npm/build step needed) and wired
directly to this Flask API and the trained ML model. Every comment you
analyze is saved for real in `hajj_umrah.db`.

**Default login** (auto-seeded on first run): `admin@hajj.sa` / `admin123`
You can also use "Sign up" on the login page to create a new account —
accounts are real rows in the `users` table, hashed with werkzeug's
`generate_password_hash` (not plaintext). "Forgot password" is simulated —
it confirms the flow but does not send a real email (no SMTP server is
configured; wire up Flask-Mail or similar for that).

## 6. Test it
```bash
curl http://localhost:5000/api/health

curl -X POST http://localhost:5000/api/analyze \
  -H "Content-Type: application/json" \
  -d "{\"text\": \"الازدحام كان شديد جداً وتأخير في كل شيء\"}"

curl http://localhost:5000/api/comments?per_page=5
curl http://localhost:5000/api/dashboard/stats
```
Or open `http://localhost:5000/api/health` directly in a browser, or use
Postman / VS Code's REST Client extension.

## 7. Connect the React frontend
In the React app (`HajjUmrahSystem.jsx`), replace the client-side
`analyzeText()` calls and the in-memory `comments` state with real `fetch`
calls to this API, e.g.:

```js
const res = await fetch("http://localhost:5000/api/analyze", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ text }),
});
const result = await res.json();
```

Do the same for `/api/comments` (GET/POST/PUT/DELETE) and
`/api/dashboard/stats`. This turns the current in-browser demo into a
frontend properly talking to a real backend + real ML model + real
database, as required by the project scope.

## Endpoints reference
| Method | Endpoint                 | Purpose                                |
|--------|---------------------------|-----------------------------------------|
| GET    | `/api/health`             | Check server + model status            |
| POST   | `/api/analyze`            | Analyze a comment (no DB write)        |
| GET    | `/api/comments`           | List/search/filter/sort/paginate       |
| POST   | `/api/comments`           | Add + analyze + store a new comment    |
| PUT    | `/api/comments/<id>`      | Edit a comment (re-analyzed)           |
| DELETE | `/api/comments/<id>`      | Delete a comment                       |
| GET    | `/api/comments/export`    | CSV export (`?format=csv`)             |
| GET    | `/api/dashboard/stats`    | Aggregated stats for charts            |

## Not included (needs further work for production)
- **Authentication (JWT) / roles** — currently the API is open; add
  `flask-jwt-extended` and per-route `@jwt_required()` checks.
- **Larger training dataset** — the model is a real, working classifier, but
  its accuracy is limited by the small illustrative dataset provided.
- **Deployment** — this runs Flask's development server; use `gunicorn` +
  a reverse proxy (nginx) for production.

## Open it from your phone (same Wi-Fi network)
The server listens on `0.0.0.0`, so other devices on the **same Wi-Fi** can
reach it too:

1. On the PC, find its local IP: open PowerShell and run `ipconfig`, look
   for **IPv4 Address** (e.g. `192.168.1.23`).
2. Make sure Windows Firewall allows inbound connections on port 5000 for
   Python (Windows may prompt you the first time you run the server — allow
   it for Private networks).
3. On the phone (connected to the same Wi-Fi), open:
   `http://192.168.1.23:5000` (use your PC's actual IP, not this example).

**Security note:** `debug=True` + `host="0.0.0.0"` exposes Werkzeug's
interactive debugger to everyone on your network — fine for a local
demo/graduation project on a trusted home/campus Wi-Fi, but set
`debug=False` (or don't bind `0.0.0.0`) before using this on any network
you don't fully trust.
