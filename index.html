<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Hajj &amp; Umrah Sentiment Analysis System</title>
<script src="https://cdn.tailwindcss.com"></script>
<script src="https://cdn.jsdelivr.net/npm/react@18/umd/react.production.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/react-dom@18/umd/react-dom.production.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@babel/standalone@7/babel.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4"></script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  body{margin:0;}
  ::-webkit-scrollbar{width:8px;height:8px;}
  ::-webkit-scrollbar-thumb{background:#94a3b8;border-radius:8px;}
</style>
<script>
  // Show a clear message instead of a silent blank page if a CDN file
  // fails to load (blocked network, offline, ad-blocker, etc.)
  function showFatalOverlay(msg) {
    var root = document.getElementById('root');
    if (!root) return;
    root.innerHTML = '<div style="padding:40px;font-family:sans-serif;max-width:700px;margin:0 auto">' +
      '<h2 style="color:#b91c1c">Something went wrong</h2>' +
      '<pre style="white-space:pre-wrap;font-family:monospace;background:#fef2f2;border:1px solid #fecaca;border-radius:8px;padding:12px;color:#b91c1c">' + msg + '</pre>' +
      '<button onclick="location.reload()" style="margin-top:12px;background:#0f766e;color:#fff;border:0;padding:10px 16px;border-radius:8px;cursor:pointer">Reload page</button></div>';
  }
  window.addEventListener('error', function (e) {
    var isResource = e.target && e.target.tagName === 'SCRIPT';
    if (isResource) {
      showFatalOverlay('Failed to load: ' + (e.target.src || 'a required file') +
        '\n\nThis page needs internet access to load React/Chart.js from a CDN. ' +
        'Check your internet connection, disable any ad-blocker/VPN restriction for this page, then refresh (Ctrl+F5).');
    } else {
      var msg = 'JavaScript error: ' + e.message + '\n' + (e.error && e.error.stack || '');
      console.error(msg);
      // If the error happened before React ever mounted (e.g. a syntax/parse error
      // in the Babel-transpiled script), the root is still empty — show it there
      // instead of leaving a silent white page. Once mounted, React's own
      // ErrorBoundary (below) handles rendering errors, so we only overlay here
      // for pre-mount failures.
      if (window.__appMounted !== true) { showFatalOverlay(msg); }
    }
  }, true);
  window.addEventListener('unhandledrejection', function (e) {
    var msg = 'Unhandled promise rejection: ' + (e.reason && (e.reason.stack || e.reason.message || e.reason));
    console.error(msg);
    if (window.__appMounted !== true) { showFatalOverlay(msg); }
  });
</script>
</head>
<body>
<div id="root"><div style="padding:40px;font-family:sans-serif;color:#666">Loading…</div></div>

<script type="text/babel" data-presets="react">
console.log("HajjUmrahSystem build: v3-errorboundary");
const { useState, useEffect, useMemo, useRef } = React;

/* ============== API BASE ============== */
const API = window.location.origin + "/api";

// Every API call goes through this wrapper: if the server doesn't respond
// within 8 seconds, the request is aborted and rejected instead of hanging
// the UI forever. Pages catch this and fall back to an empty/error state.
function apiFetch(url, options) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), 8000);
  return fetch(url, Object.assign({}, options, { signal: controller.signal }))
    .finally(() => clearTimeout(timer));
}

// Helper for reads that should show a loading/error state (Reports, Users list).
// Unlike apiFetch on its own, this rejects on a non-OK response so a 404/500 HTML
// error page from Flask doesn't silently break r.json() and leave the page stuck
// on a blank/empty screen forever. (Login/signup/add-user intentionally keep using
// apiFetch directly, since they need to read the JSON body even on error responses.)
function apiFetchJson(url) {
  return apiFetch(url).then((res) => {
    if (!res.ok) {
      const err = new Error("Request failed: " + res.status + " " + res.url);
      err.status = res.status;
      throw err;
    }
    return res.json();
  });
}

/* ============== ICONS (tiny inline SVG set, no external deps) ============== */
const ICONS = {
  dashboard: "M3 3h8v8H3V3Zm10 0h8v5h-8V3ZM3 13h8v8H3v-8Zm10-3h8v11h-8V10Z",
  analyze: "M4 4h16v4H4V4Zm0 6h10v10H4V10Zm12 0h4v4h-4v-4Zm0 6h4v4h-4v-4Z",
  comments: "M4 4h16v11H7l-3 3V4Z",
  chart: "M4 20V10m6 10V4m6 16v-7m6 7V8",
  settings: "M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6Zm8-3a8 8 0 0 0-.2-1.8l2-1.6-2-3.4-2.4 1a8 8 0 0 0-3-1.8L14 2h-4l-.4 2.4a8 8 0 0 0-3 1.8l-2.4-1-2 3.4 2 1.6A8 8 0 0 0 4 12c0 .6.1 1.2.2 1.8l-2 1.6 2 3.4 2.4-1a8 8 0 0 0 3 1.8L10 22h4l.4-2.4a8 8 0 0 0 3-1.8l2.4 1 2-3.4-2-1.6c.1-.6.2-1.2.2-1.8Z",
  sun: "M12 3v2m0 14v2M4.2 4.2l1.4 1.4m12.8 12.8 1.4 1.4M3 12h2m14 0h2M4.2 19.8l1.4-1.4M18.4 5.6l1.4-1.4M12 8a4 4 0 1 0 0 8 4 4 0 0 0 0-8Z",
  moon: "M20 14.5A8.5 8.5 0 1 1 9.5 4a7 7 0 0 0 10.5 10.5Z",
  globe: "M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20Zm0 0c2.5 2.7 4 6.2 4 10s-1.5 7.3-4 10m0-20C9.5 4.7 8 8.2 8 12s1.5 7.3 4 10M2.5 9h19M2.5 15h19",
  bell: "M6 8a6 6 0 1 1 12 0c0 5 2 6 2 6H4s2-1 2-6Zm4 10a2 2 0 0 0 4 0",
  search: "M11 4a7 7 0 1 0 0 14 7 7 0 0 0 0-14Zm10 17-5.4-5.4",
  trash: "M4 7h16M9 7V4h6v3m-8 0 1 13h8l1-13",
  eye: "M2 12s4-7 10-7 10 7 10 7-4 7-10 7-10-7-10-7Zm10 3a3 3 0 1 0 0-6 3 3 0 0 0 0 6Z",
  copy: "M9 9h11v11H9V9ZM4 4h11v11H4V4Z",
  download: "M12 3v13m0 0-4-4m4 4 4-4M4 20h16",
  x: "M6 6l12 12M18 6 6 18",
  user: "M12 12a5 5 0 1 0 0-10 5 5 0 0 0 0 10Zm0 2c-5 0-9 2.5-9 6v2h18v-2c0-3.5-4-6-9-6Z",
  logout: "M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4m6 14 5-5-5-5m5 5H9",
  sparkles: "M12 2l1.8 5.2L19 9l-5.2 1.8L12 16l-1.8-5.2L5 9l5.2-1.8L12 2Z",
  upload: "M12 16V4m0 0-4 4m4-4 4 4M4 20h16",
  paste: "M9 3h6v4H9V3ZM6 7h12v14H6V7Z",
  clear: "M6 6l12 12M18 6 6 18",
  menu: "M4 6h16M4 12h16M4 18h16",
  check: "M20 6 9 17l-5-5",
  file: "M6 2h9l5 5v15H6V2Zm9 0v5h5",
  users: "M9 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8Zm-7 9c0-3.9 3.1-7 7-7s7 3.1 7 7M17 11a3.5 3.5 0 1 0 0-7m2 16c0-2.8-1.6-5.2-4-6.4",
  edit: "M4 20h4l10-10-4-4L4 16v4Zm12.5-12.5 2.5 2.5",
};
function Icon({ name, size = 16, className = "" }) {
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8"
      strokeLinecap="round" strokeLinejoin="round" className={className}>
      <path d={ICONS[name] || ""} />
    </svg>
  );
}
function MosqueLogo({ size = 26, className = "" }) {
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="none" className={className}>
      <path d="M12 2C9 6 8 8 8 11a4 4 0 008 0c0-3-1-5-4-9z" stroke="currentColor" strokeWidth="1.4" />
      <path d="M4 21v-3a8 8 0 0116 0v3" stroke="currentColor" strokeWidth="1.4" />
    </svg>
  );
}

/* ============== I18N ============== */
const T = {
  ar: {
    appName: "الحج والعمرة", appSub: "نظام تحليل مشاعر التعليقات",
    welcomeBack: "مرحباً بعودتك", signInSub: "الرجاء تسجيل الدخول إلى حسابك",
    loginHeadline: "تحليل ملاحظات الحجاج والمعتمرين لتحسين الخدمات وتعزيز تجربة الحج والعمرة.",
    email: "البريد الإلكتروني", password: "كلمة المرور", signIn: "تسجيل الدخول",
    dashboard: "لوحة التحكم", analyzeComment: "تحليل تعليق", comments: "التعليقات", settings: "الإعدادات",
    analytics: "التحليلات", reports: "التقارير", users: "المستخدمون", profile: "الملف الشخصي",
    logout: "تسجيل الخروج", totalComments: "إجمالي التعليقات", positive: "إيجابي", negative: "سلبي", neutral: "محايد",
    ofTotal: "من الإجمالي", sentimentDistribution: "توزيع المشاعر", sentimentByCategory: "المشاعر حسب الفئة",
    sentimentOverTime: "المشاعر عبر الزمن", recentComments: "أحدث التعليقات",
    topKeywords: "أبرز الكلمات المفتاحية", enterComment: "أدخل التعليق",
    writeComment: "اكتب أو الصق تعليق أحد الحجاج هنا (عربي أو إنجليزي)...", analyze: "تحليل", clear: "مسح",
    analyzing: "جاري التحليل...", analysisResult: "نتيجة التحليل", confidenceScore: "درجة الثقة",
    keywordsDetected: "الكلمات المفتاحية المكتشفة", noKeywords: "لم يتم اكتشاف كلمات مشاعر قوية.",
    howItWorks: "كيف يعمل", step1: "أدخل التعليق", step1d: "اكتب أو الصق أي تعليق عن خدمات الحج والعمرة.",
    step2: "تحليل الذكاء الاصطناعي", step2d: "يقوم النموذج بتحليل النص باستخدام TF-IDF و Naive Bayes.",
    step3: "احصل على النتيجة", step3d: "شاهد نتائج المشاعر والتفاصيل فوراً.",
    search: "ابحث في التعليقات...", allSentiments: "كل المشاعر", allCategories: "كل الفئات",
    category: "الفئة", date: "التاريخ", sentiment: "الشعور", actions: "إجراءات", delete: "حذف", view: "عرض", edit: "تعديل", cancel: "إلغاء",
    exportCsv: "تصدير CSV", showing: "عرض", of: "من", theme: "المظهر", light: "فاتح", dark: "داكن",
    language: "اللغة", loading: "جاري التحميل...", connectedBackend: "متصل بالخادم الحقيقي",
    backendOffline: "الخادم غير متصل — شغّل python app.py أولاً", close: "إغلاق",
    generateReport: "إنشاء تقرير", print: "طباعة / حفظ PDF", reportSummary: "الملخص",
    addUser: "إضافة مستخدم", name: "الاسم", role: "الصلاحية", admin: "مدير", manager: "مشرف", viewer: "مشاهد",
    save: "حفظ التغييرات",
    loginFailed: "بيانات الدخول غير صحيحة", demoLogin: "بيانات تجريبية", noAccount: "ليس لديك حساب؟",
    signUp: "إنشاء حساب", signUpSub: "أنشئ حسابك للوصول إلى النظام", createAccount: "إنشاء الحساب",
    backToLogin: "الرجوع لتسجيل الدخول", forgotPassword: "نسيت كلمة المرور؟",
    forgotSub: "أدخل بريدك الإلكتروني وسنرسل لك رابط إعادة التعيين", sendResetLink: "إرسال رابط الاستعادة",
    servicesCat: "Services", crowdCat: "Crowd Management", transportCat: "Transportation",
    foodCat: "Food", staffCat: "Staff Behavior", accomCat: "Accommodation", generalCat: "General",
  },
  en: {
    appName: "Hajj & Umrah", appSub: "Sentiment Analysis System",
    welcomeBack: "Welcome Back", signInSub: "Please sign in to your account",
    loginHeadline: "Analyzing pilgrims' feedback to improve services and enhance the Hajj & Umrah experience.",
    email: "Email Address", password: "Password", signIn: "Sign In",
    dashboard: "Dashboard", analyzeComment: "Analyze Comment", comments: "Comments", settings: "Settings",
    analytics: "Analytics", reports: "Reports", users: "Users", profile: "Profile",
    logout: "Logout", totalComments: "Total Comments", positive: "Positive", negative: "Negative", neutral: "Neutral",
    ofTotal: "of total", sentimentDistribution: "Sentiment Distribution", sentimentByCategory: "Sentiment by Category",
    sentimentOverTime: "Sentiment Over Time", recentComments: "Recent Comments",
    topKeywords: "Top Keywords", enterComment: "Enter Comment",
    writeComment: "Write or paste a pilgrim comment here (Arabic or English)...", analyze: "Analyze", clear: "Clear",
    analyzing: "Analyzing...", analysisResult: "Analysis Result", confidenceScore: "Confidence Score",
    keywordsDetected: "Keywords Detected", noKeywords: "No strong sentiment keywords detected.",
    howItWorks: "How it works", step1: "Enter Comment", step1d: "Type or paste any comment about Hajj & Umrah services.",
    step2: "AI Analysis", step2d: "The model analyzes the text using TF-IDF and Naive Bayes.",
    step3: "Get Result", step3d: "View sentiment results and detailed insights instantly.",
    search: "Search comments...", allSentiments: "All Sentiments", allCategories: "All Categories",
    category: "Category", date: "Date", sentiment: "Sentiment", actions: "Actions", delete: "Delete", view: "View", edit: "Edit", cancel: "Cancel",
    exportCsv: "Export CSV", showing: "Showing", of: "of", theme: "Theme", light: "Light", dark: "Dark",
    language: "Language", loading: "Loading...", connectedBackend: "Connected to live backend",
    backendOffline: "Backend offline — run python app.py first", close: "Close",
    generateReport: "Generate Report", print: "Print / Save PDF", reportSummary: "Summary",
    addUser: "Add User", name: "Name", role: "Role", admin: "Admin", manager: "Manager", viewer: "Viewer",
    save: "Save Changes",
    loginFailed: "Invalid login credentials", demoLogin: "Demo login", noAccount: "Don't have an account?",
    signUp: "Sign up", signUpSub: "Create your account to access the system", createAccount: "Create Account",
    backToLogin: "Back to login", forgotPassword: "Forgot Password?",
    forgotSub: "Enter your email and we'll send you a reset link", sendResetLink: "Send Reset Link",
    servicesCat: "Services", crowdCat: "Crowd Management", transportCat: "Transportation",
    foodCat: "Food", staffCat: "Staff Behavior", accomCat: "Accommodation", generalCat: "General",
  },
};
const CATS = ["servicesCat", "crowdCat", "transportCat", "foodCat", "staffCat", "accomCat", "generalCat"];
const CAT_LABEL_TO_KEY = { Services: "servicesCat", "Crowd Management": "crowdCat", Transportation: "transportCat",
  Food: "foodCat", "Staff Behavior": "staffCat", Accommodation: "accomCat", General: "generalCat" };
const COLORS = { positive: "#059669", negative: "#e11d48", neutral: "#9ca3af" };

/* ============== SMALL UI ============== */
const Card = ({ children, className = "", dark }) => (
  <div className={`rounded-2xl border shadow-sm ${dark ? "bg-slate-900 border-slate-800" : "bg-white border-gray-100"} ${className}`}>{children}</div>
);
const Badge = ({ s, t }) => {
  const map = { positive: "bg-emerald-100 text-emerald-700", negative: "bg-rose-100 text-rose-700", neutral: "bg-gray-200 text-gray-600" };
  return <span className={`px-2.5 py-1 rounded-full text-xs font-medium ${map[s]}`}>{t[s]}</span>;
};
const PILL = "px-3 py-2 rounded-xl text-sm border focus:outline-none focus:ring-2 focus:ring-emerald-500 w-full";

/* ============== CHART.JS WRAPPER ============== */
function ChartCanvas({ type, data, options, height = 220 }) {
  const ref = useRef(null);
  const chartRef = useRef(null);
  useEffect(() => {
    if (!ref.current) return;
    chartRef.current = new Chart(ref.current.getContext("2d"), { type, data, options });
    return () => {
      // Destroy exactly once, then clear the ref — without this, the next
      // effect run saw a stale (already-destroyed) chart instance and called
      // destroy() on it a second time, which throws inside Chart.js.
      if (chartRef.current) {
        chartRef.current.destroy();
        chartRef.current = null;
      }
    };
  }, [type, JSON.stringify(data), JSON.stringify(options)]);
  return <div style={{ height }}><canvas ref={ref}></canvas></div>;
}

/* ============== BACKEND STATUS BANNER ============== */
function BackendBanner({ t, online }) {
  return (
    <div className={`text-xs px-3 py-2 rounded-lg mb-3 flex items-center gap-2 ${online ? "bg-emerald-50 text-emerald-700" : "bg-rose-50 text-rose-700"}`}>
      <span className={`w-2 h-2 rounded-full ${online ? "bg-emerald-500" : "bg-rose-500"}`}></span>
      {online ? t.connectedBackend : t.backendOffline}
    </div>
  );
}

/* ============== LOGIN ============== */
function Login({ t, lang, setLang, dark, setDark, onLogin }) {
  const [mode, setMode] = useState("login"); // login | signup | forgot
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [pw, setPw] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [info, setInfo] = useState("");

  const reset = () => { setError(""); setInfo(""); };

  const submitLogin = async (e) => {
    e.preventDefault(); reset(); setLoading(true);
    try {
      const r = await apiFetch(`${API}/auth/login`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ email, password: pw }) });
      const data = await r.json();
      if (!r.ok) { setError(data.error || t.loginFailed); setLoading(false); return; }
      onLogin(data);
    } catch { setError(t.backendOffline); }
    setLoading(false);
  };

  const submitSignup = async (e) => {
    e.preventDefault(); reset(); setLoading(true);
    try {
      const r = await apiFetch(`${API}/auth/signup`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ name, email, password: pw }) });
      const data = await r.json();
      if (!r.ok) { setError(data.error || t.loginFailed); setLoading(false); return; }
      onLogin(data);
    } catch { setError(t.backendOffline); }
    setLoading(false);
  };

  const submitForgot = async (e) => {
    e.preventDefault(); reset(); setLoading(true);
    try {
      const r = await apiFetch(`${API}/auth/forgot-password`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ email }) });
      const data = await r.json();
      setInfo(data.message);
    } catch { setError(t.backendOffline); }
    setLoading(false);
  };

  return (
    <div className={`min-h-screen flex items-center justify-center p-4 ${dark ? "bg-slate-950" : "bg-emerald-50"}`}>
      <div className="absolute top-4 inset-x-4 flex justify-end gap-2 z-10">
        <button onClick={() => setLang(lang === "ar" ? "en" : "ar")} className={`px-3 py-2 rounded-full text-sm font-medium shadow ${dark ? "bg-slate-800 text-gray-200" : "bg-white text-emerald-900"}`}>
          <Icon name="globe" size={14} /> {lang === "ar" ? "EN" : "AR"}
        </button>
        <button onClick={() => setDark(!dark)} className={`w-9 h-9 flex items-center justify-center rounded-full shadow ${dark ? "bg-slate-800 text-amber-300" : "bg-white text-emerald-900"}`}>
          <Icon name={dark ? "sun" : "moon"} size={16} />
        </button>
      </div>
      <div className={`w-full max-w-4xl grid md:grid-cols-2 rounded-3xl overflow-hidden shadow-2xl ${dark ? "bg-slate-900" : "bg-white"}`}>
        <div className="relative hidden md:flex flex-col justify-end p-8 text-white min-h-[520px]"
          style={{ background: "linear-gradient(180deg, rgba(3,30,22,.55), rgba(3,20,15,.9)), url(https://images.unsplash.com/photo-1591604129939-f1efa4d9f7fa?q=80&w=1200&auto=format&fit=crop) center/cover" }}>
          <svg width="52" height="52" viewBox="0 0 24 24" fill="none" className="mb-4 text-amber-300">
            <path d="M12 2C9 6 8 8 8 11a4 4 0 008 0c0-3-1-5-4-9z" stroke="currentColor" strokeWidth="1.4" />
            <path d="M4 21v-3a8 8 0 0116 0v3" stroke="currentColor" strokeWidth="1.4" />
          </svg>
          <h1 className="text-3xl font-bold mb-2">{t.appName}</h1>
          <p className="text-white/70 text-sm mb-3">{t.appSub}</p>
          <div className="h-px w-16 bg-amber-300/70 mb-3" />
          <p className="text-white/80 text-sm leading-relaxed max-w-xs">{t.loginHeadline}</p>
        </div>

        {mode === "login" && (
          <form onSubmit={submitLogin} className="p-8 md:p-10 flex flex-col justify-center">
            <div className={`w-14 h-14 rounded-full flex items-center justify-center mx-auto mb-4 ${dark ? "bg-slate-800" : "bg-emerald-50"}`}>
              <Icon name="user" size={22} className={dark ? "text-emerald-300" : "text-emerald-700"} />
            </div>
            <h2 className={`font-bold text-center ${dark ? "text-white" : "text-gray-900"}`}>{t.welcomeBack}</h2>
            <p className={`text-sm text-center mb-5 ${dark ? "text-gray-400" : "text-gray-500"}`}>{t.signInSub}</p>
            {error && <p className="text-rose-600 text-xs text-center mb-3">{error}</p>}
            <input required type="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder={t.email}
              className={`${PILL} mb-3 ${dark ? "bg-slate-800 border-slate-700 text-white" : "border-gray-200"}`} />
            <input required type="password" value={pw} onChange={(e) => setPw(e.target.value)} placeholder={t.password}
              className={`${PILL} mb-2 ${dark ? "bg-slate-800 border-slate-700 text-white" : "border-gray-200"}`} />
            <div className="flex justify-end mb-4">
              <button type="button" onClick={() => { setMode("forgot"); reset(); }} className="text-xs text-emerald-600 font-medium">{t.forgotPassword}</button>
            </div>
            <button disabled={loading} className="w-full bg-emerald-700 hover:bg-emerald-800 text-white rounded-xl py-2.5 font-medium">
              {loading ? "..." : t.signIn}
            </button>
            <p className={`text-center text-xs mt-4 ${dark ? "text-gray-500" : "text-gray-500"}`}>
              {t.demoLogin}: admin@hajj.sa / admin123
            </p>
            <p className={`text-center text-sm mt-3 ${dark ? "text-gray-400" : "text-gray-500"}`}>
              {t.noAccount} <button type="button" onClick={() => { setMode("signup"); reset(); }} className="text-emerald-600 font-medium">{t.signUp}</button>
            </p>
          </form>
        )}

        {mode === "signup" && (
          <form onSubmit={submitSignup} className="p-8 md:p-10 flex flex-col justify-center">
            <h2 className={`font-bold text-center ${dark ? "text-white" : "text-gray-900"}`}>{t.signUp}</h2>
            <p className={`text-sm text-center mb-5 ${dark ? "text-gray-400" : "text-gray-500"}`}>{t.signUpSub}</p>
            {error && <p className="text-rose-600 text-xs text-center mb-3">{error}</p>}
            <input required value={name} onChange={(e) => setName(e.target.value)} placeholder={t.name}
              className={`${PILL} mb-3 ${dark ? "bg-slate-800 border-slate-700 text-white" : "border-gray-200"}`} />
            <input required type="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder={t.email}
              className={`${PILL} mb-3 ${dark ? "bg-slate-800 border-slate-700 text-white" : "border-gray-200"}`} />
            <input required type="password" minLength={6} value={pw} onChange={(e) => setPw(e.target.value)} placeholder={t.password}
              className={`${PILL} mb-4 ${dark ? "bg-slate-800 border-slate-700 text-white" : "border-gray-200"}`} />
            <button disabled={loading} className="w-full bg-emerald-700 hover:bg-emerald-800 text-white rounded-xl py-2.5 font-medium">
              {loading ? "..." : t.createAccount}
            </button>
            <p className={`text-center text-sm mt-4 ${dark ? "text-gray-400" : "text-gray-500"}`}>
              <button type="button" onClick={() => { setMode("login"); reset(); }} className="text-emerald-600 font-medium">{t.backToLogin}</button>
            </p>
          </form>
        )}

        {mode === "forgot" && (
          <form onSubmit={submitForgot} className="p-8 md:p-10 flex flex-col justify-center">
            <h2 className={`font-bold text-center ${dark ? "text-white" : "text-gray-900"}`}>{t.forgotPassword}</h2>
            <p className={`text-sm text-center mb-5 ${dark ? "text-gray-400" : "text-gray-500"}`}>{t.forgotSub}</p>
            {error && <p className="text-rose-600 text-xs text-center mb-3">{error}</p>}
            {info && <p className="text-emerald-600 text-xs text-center mb-3">{info}</p>}
            <input required type="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder={t.email}
              className={`${PILL} mb-4 ${dark ? "bg-slate-800 border-slate-700 text-white" : "border-gray-200"}`} />
            <button disabled={loading} className="w-full bg-emerald-700 hover:bg-emerald-800 text-white rounded-xl py-2.5 font-medium">
              {loading ? "..." : t.sendResetLink}
            </button>
            <p className={`text-center text-sm mt-4 ${dark ? "text-gray-400" : "text-gray-500"}`}>
              <button type="button" onClick={() => { setMode("login"); reset(); }} className="text-emerald-600 font-medium">{t.backToLogin}</button>
            </p>
          </form>
        )}
      </div>
    </div>
  );
}

/* ============== SIDEBAR + TOPBAR ============== */
function Sidebar({ t, page, setPage, dark, lang, open, setOpen, onLogout }) {
  const items = [
    ["dashboard", "dashboard"], ["analyzeComment", "analyze"], ["comments", "comments"],
    ["analytics", "chart"], ["reports", "file"], ["users", "users"], ["profile", "user"], ["settings", "settings"],
  ];
  return (
    <div className={`${open ? "translate-x-0" : lang === "ar" ? "translate-x-full md:translate-x-0" : "-translate-x-full md:translate-x-0"}
      fixed md:static z-40 top-0 bottom-0 ${lang === "ar" ? "right-0" : "left-0"} w-64 transition-transform p-4 flex flex-col justify-between
      ${dark ? "bg-slate-950" : "bg-emerald-950"} text-white`}>
      <div>
        <div className="flex items-center gap-2 px-1 mb-8">
          <MosqueLogo size={26} className="text-amber-300 shrink-0" />
          <div>
            <div className="font-bold leading-tight">{t.appName}</div>
            <div className="text-[11px] text-emerald-200/70 leading-tight">{t.appSub}</div>
          </div>
        </div>
        <nav className="space-y-1">
          {items.map(([key, icon]) => (
            <button key={key} onClick={() => { setPage(key); setOpen(false); }}
              className={`w-full flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm ${page === key ? "bg-emerald-700" : "text-emerald-100/80 hover:bg-emerald-900/60"}`}>
              <Icon name={icon} size={16} /> {t[key]}
            </button>
          ))}
        </nav>
      </div>
      <button onClick={onLogout} className="flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm text-emerald-100/70 hover:bg-emerald-900/60">
        <Icon name="logout" size={16} /> {t.logout}
      </button>
    </div>
  );
}
function Topbar({ t, lang, setLang, dark, setDark, title, setOpen, user }) {
  return (
    <div className={`sticky top-0 z-20 flex items-center justify-between px-4 md:px-6 py-3.5 border-b ${dark ? "bg-slate-950/90 border-slate-800" : "bg-white/90 border-gray-100"}`}>
      <div className="flex items-center gap-3">
        <button className="md:hidden" onClick={() => setOpen((v) => !v)}><Icon name="menu" className={dark ? "text-gray-300" : "text-gray-600"} /></button>
        <h1 className={`font-bold text-lg ${dark ? "text-white" : "text-gray-900"}`}>{title}</h1>
      </div>
      <div className="flex items-center gap-2">
        <button onClick={() => setLang(lang === "ar" ? "en" : "ar")} className={`px-3 py-1.5 rounded-full text-xs border ${dark ? "border-slate-700 text-gray-200" : "border-gray-200 text-gray-700"}`}>
          {lang === "ar" ? "English" : "العربية"}
        </button>
        <button onClick={() => setDark(!dark)} className={`w-9 h-9 flex items-center justify-center rounded-full border ${dark ? "border-slate-700 text-amber-300" : "border-gray-200 text-gray-600"}`}>
          <Icon name={dark ? "sun" : "moon"} size={16} />
        </button>
        {user && (
          <div className={`w-9 h-9 rounded-full flex items-center justify-center font-semibold text-sm ${dark ? "bg-emerald-800 text-emerald-100" : "bg-emerald-100 text-emerald-800"}`}>
            {(user.name || "?").charAt(0).toUpperCase()}
          </div>
        )}
      </div>
    </div>
  );
}

/* ============== DASHBOARD ============== */
function Dashboard({ t, dark, online, lang }) {
  const [stats, setStats] = useState(null);
  const [recent, setRecent] = useState([]);
  useEffect(() => {
    apiFetch(`${API}/dashboard/stats`).then((r) => r.json()).then(setStats).catch(() => setStats(null));
    apiFetch(`${API}/comments?per_page=100&sort=date`).then((r) => r.json()).then((d) => setRecent(d.items || [])).catch(() => setRecent([]));
  }, [online]);

  if (!stats) return <div className="p-6"><Card dark={dark} className="p-8 text-center"><BackendBanner t={t} online={online} /></Card></div>;

  const pie = {
    labels: [t.positive, t.negative, t.neutral],
    datasets: [{ data: [stats.positive, stats.negative, stats.neutral], backgroundColor: [COLORS.positive, COLORS.negative, COLORS.neutral] }],
  };
  const catLabels = Object.keys(stats.by_category);
  const bar = {
    labels: catLabels.map((c) => t[CAT_LABEL_TO_KEY[c]] || c),
    datasets: [
      { label: t.positive, data: catLabels.map((c) => stats.by_category[c].positive || 0), backgroundColor: COLORS.positive },
      { label: t.negative, data: catLabels.map((c) => stats.by_category[c].negative || 0), backgroundColor: COLORS.negative },
    ],
  };

  const days = [];
  for (let i = 6; i >= 0; i--) {
    const d = new Date(Date.now() - i * 24 * 3600 * 1000);
    const dayComments = recent.filter((c) => new Date(c.created_at).toDateString() === d.toDateString());
    days.push({
      label: d.toLocaleDateString(lang === "ar" ? "ar" : "en", { weekday: "short" }),
      positive: dayComments.filter((c) => c.sentiment === "positive").length,
      negative: dayComments.filter((c) => c.sentiment === "negative").length,
    });
  }
  const trend = {
    labels: days.map((d) => d.label),
    datasets: [
      { label: t.positive, data: days.map((d) => d.positive), borderColor: COLORS.positive, backgroundColor: COLORS.positive + "33", tension: 0.35, fill: true },
      { label: t.negative, data: days.map((d) => d.negative), borderColor: COLORS.negative, backgroundColor: COLORS.negative + "22", tension: 0.35, fill: true },
    ],
  };

  return (
    <div className="p-4 md:p-6 space-y-5">
      <BackendBanner t={t} online={online} />
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
        {[[t.totalComments, stats.total, "#0369a1"], [t.positive, stats.positive, COLORS.positive],
        [t.negative, stats.negative, COLORS.negative], [t.neutral, stats.neutral, COLORS.neutral]].map(([label, val, color]) => (
          <Card dark={dark} className="p-4" key={label}>
            <div className={`text-xs mb-1 ${dark ? "text-gray-400" : "text-gray-500"}`}>{label}</div>
            <div className={`text-2xl font-bold ${dark ? "text-white" : "text-gray-900"}`} style={{ color }}>{val}</div>
          </Card>
        ))}
      </div>
      <div className="grid lg:grid-cols-3 gap-4">
        <Card dark={dark} className="p-4 lg:col-span-1">
          <div className={`font-semibold mb-2 ${dark ? "text-white" : "text-gray-900"}`}>{t.sentimentDistribution}</div>
          <ChartCanvas type="doughnut" data={pie} options={{ maintainAspectRatio: false }} />
        </Card>
        <Card dark={dark} className="p-4 lg:col-span-2">
          <div className={`font-semibold mb-2 ${dark ? "text-white" : "text-gray-900"}`}>{t.sentimentOverTime}</div>
          <ChartCanvas type="line" data={trend} options={{ maintainAspectRatio: false }} />
        </Card>
      </div>
      <div className="grid lg:grid-cols-2 gap-4">
        <Card dark={dark} className="p-4">
          <div className={`font-semibold mb-2 ${dark ? "text-white" : "text-gray-900"}`}>{t.sentimentByCategory}</div>
          <ChartCanvas type="bar" data={bar} options={{ maintainAspectRatio: false, scales: { x: { stacked: false } } }} />
        </Card>
        <Card dark={dark} className="p-4">
          <div className={`font-semibold mb-3 ${dark ? "text-white" : "text-gray-900"}`}>{t.recentComments}</div>
          <div className="space-y-2 max-h-56 overflow-auto pr-1">
            {recent.slice(0, 6).map((c) => (
              <div key={c.id} className={`flex items-center justify-between gap-3 p-2.5 rounded-xl ${dark ? "bg-slate-800/60" : "bg-gray-50"}`}>
                <div className={`text-xs truncate flex-1 ${dark ? "text-gray-300" : "text-gray-700"}`}>{c.text}</div>
                <Badge s={c.sentiment} t={t} />
              </div>
            ))}
            {!recent.length && <div className={`text-xs ${dark ? "text-gray-500" : "text-gray-400"}`}>—</div>}
          </div>
        </Card>
      </div>
      <Card dark={dark} className="p-4">
        <div className={`font-semibold mb-3 ${dark ? "text-white" : "text-gray-900"}`}>{t.topKeywords}</div>
        <div className="flex flex-wrap gap-2">
          {stats.top_keywords.map(([w, n]) => (
            <span key={w} className={`px-2.5 py-1 rounded-full text-xs ${dark ? "bg-slate-800 text-gray-200" : "bg-emerald-50 text-emerald-800"}`} style={{ fontSize: 10 + Math.min(n, 6) * 1.5 }}>{w}</span>
          ))}
        </div>
      </Card>
    </div>
  );
}

/* ============== ANALYZE ============== */
function AnalyzeComment({ t, dark, online, onAnalyzed }) {
  const [text, setText] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [category, setCategory] = useState("General");

  const run = async () => {
    if (!text.trim()) return;
    setLoading(true); setResult(null);
    try {
      const r = await apiFetch(`${API}/analyze`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ text }) });
      const data = await r.json();
      setResult(data);
      // also persist it as a real comment in the database
      apiFetch(`${API}/comments`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ text, category }) })
        .then(() => onAnalyzed && onAnalyzed());
    } catch { setResult({ error: true }); }
    setLoading(false);
  };
  const emoji = result && !result.error ? (result.label === "positive" ? "😊" : result.label === "negative" ? "😠" : "😐") : null;

  return (
    <div className="p-4 md:p-6 grid lg:grid-cols-2 gap-5">
      <div className="space-y-5">
        <Card dark={dark} className="overflow-hidden">
          <div className="relative p-6 text-white min-h-[130px] flex flex-col justify-center"
            style={{ background: "linear-gradient(120deg, rgba(3,30,22,.7), rgba(3,20,15,.35)), url(https://images.unsplash.com/photo-1591604129939-f1efa4d9f7fa?q=80&w=1200&auto=format&fit=crop) center/cover" }}>
            <h2 className="text-xl font-bold">{t.analyzeComment}</h2>
            <p className="text-white/80 text-sm mt-1 max-w-md">{t.writeComment}</p>
          </div>
        </Card>
        <Card dark={dark} className="p-5">
          <BackendBanner t={t} online={online} />
          <div className={`font-semibold mb-3 ${dark ? "text-white" : "text-gray-900"}`}>{t.enterComment}</div>
          <textarea value={text} onChange={(e) => setText(e.target.value)} rows={7} placeholder={t.writeComment}
            className={`w-full rounded-xl border p-3 text-sm resize-none focus:outline-none focus:ring-2 focus:ring-emerald-500 ${dark ? "bg-slate-800 border-slate-700 text-white" : "border-gray-200"}`} />
          <select value={category} onChange={(e) => setCategory(e.target.value)} className={`${PILL} mt-3 ${dark ? "bg-slate-800 border-slate-700 text-white" : "border-gray-200"}`}>
            {CATS.map((c) => <option key={c} value={Object.keys(CAT_LABEL_TO_KEY).find((k) => CAT_LABEL_TO_KEY[k] === c) || c}>{t[c]}</option>)}
          </select>
          <div className="flex gap-2 mt-3">
            <button onClick={run} className="flex items-center gap-1.5 bg-emerald-700 hover:bg-emerald-800 text-white px-4 py-2 rounded-xl text-sm font-medium">
              <Icon name="sparkles" size={15} /> {loading ? t.analyzing : t.analyze}
            </button>
            <button onClick={() => { setText(""); setResult(null); }} className={`flex items-center gap-1.5 px-3 py-2 rounded-xl text-sm border ${dark ? "border-slate-700 text-gray-200" : "border-gray-200 text-gray-600"}`}>
              <Icon name="clear" size={14} /> {t.clear}
            </button>
          </div>
        </Card>
        <Card dark={dark} className="p-5">
          <div className={`text-sm font-semibold mb-3 ${dark ? "text-white" : "text-gray-900"}`}>{t.howItWorks}</div>
          <div className="grid grid-cols-3 gap-3 text-center">
            {[["analyze", t.step1, t.step1d], ["sparkles", t.step2, t.step2d], ["chart", t.step3, t.step3d]].map(([icon, title, desc], i) => (
              <div key={i} className={`p-3 rounded-xl ${dark ? "bg-slate-800/60" : "bg-emerald-50/60"}`}>
                <Icon name={icon} size={18} className="text-emerald-600 mx-auto mb-1.5" />
                <div className={`text-xs font-medium ${dark ? "text-gray-200" : "text-gray-800"}`}>{title}</div>
                <div className={`text-[10px] mt-1 ${dark ? "text-gray-500" : "text-gray-500"}`}>{desc}</div>
              </div>
            ))}
          </div>
        </Card>
      </div>

      <Card dark={dark} className="p-5 min-h-[260px]">
        {!result && !loading && <div className={`h-full flex items-center justify-center text-sm ${dark ? "text-gray-500" : "text-gray-400"}`}>{t.analysisResult}</div>}
        {loading && <div className={`h-full flex items-center justify-center text-sm ${dark ? "text-gray-400" : "text-gray-500"}`}>{t.analyzing}</div>}
        {result && !loading && !result.error && (
          <>
            <div className={`font-semibold mb-3 ${dark ? "text-white" : "text-gray-900"}`}>{t.analysisResult}</div>
            <div className="flex items-center gap-4 mb-4">
              <div className="text-4xl">{emoji}</div>
              <div>
                <Badge s={result.label} t={t} />
                <div className={`text-xs mt-1 ${dark ? "text-gray-400" : "text-gray-500"}`}>{t.confidenceScore}: <b>{result.confidence}%</b></div>
              </div>
            </div>
            {["positive", "negative", "neutral"].map((k) => (
              <div key={k} className="flex items-center gap-2 text-xs mb-1.5">
                <span className={`w-14 ${dark ? "text-gray-400" : "text-gray-500"}`}>{t[k]}</span>
                <div className={`flex-1 h-1.5 rounded-full overflow-hidden ${dark ? "bg-slate-800" : "bg-gray-100"}`}>
                  <div className="h-full rounded-full" style={{ width: `${result.scores[k]}%`, background: COLORS[k] }} />
                </div>
                <span className={`w-8 text-right ${dark ? "text-gray-400" : "text-gray-500"}`}>{result.scores[k]}%</span>
              </div>
            ))}
            <div className={`mt-4 pt-4 border-t ${dark ? "border-slate-800" : "border-gray-100"}`}>
              <div className={`text-sm font-semibold mb-2 ${dark ? "text-white" : "text-gray-900"}`}>{t.keywordsDetected}</div>
              {result.keywords.length ? (
                <div className="flex flex-wrap gap-2">
                  {result.keywords.map((k) => (
                    <span key={k} className={`px-2.5 py-1 rounded-lg text-xs font-medium ${result.negative_keywords.includes(k) ? "bg-rose-50 text-rose-600" : "bg-emerald-50 text-emerald-700"}`}>{k}</span>
                  ))}
                </div>
              ) : <p className={`text-sm ${dark ? "text-gray-400" : "text-gray-500"}`}>{t.noKeywords}</p>}
            </div>
          </>
        )}
        {result && result.error && <div className="text-rose-500 text-sm">{t.backendOffline}</div>}
      </Card>
    </div>
  );
}

/* ============== COMMENTS ============== */
function CommentsPage({ t, dark, online, refreshKey }) {
  const [items, setItems] = useState([]);
  const [total, setTotal] = useState(0);
  const [query, setQuery] = useState("");
  const [sentFilter, setSentFilter] = useState("all");
  const [page, setPage] = useState(1);
  const perPage = 8;

  const load = () => {
    const params = new URLSearchParams({ search: query, sentiment: sentFilter, page, per_page: perPage });
    apiFetch(`${API}/comments?${params}`).then((r) => r.json()).then((d) => { setItems(d.items || []); setTotal(d.total || 0); }).catch(() => { setItems([]); setTotal(0); });
  };
  useEffect(load, [query, sentFilter, page, online, refreshKey]);

  const del = (id) => apiFetch(`${API}/comments/${id}`, { method: "DELETE" }).then(load);
  const exportCsv = () => window.open(`${API}/comments/export?format=csv`, "_blank");

  return (
    <div className="p-4 md:p-6 space-y-4">
      <BackendBanner t={t} online={online} />
      <Card dark={dark} className="p-4 flex flex-wrap gap-2 items-center">
        <input value={query} onChange={(e) => { setQuery(e.target.value); setPage(1); }} placeholder={t.search}
          className={`${PILL} flex-1 min-w-[200px] ${dark ? "bg-slate-800 border-slate-700 text-white" : "border-gray-200"}`} />
        <select value={sentFilter} onChange={(e) => { setSentFilter(e.target.value); setPage(1); }} className={`${PILL} w-auto ${dark ? "bg-slate-800 border-slate-700 text-white" : "border-gray-200"}`}>
          <option value="all">{t.allSentiments}</option><option value="positive">{t.positive}</option><option value="negative">{t.negative}</option><option value="neutral">{t.neutral}</option>
        </select>
        <button onClick={exportCsv} className="flex items-center gap-1.5 text-xs px-3 py-2 rounded-xl bg-emerald-700 text-white"><Icon name="download" size={13} />{t.exportCsv}</button>
      </Card>
      <Card dark={dark} className="overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-sm">
            <thead className={dark ? "bg-slate-800/60" : "bg-gray-50"}>
              <tr className={dark ? "text-gray-400" : "text-gray-500"}>
                {["ID", t.enterComment, t.sentiment, t.category, t.date, t.actions].map((h) => <th key={h} className="text-start px-4 py-3 font-medium whitespace-nowrap">{h}</th>)}
              </tr>
            </thead>
            <tbody>
              {items.map((c) => (
                <tr key={c.id} className={`border-t ${dark ? "border-slate-800" : "border-gray-100"}`}>
                  <td className={`px-4 py-3 ${dark ? "text-gray-400" : "text-gray-500"}`}>#{c.id}</td>
                  <td className={`px-4 py-3 max-w-xs truncate ${dark ? "text-gray-200" : "text-gray-800"}`}>{c.text}</td>
                  <td className="px-4 py-3"><Badge s={c.sentiment} t={t} /></td>
                  <td className={`px-4 py-3 whitespace-nowrap ${dark ? "text-gray-400" : "text-gray-500"}`}>{t[CAT_LABEL_TO_KEY[c.category]] || c.category}</td>
                  <td className={`px-4 py-3 whitespace-nowrap ${dark ? "text-gray-400" : "text-gray-500"}`}>{new Date(c.created_at).toLocaleDateString()}</td>
                  <td className="px-4 py-3"><button onClick={() => del(c.id)} className={`p-1.5 rounded-lg ${dark ? "hover:bg-slate-800 text-rose-400" : "hover:bg-gray-100 text-rose-500"}`}><Icon name="trash" size={14} /></button></td>
                </tr>
              ))}
              {!items.length && <tr><td colSpan={6} className={`text-center py-8 text-sm ${dark ? "text-gray-500" : "text-gray-400"}`}>—</td></tr>}
            </tbody>
          </table>
        </div>
        <div className={`flex items-center justify-between px-4 py-3 border-t text-xs ${dark ? "border-slate-800 text-gray-400" : "border-gray-100 text-gray-500"}`}>
          <span>{t.showing} {items.length} {t.of} {total}</span>
          <div className="flex items-center gap-2">
            <button disabled={page === 1} onClick={() => setPage((p) => p - 1)} className="disabled:opacity-30">‹</button>
            <span>{page}</span>
            <button disabled={page * perPage >= total} onClick={() => setPage((p) => p + 1)} className="disabled:opacity-30">›</button>
          </div>
        </div>
      </Card>
    </div>
  );
}

/* ============== ANALYTICS ============== */
function AnalyticsPage({ t, dark, online }) {
  const [stats, setStats] = useState(null);
  useEffect(() => { apiFetch(`${API}/dashboard/stats`).then((r) => r.json()).then(setStats).catch(() => setStats(null)); }, [online]);
  if (!stats) return <div className="p-6"><Card dark={dark} className="p-8"><BackendBanner t={t} online={online} /></Card></div>;
  const catLabels = Object.keys(stats.by_category);
  const bar = {
    labels: catLabels.map((c) => t[CAT_LABEL_TO_KEY[c]] || c),
    datasets: [{ label: t.totalComments, data: catLabels.map((c) => stats.by_category[c].total), backgroundColor: "#059669" }],
  };
  return (
    <div className="p-4 md:p-6 space-y-4">
      <BackendBanner t={t} online={online} />
      <Card dark={dark} className="p-4">
        <div className={`font-semibold mb-2 ${dark ? "text-white" : "text-gray-900"}`}>{t.sentimentByCategory}</div>
        <ChartCanvas type="bar" data={bar} options={{ maintainAspectRatio: false }} />
      </Card>
      <Card dark={dark} className="p-4">
        <div className={`font-semibold mb-3 ${dark ? "text-white" : "text-gray-900"}`}>{t.topKeywords}</div>
        <div className="flex flex-wrap gap-2">
          {stats.top_keywords.map(([w, n]) => (
            <span key={w} className={`px-3 py-1.5 rounded-full text-xs ${dark ? "bg-slate-800 text-gray-200" : "bg-emerald-50 text-emerald-800"}`} style={{ fontSize: 11 + Math.min(n, 6) * 2 }}>{w}</span>
          ))}
        </div>
      </Card>
    </div>
  );
}

/* ============== REPORTS ============== */
function ReportsPage({ t, dark, online }) {
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  useEffect(() => {
    setLoading(true);
    setError("");
    apiFetchJson(`${API}/dashboard/stats`)
      .then((d) => setStats(d))
      .catch((e) => { setStats(null); setError(e && e.message ? e.message : "Failed to load report"); })
      .finally(() => setLoading(false));
  }, [online]);
  return (
    <div className="p-4 md:p-6 space-y-4">
      <BackendBanner t={t} online={online} />
      <Card dark={dark} className="p-4 flex justify-end">
        <button onClick={() => window.print()} className="flex items-center gap-1.5 bg-emerald-700 text-white px-4 py-2 rounded-xl text-sm"><Icon name="file" size={14} />{t.print}</button>
      </Card>
      {loading && (
        <Card dark={dark} className="p-8 text-center text-sm">
          <span className={dark ? "text-gray-400" : "text-gray-500"}>{t.analyzing || "Loading…"}</span>
        </Card>
      )}
      {!loading && error && (
        <Card dark={dark} className="p-6 text-center">
          <p className="text-rose-600 text-sm mb-3">{error}</p>
          <button onClick={() => window.location.reload()} className="text-xs bg-rose-600 text-white px-3 py-1.5 rounded-lg">Retry</button>
        </Card>
      )}
      {!loading && !error && stats && (
        <Card dark={dark} className="p-6">
          <div className="flex items-center gap-2 mb-1">
            <MosqueLogo size={22} className="text-emerald-700" />
            <h2 className={`text-lg font-bold ${dark ? "text-white" : "text-gray-900"}`}>{t.appName} — {t.generateReport}</h2>
          </div>
          <p className={`text-xs mb-5 ${dark ? "text-gray-500" : "text-gray-400"}`}>{new Date().toLocaleDateString()}</p>
          <div className={`font-semibold mb-2 ${dark ? "text-white" : "text-gray-900"}`}>{t.reportSummary}</div>
          <div className="grid grid-cols-3 gap-3">
            <div className={`p-3 rounded-xl text-center ${dark ? "bg-slate-800/60" : "bg-emerald-50"}`}><div className="text-xl font-bold text-emerald-600">{stats.positive}</div><div className={`text-xs ${dark ? "text-gray-400" : "text-gray-500"}`}>{t.positive}</div></div>
            <div className={`p-3 rounded-xl text-center ${dark ? "bg-slate-800/60" : "bg-rose-50"}`}><div className="text-xl font-bold text-rose-600">{stats.negative}</div><div className={`text-xs ${dark ? "text-gray-400" : "text-gray-500"}`}>{t.negative}</div></div>
            <div className={`p-3 rounded-xl text-center ${dark ? "bg-slate-800/60" : "bg-gray-100"}`}><div className="text-xl font-bold text-gray-600">{stats.neutral}</div><div className={`text-xs ${dark ? "text-gray-400" : "text-gray-500"}`}>{t.neutral}</div></div>
          </div>
        </Card>
      )}
    </div>
  );
}

/* ============== USERS ============== */
function UsersPage({ t, dark, online }) {
  const [users, setUsers] = useState([]);
  const [editingId, setEditingId] = useState(null);
  const [draft, setDraft] = useState({ name: "", email: "", role: "viewer" });
  const [adding, setAdding] = useState(false);
  const [newUser, setNewUser] = useState({ name: "", email: "", role: "viewer", password: "" });
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);
  const [loadError, setLoadError] = useState("");

  const load = () => {
    setLoading(true);
    setLoadError("");
    return apiFetchJson(`${API}/users`)
      .then(setUsers)
      .catch((e) => { setUsers([]); setLoadError(e && e.message ? e.message : "Failed to load users"); })
      .finally(() => setLoading(false));
  };
  useEffect(() => { load(); }, [online]);

  const startEdit = (u) => { setEditingId(u.id); setDraft({ name: u.name, email: u.email, role: u.role }); };
  const saveEdit = async (id) => {
    await apiFetch(`${API}/users/${id}`, { method: "PUT", headers: { "Content-Type": "application/json" }, body: JSON.stringify(draft) });
    setEditingId(null);
    load();
  };
  const cancelEdit = () => setEditingId(null);
  const del = (id) => apiFetch(`${API}/users/${id}`, { method: "DELETE" }).then(load);

  const addUser = async () => {
    setError("");
    if (!newUser.name.trim() || !newUser.email.trim()) return;
    const r = await apiFetch(`${API}/users`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(newUser) });
    const data = await r.json();
    if (!r.ok) { setError(data.error || "Error"); return; }
    setNewUser({ name: "", email: "", role: "viewer", password: "" });
    setAdding(false);
    load();
  };

  const inputCls = `px-2 py-1.5 rounded-lg text-sm border w-full ${dark ? "bg-slate-800 border-slate-700 text-white" : "border-gray-200"}`;
  const roleSelect = (value, onChange) => (
    <select value={value} onChange={(e) => onChange(e.target.value)} className={inputCls}>
      <option value="admin">{t.admin}</option>
      <option value="manager">{t.manager}</option>
      <option value="viewer">{t.viewer}</option>
    </select>
  );

  return (
    <div className="p-4 md:p-6 space-y-4">
      <BackendBanner t={t} online={online} />
      <Card dark={dark} className="p-4 flex justify-between items-center">
        <div className={`font-semibold ${dark ? "text-white" : "text-gray-900"}`}>{t.users}</div>
        {!adding && (
          <button onClick={() => setAdding(true)} className="flex items-center gap-1.5 bg-emerald-700 text-white px-3 py-2 rounded-xl text-sm">
            <Icon name="users" size={14} />{t.addUser}
          </button>
        )}
      </Card>

      {adding && (
        <Card dark={dark} className="p-4">
          {error && <p className="text-rose-600 text-xs mb-2">{error}</p>}
          <div className="grid sm:grid-cols-4 gap-2 mb-3">
            <input placeholder={t.name} value={newUser.name} onChange={(e) => setNewUser({ ...newUser, name: e.target.value })} className={inputCls} />
            <input placeholder={t.email} value={newUser.email} onChange={(e) => setNewUser({ ...newUser, email: e.target.value })} className={inputCls} />
            <input placeholder={t.password} type="password" value={newUser.password} onChange={(e) => setNewUser({ ...newUser, password: e.target.value })} className={inputCls} />
            {roleSelect(newUser.role, (v) => setNewUser({ ...newUser, role: v }))}
          </div>
          <div className="flex gap-2">
            <button onClick={addUser} className="bg-emerald-700 text-white px-4 py-2 rounded-xl text-xs font-medium">{t.save}</button>
            <button onClick={() => setAdding(false)} className={`px-4 py-2 rounded-xl text-xs border ${dark ? "border-slate-700 text-gray-200" : "border-gray-200 text-gray-600"}`}>{t.cancel}</button>
          </div>
        </Card>
      )}

      {loading && (
        <Card dark={dark} className="p-8 text-center text-sm">
          <span className={dark ? "text-gray-400" : "text-gray-500"}>{t.analyzing || "Loading…"}</span>
        </Card>
      )}
      {!loading && loadError && (
        <Card dark={dark} className="p-6 text-center">
          <p className="text-rose-600 text-sm mb-3">{loadError}</p>
          <button onClick={load} className="text-xs bg-rose-600 text-white px-3 py-1.5 rounded-lg">Retry</button>
        </Card>
      )}
      {!loading && !loadError && (
      <Card dark={dark} className="overflow-hidden">
        <table className="w-full text-sm">
          <thead className={dark ? "bg-slate-800/60" : "bg-gray-50"}>
            <tr className={dark ? "text-gray-400" : "text-gray-500"}>{[t.name, t.email, t.role, t.actions].map((h) => <th key={h} className="text-start px-4 py-3 font-medium">{h}</th>)}</tr>
          </thead>
          <tbody>
            {users.map((u) => {
              const isEditing = editingId === u.id;
              return (
                <tr key={u.id} className={`border-t ${dark ? "border-slate-800" : "border-gray-100"}`}>
                  <td className="px-4 py-3">
                    {isEditing ? <input value={draft.name} onChange={(e) => setDraft({ ...draft, name: e.target.value })} className={inputCls} />
                      : <span className={dark ? "text-gray-200" : "text-gray-800"}>{u.name}</span>}
                  </td>
                  <td className="px-4 py-3">
                    {isEditing ? <input value={draft.email} onChange={(e) => setDraft({ ...draft, email: e.target.value })} className={inputCls} />
                      : <span className={dark ? "text-gray-400" : "text-gray-500"}>{u.email}</span>}
                  </td>
                  <td className="px-4 py-3">
                    {isEditing ? roleSelect(draft.role, (v) => setDraft({ ...draft, role: v }))
                      : <span className={`px-2 py-1 rounded-full text-xs ${dark ? "bg-slate-800 text-emerald-300" : "bg-emerald-50 text-emerald-700"}`}>{t[u.role]}</span>}
                  </td>
                  <td className="px-4 py-3">
                    {isEditing ? (
                      <div className="flex gap-1.5">
                        <button onClick={() => saveEdit(u.id)} className="p-1.5 rounded-lg text-emerald-600 hover:bg-emerald-50"><Icon name="check" size={14} /></button>
                        <button onClick={cancelEdit} className={`p-1.5 rounded-lg ${dark ? "hover:bg-slate-800 text-gray-400" : "hover:bg-gray-100 text-gray-500"}`}><Icon name="x" size={14} /></button>
                      </div>
                    ) : (
                      <div className="flex gap-1.5">
                        <button onClick={() => startEdit(u)} className={`p-1.5 rounded-lg ${dark ? "hover:bg-slate-800 text-gray-400" : "hover:bg-gray-100 text-gray-500"}`}><Icon name="edit" size={14} /></button>
                        <button onClick={() => del(u.id)} className={`p-1.5 rounded-lg ${dark ? "hover:bg-slate-800 text-rose-400" : "hover:bg-gray-100 text-rose-500"}`}><Icon name="trash" size={14} /></button>
                      </div>
                    )}
                  </td>
                </tr>
              );
            })}
            {!users.length && <tr><td colSpan={4} className={`text-center py-8 text-sm ${dark ? "text-gray-500" : "text-gray-400"}`}>—</td></tr>}
          </tbody>
        </table>
      </Card>
      )}
    </div>
  );
}

/* ============== PROFILE ============== */
function ProfilePage({ t, dark, user }) {
  const safeUser = user && typeof user === "object" ? user : {};
  const safeName = typeof safeUser.name === "string" && safeUser.name.length > 0 ? safeUser.name : "?";
  const safeEmail = typeof safeUser.email === "string" ? safeUser.email : "";
  const safeRole = typeof safeUser.role === "string" ? safeUser.role : "";
  const roleLabel = (t && t[safeRole]) ? t[safeRole] : safeRole;
  return (
    <div className="p-4 md:p-6 max-w-md">
      <Card dark={dark} className="p-6 text-center">
        <div className={`w-20 h-20 rounded-full mx-auto flex items-center justify-center text-2xl font-bold mb-3 ${dark ? "bg-emerald-800 text-emerald-100" : "bg-emerald-100 text-emerald-800"}`}>
          {safeName.charAt(0).toUpperCase()}
        </div>
        <input defaultValue={safeName === "?" ? "" : safeName} className={`${PILL} mb-2 text-center font-semibold ${dark ? "bg-slate-800 border-slate-700 text-white" : "border-gray-200"}`} />
        <input defaultValue={safeEmail} className={`${PILL} mb-2 text-center ${dark ? "bg-slate-800 border-slate-700 text-white" : "border-gray-200"}`} />
        <div className={`text-xs mb-4 ${dark ? "text-gray-400" : "text-gray-500"}`}>{t.role}: {roleLabel}</div>
        <button className="w-full bg-emerald-700 text-white rounded-xl py-2.5 font-medium">{t.save}</button>
      </Card>
    </div>
  );
}

/* ============== SETTINGS ============== */
function SettingsPage({ t, dark, setDark, lang, setLang, online }) {
  return (
    <div className="p-4 md:p-6 max-w-md">
      <BackendBanner t={t} online={online} />
      <Card dark={dark} className="p-5">
        <div className="flex items-center justify-between py-2.5">
          <span className={`text-sm ${dark ? "text-gray-300" : "text-gray-700"}`}>{t.theme}</span>
          <div className="flex gap-2">
            <button onClick={() => setDark(false)} className={`px-3 py-1.5 rounded-lg text-xs ${!dark ? "bg-emerald-700 text-white" : "bg-gray-100 text-gray-600"}`}>{t.light}</button>
            <button onClick={() => setDark(true)} className={`px-3 py-1.5 rounded-lg text-xs ${dark ? "bg-emerald-700 text-white" : "bg-gray-100 text-gray-600"}`}>{t.dark}</button>
          </div>
        </div>
        <div className="flex items-center justify-between py-2.5">
          <span className={`text-sm ${dark ? "text-gray-300" : "text-gray-700"}`}>{t.language}</span>
          <div className="flex gap-2">
            <button onClick={() => setLang("ar")} className={`px-3 py-1.5 rounded-lg text-xs ${lang === "ar" ? "bg-emerald-700 text-white" : "bg-gray-100 text-gray-600"}`}>عربي</button>
            <button onClick={() => setLang("en")} className={`px-3 py-1.5 rounded-lg text-xs ${lang === "en" ? "bg-emerald-700 text-white" : "bg-gray-100 text-gray-600"}`}>English</button>
          </div>
        </div>
      </Card>
    </div>
  );
}

/* ============== ERROR BOUNDARY (shows real errors instead of a blank page) ============== */
class ErrorBoundary extends React.Component {
  constructor(props) { super(props); this.state = { error: null }; }
  static getDerivedStateFromError(error) { return { error }; }
  componentDidCatch(error, info) { console.error("Page crashed:", error, info); }
  render() {
    if (this.state.error) {
      return (
        <div className="p-6" style={{ maxWidth: "100%", overflowX: "hidden" }}>
          <div className="rounded-2xl border border-rose-200 bg-rose-50 p-5 text-rose-700">
            <div className="font-bold mb-1">This page hit an error</div>
            <pre className="text-xs whitespace-pre-wrap" style={{ overflowWrap: "break-word", wordBreak: "break-word", maxWidth: "100%" }}>{String(this.state.error && this.state.error.message || this.state.error)}</pre>
            <button onClick={() => this.setState({ error: null })} className="mt-3 text-xs bg-rose-600 text-white px-3 py-1.5 rounded-lg">
              Try again
            </button>
          </div>
        </div>
      );
    }
    return this.props.children;
  }
}

/* ============== APP ROOT ============== */
function App() {
  const [user, setUser] = useState(null);
  const [lang, setLang] = useState("ar");
  const [dark, setDark] = useState(false);
  const [page, setPage] = useState("dashboard");
  const [open, setOpen] = useState(false);
  const [online, setOnline] = useState(false);
  const [refreshKey, setRefreshKey] = useState(0);
  const t = T[lang];

  useEffect(() => { document.documentElement.dir = lang === "ar" ? "rtl" : "ltr"; document.body.style.fontFamily = lang === "ar" ? "'Tajawal',sans-serif" : "'Inter',sans-serif"; }, [lang]);
  useEffect(() => {
    const check = () => apiFetch(`${API}/health`).then((r) => r.ok && setOnline(true)).catch(() => setOnline(false));
    check();
    const iv = setInterval(check, 20000);
    return () => clearInterval(iv);
  }, []);

  if (!user) return <Login t={t} lang={lang} setLang={setLang} dark={dark} setDark={setDark} onLogin={setUser} />;

  const pages = {
    dashboard: <Dashboard t={t} dark={dark} online={online} lang={lang} key={refreshKey} />,
    analyzeComment: <AnalyzeComment t={t} dark={dark} online={online} onAnalyzed={() => setRefreshKey((k) => k + 1)} />,
    comments: <CommentsPage t={t} dark={dark} online={online} refreshKey={refreshKey} />,
    analytics: <AnalyticsPage t={t} dark={dark} online={online} />,
    reports: <ReportsPage t={t} dark={dark} online={online} />,
    users: <UsersPage t={t} dark={dark} online={online} />,
    profile: <ProfilePage t={t} dark={dark} user={user} />,
    settings: <SettingsPage t={t} dark={dark} setDark={setDark} lang={lang} setLang={setLang} online={online} />,
  };

  return (
    <div className={`min-h-screen flex ${dark ? "bg-slate-950" : "bg-gray-50"}`}>
      <Sidebar t={t} page={page} setPage={setPage} dark={dark} lang={lang} open={open} setOpen={setOpen} onLogout={() => setUser(null)} />
      {open && <div className="fixed inset-0 bg-black/40 z-30 md:hidden" onClick={() => setOpen(false)} />}
      <div className="flex-1 min-w-0">
        <Topbar t={t} lang={lang} setLang={setLang} dark={dark} setDark={setDark} title={t[page]} setOpen={setOpen} user={user} />
        <ErrorBoundary key={page}>{pages[page]}</ErrorBoundary>
      </div>
    </div>
  );
}

ReactDOM.createRoot(document.getElementById("root")).render(
  <ErrorBoundary><App /></ErrorBoundary>
);
window.__appMounted = true;
</script>
</body>
</html>
