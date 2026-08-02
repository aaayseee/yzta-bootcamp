def get_custom_css():
    return """
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200;400;500;600;700;800;900&display=swap');
@import url('https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css');

/* Sayfa Arkaplanı ve Yazı Tipleri */
html, body, [data-testid="stAppViewContainer"], .stWidgetLabel {
    font-family: 'Outfit', sans-serif !important;
}

[data-testid="stAppViewContainer"] {
    background: transparent !important;
}

/* Sol Sidebar Tasarımı (Floating Glass Island) */
[data-testid="stSidebar"] {
    background-color: transparent !important;
    border-right: none !important;
}

[data-testid="stSidebarUserContent"] {
    background-color: rgba(10, 15, 28, 0.6) !important;
    backdrop-filter: blur(20px) !important;
    -webkit-backdrop-filter: blur(20px) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-radius: 20px !important;
    margin: 15px !important;
    height: calc(100vh - 30px) !important;
    padding: 24px 20px !important;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5) !important;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
}

[data-testid="stSidebarUserContent"]:hover {
    border-color: rgba(14, 165, 233, 0.25) !important;
    box-shadow: 0 20px 45px rgba(14, 165, 233, 0.12) !important;
}

/* Sidebar Radio Button custom navigation pills */
div[data-testid="stRadio"] label {
    font-weight: 600 !important;
    font-size: 14px !important;
    color: #94a3b8 !important;
    margin-bottom: 10px !important;
}

/* Style active/inactive navigation pills */
div[data-testid="stRadio"] div[role="radiogroup"] > div {
    background-color: rgba(255, 255, 255, 0.01) !important;
    border: 1px solid rgba(255, 255, 255, 0.02) !important;
    border-radius: 10px !important;
    padding: 10px 14px !important;
    margin-bottom: 8px !important;
    transition: all 0.25s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
    cursor: pointer !important;
}

div[data-testid="stRadio"] div[role="radiogroup"] > div:hover {
    background-color: rgba(14, 165, 233, 0.06) !important;
    border-color: rgba(14, 165, 233, 0.2) !important;
    transform: translateX(5px) !important;
}

/* Style selected active radio pill */
div[data-testid="stRadio"] div[role="radiogroup"] div[data-checked="true"] {
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.15) 0%, rgba(14, 165, 233, 0.15) 100%) !important;
    border-color: rgba(16, 185, 129, 0.4) !important;
    box-shadow: 0 0 12px rgba(16, 185, 129, 0.12) !important;
}

/* Hide Streamlit default radio check circles inside sidebar group */
div[data-testid="stRadio"] div[role="radiogroup"] label div[dir="ltr"] {
    display: none !important;
}

/* Hareketli Balon (Panning Gradient Blobs) Efekti */
@keyframes float-blob-1 {
    0% { transform: translate(0px, 0px) scale(1); }
    33% { transform: translate(80px, -100px) scale(1.25); }
    66% { transform: translate(-60px, 50px) scale(0.85); }
    100% { transform: translate(0px, 0px) scale(1); }
}
@keyframes float-blob-2 {
    0% { transform: translate(0px, 0px) scale(1); }
    50% { transform: translate(-100px, 100px) scale(1.15); }
    100% { transform: translate(0px, 0px) scale(1); }
}

.bg-blob {
    position: fixed;
    border-radius: 50%;
    filter: blur(90px);
    z-index: -1;
    pointer-events: none;
    opacity: 0.5;
}
.bg-blob-1 {
    top: 10%;
    left: 15%;
    width: 320px;
    height: 320px;
    background: radial-gradient(circle, rgba(16, 185, 129, 0.25) 0%, rgba(0,0,0,0) 70%);
    animation: float-blob-1 22s infinite ease-in-out;
}
.bg-blob-2 {
    bottom: 12%;
    right: 18%;
    width: 420px;
    height: 420px;
    background: radial-gradient(circle, rgba(14, 165, 233, 0.25) 0%, rgba(0,0,0,0) 70%);
    animation: float-blob-2 28s infinite ease-in-out;
}

/* Dinamik Renk Geçişli Yazı Efekti */
.animated-gradient-text {
    background: linear-gradient(-45deg, #10b981, #0ea5e9, #6366f1, #10b981);
    background-size: 300% 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: text-gradient 7s ease infinite;
}
@keyframes text-gradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Balon Gibi Yüzme & Sallanma Animasyonları */
@keyframes sway-slow {
    0% { transform: translateY(0px) translateX(0px) rotate(0deg); }
    50% { transform: translateY(-8px) translateX(4px) rotate(0.4deg); }
    100% { transform: translateY(0px) translateX(0px) rotate(0deg); }
}

@keyframes sway-medium {
    0% { transform: translateY(0px) translateX(0px) rotate(0deg); }
    50% { transform: translateY(-10px) translateX(-4px) rotate(-0.3deg); }
    100% { transform: translateY(0px) translateX(0px) rotate(0deg); }
}

@keyframes sway-fast {
    0% { transform: translateY(0px) translateX(0px) rotate(0deg); }
    50% { transform: translateY(-7px) translateX(3px) rotate(0.2deg); }
    100% { transform: translateY(0px) translateX(0px) rotate(0deg); }
}

/* Premium Kart Tasarımı (Custom Card) */
.custom-card {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    backdrop-filter: none !important;
    -webkit-backdrop-filter: none !important;
    padding: 10px 0 !important;
    margin-bottom: 20px;
    animation: sway-slow 12s infinite ease-in-out !important;
}

/* Giriş Kartı Özel Tasarımı (Modern Glassmorphism) */
.login-card {
    background: rgba(255, 255, 255, 0.05) !important;
    backdrop-filter: blur(15px) !important;
    -webkit-backdrop-filter: blur(15px) !important;
    border: 2px solid rgba(255, 255, 255, 0.2) !important;
    border-radius: 16px !important;
    padding: 30px 40px !important;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2) !important;
    color: #fff !important;
}

.login-card, .login-card h1, .login-card h3, .login-card input, .login-card button, .login-card label, .login-card a, .login-card p {
    font-family: 'Poppins', sans-serif !important;
}

/* Streamlit Inputs Glassmorphism Override */
.login-card div[data-testid="stTextInput"] input {
    background: transparent !important;
    border: 2px solid rgba(255, 255, 255, 0.2) !important;
    border-radius: 40px !important;
    font-size: 16px !important;
    color: #fff !important;
    padding: 10px 45px 10px 20px !important; /* 45px on right for icon */
    height: 50px !important;
    outline: none !important;
    box-sizing: border-box !important;
    transition: all 0.3s ease !important;
}

.login-card div[data-testid="stTextInput"] input::placeholder {
    color: rgba(255, 255, 255, 0.7) !important;
}

.login-card div[data-testid="stTextInput"] input:focus {
    border-color: #fff !important;
    box-shadow: 0 0 10px rgba(255, 255, 255, 0.25) !important;
}

/* Pseudo-elements for Boxicons absolute positioning inside input wrapper */
.login-card div[data-testid="stTextInput"] > div {
    position: relative !important;
}

/* User icon for Username */
.login-card div[data-testid="stTextInput"]:first-of-type > div::after {
    content: "\\eec4" !important; /* Boxicon bxs-user */
    font-family: 'boxicons' !important;
    position: absolute !important;
    right: 20px !important;
    top: 50% !important;
    transform: translateY(-50%) !important;
    font-size: 20px !important;
    color: rgba(255, 255, 255, 0.75) !important;
    pointer-events: none !important;
    z-index: 5 !important;
}

/* Lock icon for Password */
.login-card div[data-testid="stTextInput"]:nth-of-type(2) > div::after {
    content: "\\eea7" !important; /* Boxicon bxs-lock-alt */
    font-family: 'boxicons' !important;
    position: absolute !important;
    right: 20px !important;
    top: 50% !important;
    transform: translateY(-50%) !important;
    font-size: 20px !important;
    color: rgba(255, 255, 255, 0.75) !important;
    pointer-events: none !important;
    z-index: 5 !important;
}

/* Streamlit Button override for modern white pill button */
.login-card div.stButton button {
    width: 100% !important;
    height: 45px !important;
    background: #fff !important;
    border: none !important;
    outline: none !important;
    border-radius: 40px !important;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1) !important;
    cursor: pointer !important;
    font-size: 16px !important;
    color: #333 !important;
    font-weight: 600 !important;
    transition: all 0.3s ease !important;
    margin-top: 10px !important;
}

.login-card div.stButton button:hover {
    background: rgba(255, 255, 255, 0.9) !important;
    box-shadow: 0 0 15px rgba(255, 255, 255, 0.4) !important;
    transform: translateY(-1px) !important;
}

.login-card div.stButton button:active {
    transform: translateY(1px) !important;
}

/* Remember Forgot & Register styles */
.remember-forgot {
    display: flex;
    justify-content: space-between;
    font-size: 14px;
    margin: 15px 0;
    color: #fff;
    font-family: sans-serif;
}
.remember-forgot label {
    display: flex;
    align-items: center;
    gap: 5px;
    cursor: pointer;
}
.remember-forgot input[type="checkbox"] {
    accent-color: #fff;
    cursor: pointer;
}
.remember-forgot a {
    color: #fff;
    text-decoration: none;
    font-weight: 500;
}
.remember-forgot a:hover {
    text-decoration: underline;
}

.register-link {
    font-size: 14px;
    text-align: center;
    margin: 20px 0 10px;
    color: #fff;
}
.register-link p a {
    color: #fff;
    text-decoration: none;
    font-weight: 600;
}
.register-link p a:hover {
    text-decoration: underline;
}

/* Metrik Kartı Tasarımları (Vibrant Border & Glow) */
.kpi-container {
    display: flex;
    gap: 20px;
    margin-bottom: 25px;
}
.kpi-card {
    flex: 1;
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
    transition: all 0.3s ease;
    animation: sway-fast 7s infinite ease-in-out !important;
}
.kpi-card:nth-child(even) {
    animation: sway-medium 9s infinite ease-in-out !important;
}

.kpi-card.blue {
    background-color: rgba(10, 14, 23, 0.5) !important;
    backdrop-filter: blur(10px) !important;
    border: 1px solid rgba(14, 165, 233, 0.25) !important;
}
.kpi-card.blue:hover {
    background-color: rgba(14, 165, 233, 0.08) !important;
    border: 1px solid rgba(14, 165, 233, 0.5) !important;
    box-shadow: 0 8px 24px rgba(14, 165, 233, 0.15) !important;
}
.kpi-card.blue .kpi-value {
    color: #0ea5e9 !important;
}

.kpi-card.red {
    background-color: rgba(10, 14, 23, 0.5) !important;
    backdrop-filter: blur(10px) !important;
    border: 1px solid rgba(239, 68, 68, 0.25) !important;
}
.kpi-card.red:hover {
    background-color: rgba(239, 68, 68, 0.08) !important;
    border: 1px solid rgba(239, 68, 68, 0.5) !important;
    box-shadow: 0 8px 24px rgba(239, 68, 68, 0.15) !important;
}
.kpi-card.red .kpi-value {
    color: #ef4444 !important;
}

.kpi-card.orange {
    background-color: rgba(10, 14, 23, 0.5) !important;
    backdrop-filter: blur(10px) !important;
    border: 1px solid rgba(245, 158, 11, 0.25) !important;
}
.kpi-card.orange:hover {
    background-color: rgba(245, 158, 11, 0.08) !important;
    border: 1px solid rgba(245, 158, 11, 0.5) !important;
    box-shadow: 0 8px 24px rgba(245, 158, 11, 0.15) !important;
}
.kpi-card.orange .kpi-value {
    color: #f59e0b !important;
}

.kpi-card.green {
    background-color: rgba(10, 14, 23, 0.5) !important;
    backdrop-filter: blur(10px) !important;
    border: 1px solid rgba(16, 185, 129, 0.25) !important;
}
.kpi-card.green:hover {
    background-color: rgba(16, 185, 129, 0.08) !important;
    border: 1px solid rgba(16, 185, 129, 0.5) !important;
    box-shadow: 0 8px 24px rgba(16, 185, 129, 0.15) !important;
}
.kpi-card.green .kpi-value {
    color: #10b981 !important;
}

.kpi-card.purple {
    background-color: rgba(10, 14, 23, 0.5) !important;
    backdrop-filter: blur(10px) !important;
    border: 1px solid rgba(139, 92, 246, 0.25) !important;
}
.kpi-card.purple:hover {
    background-color: rgba(139, 92, 246, 0.08) !important;
    border: 1px solid rgba(139, 92, 246, 0.5) !important;
    box-shadow: 0 8px 24px rgba(139, 92, 246, 0.15) !important;
}
.kpi-card.purple .kpi-value {
    color: #8b5cf6 !important;
}
.kpi-title {
    color: #94a3b8;
    font-size: 14px;
    font-weight: 500;
    margin-bottom: 5px;
}
.kpi-value {
    color: #f8fafc;
    font-size: 28px;
    font-weight: 700;
}

/* Tablolar ve Veri Çerçeveleri */
[data-testid="stDataFrame"] {
    animation: sway-medium 10s infinite ease-in-out !important;
    background: #111827 !important;
    border: 1px solid rgba(255, 255, 255, 0.05) !important;
    border-radius: 12px !important;
    padding: 10px !important;
    box-shadow: 0 10px 25px rgba(0,0,0,0.4) !important;
    transition: box-shadow 0.3s ease !important;
}
[data-testid="stDataFrame"]:hover {
    box-shadow: 0 14px 32px rgba(14, 165, 233, 0.18) !important;
}

/* Sonuç Panelleri */
.result-card {
    border-radius: 12px;
    padding: 24px;
    margin-top: 20px;
    color: #f8fafc;
    box-shadow: 0 10px 25px rgba(0,0,0,0.4);
    animation: sway-slow 7s infinite ease-in-out !important;
}
.result-card.risk {
    background: linear-gradient(135deg, rgba(244, 63, 94, 0.15) 0%, rgba(159, 18, 57, 0.3) 100%);
    border: 1px solid rgba(244, 63, 94, 0.4);
}
.result-card.loyal {
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.15) 0%, rgba(6, 78, 59, 0.3) 100%);
    border: 1px solid rgba(16, 185, 129, 0.4);
}

/* ====================================================
   AÇIK MOD (LIGHT THEME) OVERRIDES & FIXES
   ==================================================== */
.light-theme {
    color: #0f172a !important;
}

.light-theme .kpi-title {
    color: #475569 !important;
}
.light-theme .kpi-value {
    color: #0f172a !important;
}

.light-theme .kpi-card {
    background-color: rgba(255, 255, 255, 0.45) !important;
    backdrop-filter: blur(8px) !important;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.04) !important;
}

.light-theme .kpi-card.blue {
    border: 1px solid rgba(14, 165, 233, 0.4) !important;
}
.light-theme .kpi-card.blue .kpi-value {
    color: #0369a1 !important;
}

.light-theme .kpi-card.red {
    border: 1px solid rgba(239, 68, 68, 0.4) !important;
}
.light-theme .kpi-card.red .kpi-value {
    color: #b91c1c !important;
}

.light-theme .kpi-card.orange {
    border: 1px solid rgba(245, 158, 11, 0.4) !important;
}
.light-theme .kpi-card.orange .kpi-value {
    color: #c2410c !important;
}

.light-theme .kpi-card.green {
    border: 1px solid rgba(16, 185, 129, 0.4) !important;
}
.light-theme .kpi-card.green .kpi-value {
    color: #047857 !important;
}

.light-theme .kpi-card.purple {
    border: 1px solid rgba(139, 92, 246, 0.4) !important;
}
.light-theme .kpi-card.purple .kpi-value {
    color: #6d28d9 !important;
}

/* Light mode login overrides */
.light-theme .login-card {
    background: rgba(255, 255, 255, 0.5) !important;
    border: 2px solid rgba(15, 23, 42, 0.15) !important;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05) !important;
    color: #0f172a !important;
}
.light-theme .login-card h3 {
    color: #0f172a !important;
}
.light-theme .login-card div[data-testid="stTextInput"] input {
    border-color: rgba(15, 23, 42, 0.15) !important;
    color: #0f172a !important;
}
.light-theme .login-card div[data-testid="stTextInput"] input::placeholder {
    color: #475569 !important;
}
.light-theme .login-card div[data-testid="stTextInput"] input:focus {
    border-color: #0f172a !important;
    box-shadow: 0 0 10px rgba(15, 23, 42, 0.1) !important;
}
.light-theme .login-card div.stButton button {
    background: #0f172a !important;
    color: #ffffff !important;
}
.light-theme .login-card div.stButton button:hover {
    background: #1e293b !important;
    box-shadow: 0 0 12px rgba(15, 23, 42, 0.2) !important;
}
.light-theme .remember-forgot,
.light-theme .remember-forgot a,
.light-theme .register-link,
.light-theme .register-link p a {
    color: #334155 !important;
}
.light-theme .remember-forgot input[type="checkbox"] {
    accent-color: #0f172a !important;
}

/* Light mode support ticket & results card text fix */
.light-theme .result-card {
    color: #1e293b !important;
    box-shadow: 0 10px 25px rgba(0,0,0,0.05) !important;
}
.light-theme .result-card.risk {
    background: linear-gradient(135deg, rgba(244, 63, 94, 0.08) 0%, rgba(244, 63, 94, 0.15) 100%) !important;
    border: 1px solid rgba(244, 63, 94, 0.3) !important;
}
.light-theme .result-card.loyal {
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.08) 0%, rgba(16, 185, 129, 0.15) 100%) !important;
    border: 1px solid rgba(16, 185, 129, 0.3) !important;
}

/* Light mode text gradient adjustment for better contrast */
.light-theme .animated-gradient-text {
    background: linear-gradient(-45deg, #047857, #0284c7, #5b21b6, #047857) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
}

/* Dynamic text colors inside general custom-markdown blocks */
.light-theme p, .light-theme span, .light-theme li {
    color: #334155 !important;
}
.light-theme strong {
    color: #0f172a !important;
}

/* Light mode sidebar overrides (Floating Island) */
.light-theme [data-testid="stSidebar"] {
    background-color: transparent !important;
    border-right: none !important;
}

.light-theme [data-testid="stSidebarUserContent"] {
    background-color: rgba(255, 255, 255, 0.55) !important;
    border: 1px solid rgba(0, 0, 0, 0.08) !important;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05) !important;
}

.light-theme div[data-testid="stRadio"] label {
    color: #475569 !important;
}

.light-theme div[data-testid="stRadio"] div[role="radiogroup"] > div {
    background-color: rgba(0, 0, 0, 0.02) !important;
    border: 1px solid rgba(0, 0, 0, 0.03) !important;
}

.light-theme div[data-testid="stRadio"] div[role="radiogroup"] > div:hover {
    background-color: rgba(3, 105, 161, 0.06) !important;
    border-color: rgba(3, 105, 161, 0.15) !important;
}

.light-theme div[data-testid="stRadio"] div[role="radiogroup"] div[data-checked="true"] {
    background: linear-gradient(135deg, rgba(4, 120, 87, 0.1) 0%, rgba(3, 105, 161, 0.1) 100%) !important;
    border-color: rgba(4, 120, 87, 0.3) !important;
    box-shadow: 0 0 12px rgba(4, 120, 87, 0.05) !important;
}

.light-theme div[data-testid="stRadio"] div[role="radiogroup"] label p {
    color: #1e293b !important;
}

/* ----------------------------------------------------------------
   AÇIK MOD HATA DÜZELTMELERİ (kritik: sayfa başlıkları/tablolar
   koyu moda göre kodlanmış inline renklerle görünmez oluyordu)
   ---------------------------------------------------------------- */

/* h1-h6 başlıkları için kapsamlı okunabilirlik düzeltmesi.
   (dashboard.py, complaints.py, simulation.py vb. sayfalardaki
   `style="color:#f8fafc"` gibi koyu-mod-özel satır içi renkler
   açık modda krem arkaplan üzerinde neredeyse görünmez kalıyordu) */
.light-theme h1:not(.animated-gradient-text),
.light-theme h2:not(.animated-gradient-text),
.light-theme h3:not(.animated-gradient-text),
.light-theme h4,
.light-theme h5,
.light-theme h6,
.light-theme label,
.light-theme [data-testid="stMarkdownContainer"] {
    color: #0f172a !important;
}

/* Sidebar logo ve alt bilgi yazısı (LoyalCart) satır içi #f8fafc
   rengiyle sabitlenmişti; açık modda cam sidebar üzerinde kayboluyordu */
.light-theme [data-testid="stSidebarUserContent"] span,
.light-theme [data-testid="stSidebarUserContent"] div {
    color: #0f172a !important;
}
.light-theme [data-testid="stSidebarUserContent"] div[style*="color: #64748b"] {
    color: #64748b !important;
}

/* Veri tabloları / DataFrame'ler koyu arkaplanla sabitlenmişti,
   açık modda temayla uyumlu, okunaklı bir görünüme çevrildi */
.light-theme [data-testid="stDataFrame"] {
    background: rgba(255, 255, 255, 0.65) !important;
    border: 1px solid rgba(15, 23, 42, 0.08) !important;
    box-shadow: 0 10px 25px rgba(0,0,0,0.06) !important;
}
.light-theme [data-testid="stDataFrame"]:hover {
    box-shadow: 0 14px 30px rgba(3, 105, 161, 0.12) !important;
}

/* Streamlit metrik / expander / tab bileşenleri için genel kontrast */
.light-theme [data-testid="stMetric"],
.light-theme [data-testid="stExpander"] {
    color: #0f172a !important;
}
.light-theme [data-testid="stMetricLabel"] {
    color: #475569 !important;
}
.light-theme hr {
    border-color: rgba(15, 23, 42, 0.12) !important;
}

/* Butonlar için açık mod kontrastı (giriş ekranı dışındaki genel butonlar) */
.light-theme div.stButton button:not(.login-card div.stButton button) {
    color: #0f172a !important;
    border-color: rgba(15, 23, 42, 0.15) !important;
}

/* ----------------------------------------------------------------
   GİRİŞ SONRASI ANİMASYONLAR (sayfa açılışı & etkileşim)
   ---------------------------------------------------------------- */
@keyframes fade-in-up {
    0% { opacity: 0; transform: translateY(18px); }
    100% { opacity: 1; transform: translateY(0); }
}

section.main .block-container {
    animation: fade-in-up 0.6s cubic-bezier(0.22, 1, 0.36, 1) both !important;
}

/* Sekme/expander geçişlerine yumuşaklık */
[data-testid="stExpander"], [data-baseweb="tab-panel"] {
    transition: all 0.3s ease !important;
}

/* Plotly grafik kartlarına hafif giriş animasyonu ve hover parlaması */
[data-testid="stPlotlyChart"] {
    animation: fade-in-up 0.7s cubic-bezier(0.22, 1, 0.36, 1) both !important;
    border-radius: 14px !important;
    transition: box-shadow 0.3s ease, transform 0.3s ease !important;
}
[data-testid="stPlotlyChart"]:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 16px 32px rgba(99, 102, 241, 0.15) !important;
}

/* ====================================================
   NEON SPIDER WEB & DROP-DOWN SWAY ANIMATIONS
   ==================================================== */
.web-thread {
    position: absolute;
    top: -50px;
    left: 50%;
    width: 1.5px;
    height: 230px;
    background: linear-gradient(to bottom, rgba(16, 185, 129, 0.85), rgba(14, 165, 233, 0.05));
    box-shadow: 0 0 8px rgba(16, 185, 129, 0.5);
    transform-origin: top center;
    z-index: 2;
    animation: thread-drop 1.8s cubic-bezier(0.25, 1, 0.5, 1) forwards, thread-sway 5s infinite ease-in-out 1.8s;
}

/* Sibling animation mapping from the DOM marker */
.login-card-wrapper ~ div.element-container,
.login-card-wrapper ~ div[data-testid="stHorizontalBlock"] {
    transform-origin: top center !important;
    animation: card-spider-drop 1.8s cubic-bezier(0.175, 0.885, 0.32, 1.12) forwards, card-spider-sway 5s infinite ease-in-out 1.8s !important;
}

@keyframes thread-drop {
    0% { transform: scaleY(0); }
    100% { transform: scaleY(1); }
}

@keyframes card-spider-drop {
    0% { transform: translateY(-400px) scale(0.85); opacity: 0; }
    50% { opacity: 0.3; }
    100% { transform: translateY(0px) scale(1); opacity: 1; }
}

@keyframes thread-sway {
    0%, 100% { transform: scaleY(1) rotate(0deg); }
    25% { transform: scaleY(1) rotate(-1deg); }
    75% { transform: scaleY(1) rotate(1deg); }
}

@keyframes card-spider-sway {
    0%, 100% { transform: rotate(0deg) translateZ(0px); }
    25% { transform: rotate(-1deg) translateZ(8px); }
    75% { transform: rotate(1deg) translateZ(8px); }
}

/* Light mode overrides for the spider web thread */
.light-theme .web-thread {
    background: linear-gradient(to bottom, rgba(15, 118, 110, 0.6), rgba(3, 105, 161, 0.05)) !important;
    box-shadow: none !important;
}

/* Top Navigation Bar Styling */
.top-nav-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: rgba(10, 15, 28, 0.5) !important;
    backdrop-filter: blur(20px) !important;
    -webkit-backdrop-filter: blur(20px) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-bottom: 1.5px solid rgba(14, 165, 233, 0.25) !important;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.37) !important;
    padding: 10px 24px !important;
    border-radius: 16px !important;
    margin-bottom: 24px !important;
    width: 100% !important;
    z-index: 999;
}

.top-nav-left {
    display: flex;
    align-items: center;
    gap: 12px;
}

.top-nav-logo {
    font-weight: 800;
    font-size: 22px;
    color: #ffffff;
    font-family: 'Poppins', sans-serif;
    letter-spacing: -0.5px;
    display: flex;
    align-items: center;
    gap: 6px;
}

.logo-emoji-circle-sm {
    background: linear-gradient(135deg, #10b981 0%, #0ea5e9 100%);
    width: 28px;
    height: 28px;
    border-radius: 50%;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
    box-shadow: 0 0 8px rgba(16, 185, 129, 0.25);
}

.top-nav-divider {
    color: rgba(255, 255, 255, 0.25);
    font-weight: 300;
    font-size: 18px;
}

.top-nav-title {
    color: rgba(255, 255, 255, 0.85);
    font-size: 15px;
    font-weight: 500;
    font-family: 'Outfit', sans-serif;
}

.top-nav-right {
    display: flex;
    align-items: center;
}

.user-profile {
    display: flex;
    align-items: center;
    gap: 8px;
    background: rgba(255, 255, 255, 0.05);
    padding: 6px 12px;
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.1);
}

.user-avatar {
    font-size: 14px;
}

.user-name {
    color: #ffffff;
    font-size: 13px;
    font-weight: 600;
}

.status-indicator {
    width: 8px;
    height: 8px;
    background-color: #10b981;
    border-radius: 50%;
    display: inline-block;
    box-shadow: 0 0 8px #10b981;
}

/* Light Theme Overrides for Top Nav Bar */
body.light-theme .top-nav-bar {
    background: rgba(255, 255, 255, 0.8) !important;
    border: 1px solid rgba(10, 15, 29, 0.08) !important;
    border-bottom: 1.5px solid rgba(14, 165, 233, 0.15) !important;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.05) !important;
}

body.light-theme .top-nav-logo {
    color: #0c1524 !important;
}

body.light-theme .top-nav-divider {
    color: rgba(0, 0, 0, 0.15) !important;
}

body.light-theme .top-nav-title {
    color: #475569 !important;
}

body.light-theme .user-profile {
    background: rgba(0, 0, 0, 0.03) !important;
    border: 1px solid rgba(0, 0, 0, 0.08) !important;
}

body.light-theme .user-name {
    color: #0c1524 !important;
}
</style>
"""

def get_3d_javascript():
    return """
<div class="bg-blob bg-blob-1"></div>
<div class="bg-blob bg-blob-2"></div>

<script>
const injectInteractiveEffects = () => {
    const parentDoc = window.parent.document;
    
    // Clean up login animation canvas if present
    const oldCanvasParent = parentDoc.getElementById('login-animation-canvas');
    if (oldCanvasParent) {
        oldCanvasParent.remove();
    }
    const oldCanvasLocal = document.getElementById('login-animation-canvas');
    if (oldCanvasLocal) {
        oldCanvasLocal.remove();
    }
    
    // Background canvas control
    if (!parentDoc.getElementById('cyber-interactive-bg')) {
        const canvas = parentDoc.createElement('canvas');
        canvas.id = 'cyber-interactive-bg';
        canvas.style.position = 'fixed';
        canvas.style.top = '0';
        canvas.style.left = '0';
        canvas.style.width = '100vw';
        canvas.style.height = '100vh';
        canvas.style.zIndex = '-2';
        canvas.style.pointerEvents = 'none';
        canvas.style.background = '#03050a'; // Ultra dark black mode
        parentDoc.body.appendChild(canvas);
        
        const ctx = canvas.getContext('2d');
        let width = canvas.width = parentDoc.documentElement.clientWidth;
        let height = canvas.height = parentDoc.documentElement.clientHeight;
        
        window.parent.addEventListener('resize', () => {
            width = canvas.width = parentDoc.documentElement.clientWidth;
            height = canvas.height = parentDoc.documentElement.clientHeight;
        });
        
        let mouse = { x: width / 2, y: height / 2, tx: width / 2, ty: height / 2 };
        parentDoc.addEventListener('mousemove', (e) => {
            mouse.tx = e.clientX;
            mouse.ty = e.clientY;
        });

        // "Deniz Efekti" - mavi / mor / yeşil dalgalı okyanus katmanları
        const bubbles = [];
        const numBubbles = 40;
        for (let i = 0; i < numBubbles; i++) {
            bubbles.push({
                x: Math.random() * width,
                y: Math.random() * height,
                r: Math.random() * 3 + 1.2,
                speed: Math.random() * 0.6 + 0.2,
                drift: (Math.random() - 0.5) * 0.4,
                alpha: Math.random() * 0.4 + 0.15
            });
        }

        const waveBands = [
            { yRatio: 0.62, amp: 55, freq: 0.0032, speed: 0.55, hueDark: '16, 185, 129', hueLight: '5, 150, 105' },   // yeşil
            { yRatio: 0.72, amp: 75, freq: 0.0022, speed: -0.42, hueDark: '14, 165, 233', hueLight: '2, 132, 199' },  // mavi
            { yRatio: 0.82, amp: 45, freq: 0.0045, speed: 0.7, hueDark: '168, 85, 247', hueLight: '147, 51, 234' }    // mor
        ];

        const animate = () => {
            // Check light mode dynamically from parent document text color
            const mainEl = parentDoc.querySelector('section.main') || parentDoc.body;
            const textColor = window.parent.getComputedStyle(mainEl).getPropertyValue('--text-color').trim();
            const isLight = textColor.includes('49') || textColor.includes('51') || textColor.includes('31333F') || textColor.includes('rgb(49') || textColor.includes('rgb(51');
            
            // Toggle light-theme class on iframe body
            if (isLight) {
                document.body.classList.add('light-theme');
                document.body.classList.remove('dark-theme');
                canvas.style.background = '#f1f7fb';
                ctx.fillStyle = 'rgba(241, 247, 251, 0.22)';
            } else {
                document.body.classList.add('dark-theme');
                document.body.classList.remove('light-theme');
                canvas.style.background = '#040912';
                ctx.fillStyle = 'rgba(4, 9, 18, 0.22)';
            }
            
            mouse.x += (mouse.tx - mouse.x) * 0.08;
            mouse.y += (mouse.ty - mouse.y) * 0.08;
            
            ctx.fillRect(0, 0, width, height);

            const time = Date.now() * 0.001;

            // Dalgalı deniz katmanlarını çiz (yeşil > mavi > mor)
            waveBands.forEach((b) => {
                const yCenter = height * b.yRatio;
                const hue = isLight ? b.hueLight : b.hueDark;
                ctx.beginPath();
                ctx.moveTo(0, height);
                for (let x = 0; x <= width; x += 12) {
                    // fareye yakın bölgede hafif dalga yükselmesi (etkileşim)
                    const distMouse = Math.abs(x - mouse.x);
                    const mouseLift = Math.max(0, 1 - distMouse / 260) * 18;
                    const y = yCenter + Math.sin(x * b.freq + time * b.speed) * b.amp - mouseLift;
                    ctx.lineTo(x, y);
                }
                ctx.lineTo(width, height);
                ctx.closePath();

                const grad = ctx.createLinearGradient(0, yCenter - b.amp, 0, height);
                grad.addColorStop(0, `rgba(${hue}, ${isLight ? 0.16 : 0.16})`);
                grad.addColorStop(1, `rgba(${hue}, ${isLight ? 0.02 : 0.01})`);
                ctx.fillStyle = grad;
                ctx.fill();
            });

            // Yükselen deniz kabarcıkları (bubbles)
            bubbles.forEach(bub => {
                bub.y -= bub.speed;
                bub.x += bub.drift;
                if (bub.y < 0) {
                    bub.y = height + 10;
                    bub.x = Math.random() * width;
                }
                if (bub.x < 0) bub.x = width;
                if (bub.x > width) bub.x = 0;

                ctx.beginPath();
                ctx.arc(bub.x, bub.y, bub.r, 0, Math.PI * 2);
                ctx.fillStyle = isLight
                    ? `rgba(2, 132, 199, ${bub.alpha * 0.5})`
                    : `rgba(125, 211, 252, ${bub.alpha})`;
                ctx.fill();
            });
            
            // Mouse gradient glow light beam
            const grad = ctx.createRadialGradient(mouse.x, mouse.y, 0, mouse.x, mouse.y, 220);
            if (isLight) {
                grad.addColorStop(0, 'rgba(3, 105, 161, 0.05)');
                grad.addColorStop(0.5, 'rgba(147, 51, 234, 0.02)');
            } else {
                grad.addColorStop(0, 'rgba(14, 165, 233, 0.06)');
                grad.addColorStop(0.5, 'rgba(168, 85, 247, 0.02)');
            }
            grad.addColorStop(1, 'rgba(0, 0, 0, 0)');
            ctx.fillStyle = grad;
            ctx.fillRect(0, 0, width, height);
            
            requestAnimationFrame(animate);
        };
        animate();
    }
    
    // Global 3D Perspective Tilt on the entire Streamlit page viewport
    const applyGlobal3D = () => {
        const appContainer = parentDoc.querySelector('[data-testid="stAppViewContainer"]');
        const mainContent = parentDoc.querySelector('section.main');
        if (appContainer && mainContent && !mainContent.dataset.global3dActive) {
            mainContent.dataset.global3dActive = "true";
            appContainer.style.perspective = '1500px';
            appContainer.style.perspectiveOrigin = '50% 50%';
            
            mainContent.style.transformStyle = 'preserve-3d';
            mainContent.style.transition = 'transform 0.25s cubic-bezier(0.25, 0.8, 0.25, 1)';
            
            parentDoc.addEventListener('mousemove', (e) => {
                const xc = parentDoc.documentElement.clientWidth / 2;
                const yc = parentDoc.documentElement.clientHeight / 2;
                const angleX = -((e.clientY - yc) / yc) * 3; // Up to 3 deg tilt
                const angleY = ((e.clientX - xc) / xc) * 3; // Up to 3 deg tilt
                
                mainContent.style.transform = `rotateX(${angleX}deg) rotateY(${angleY}deg) translateZ(0px)`;
            });
        }
    };
    
    // 3D Tilt effects for KPI cards (Local Parallax)
    const apply3DTilt = () => {
        const cards = parentDoc.querySelectorAll('.kpi-card, .login-card, [data-testid="stMetricValue"]');
        cards.forEach(card => {
            if (card.dataset.tiltActive) return;
            card.dataset.tiltActive = "true";
            
            card.style.transformStyle = 'preserve-3d';
            card.style.perspective = '1000px';
            card.style.transition = 'transform 0.15s ease-out, box-shadow 0.15s ease-out';
            
            card.addEventListener('mousemove', (e) => {
                const rect = card.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                const xc = rect.width / 2;
                const yc = rect.height / 2;
                
                const angleX = -(y - yc) / 7;
                const angleY = (x - xc) / 7;
                
                card.style.transform = `rotateX(${angleX}deg) rotateY(${angleY}deg) scale3d(1.025, 1.025, 1.025) translateZ(10px)`;
                card.style.boxShadow = `0 15px 35px rgba(14, 165, 233, 0.22)`;
            });
            
            card.addEventListener('mouseleave', () => {
                card.style.transform = 'rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1) translateZ(0px)';
                card.style.boxShadow = '';
            });
        });
    };
    
    const observer = new MutationObserver(() => {
        applyGlobal3D();
        apply3DTilt();
    });
    observer.observe(parentDoc.body, { childList: true, subtree: true });
    applyGlobal3D();
    apply3DTilt();
};

// Delay initialization slightly to guarantee DOM stability
setTimeout(injectInteractiveEffects, 500);
</script>
"""

def get_login_css():
    return """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200;400;500;600;700;800;900&display=swap');
@import url('https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css');

/* Global resets and font styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Poppins', sans-serif !important;
}

/* Hide default streamlit elements */
header, [data-testid="stHeader"] {
    display: none !important;
}
footer {
    display: none !important;
}
[data-testid="collapsedControl"] {
    display: none !important;
}

html, body, 
.stApp,
[data-testid="stAppViewContainer"], 
[data-testid="stAppViewBlockContainer"],
[data-testid="stMainBlockContainer"],
.main,
section.main {
    min-height: 100vh !important;
    min-height: 100dvh !important;
    height: auto !important;
    overflow-y: auto !important;
    overflow-x: hidden !important;
}

html {
    background: transparent !important;
}

/* Force full screen background layout - Dark Theme (Default) */
body {
    background: url("https://i.pinimg.com/originals/d7/b9/0c/d7b90cc80898e8823455a127945719af.jpg") no-repeat !important;
    background-size: cover !important;
    background-position: center !important;
    width: 100vw !important;
    transition: background 0.5s ease-in-out !important;
}

/* Light Theme Background override (Rich Dark Cream & Warm Sand Gradient) */
body.light-theme {
    background: linear-gradient(135deg, #ebdcb9 0%, #d8c397 100%) !important;
    background-image: none !important;
}

[data-testid="stAppViewContainer"] {
    background: transparent !important;
    position: relative !important;
    z-index: 2 !important;
}

[data-testid="stMainBlockContainer"] {
    padding: 0 !important;
    margin: 0 !important;
    max-width: 100% !important;
    min-height: 100vh !important;
    min-height: 100dvh !important;
    height: auto !important;
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
}

/* Center Horizontal Block */
div[data-testid="stHorizontalBlock"] {
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    width: 100% !important;
    margin: 0 !important;
    padding: 0 !important;
}

/* Blue Glassmorphism Login Card Wrapper Reset */
div[data-testid="stVerticalBlockBorderWrapper"]:has(.st-key-login_card) {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}

/* Single Blue Glassmorphism Login Card */
.st-key-login_card {
    width: 100% !important;
    max-width: 480px !important; /* Widened horizontally */
    background: rgba(10, 25, 47, 0.12) !important; /* Soft transparent background */
    border: 1.5px solid rgba(14, 165, 233, 0.25) !important; /* Soft solid blue border */
    
    backdrop-filter: blur(20px) !important;
    -webkit-backdrop-filter: blur(20px) !important;
    
    /* Multi-layered gradient neon glow shadow (Blue, Green, and Ambient) */
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4), 
                0 0 25px rgba(14, 165, 233, 0.2), 
                0 0 12px rgba(16, 185, 129, 0.15), 
                inset 0 0 20px rgba(14, 165, 233, 0.1) !important;
                
    color: #fff !important;
    border-radius: 16px !important;
    padding: 20px 32px !important; /* Reduced vertical padding, increased horizontal */
    z-index: 10 !important;
    position: relative !important;
    transition: all 0.5s ease !important;
    margin: 0 auto !important; /* Center horizontally with no vertical margin pushing it down */
    
    /* User requested styles */
    font-size: 16px !important;
    font-weight: 400 !important;
    line-height: 1.6 !important;
    text-size-adjust: 100% !important;
    -webkit-tap-highlight-color: rgba(0, 0, 0, 0) !important;
    -webkit-font-smoothing: auto !important;
    font-family: 'Outfit', sans-serif !important;
    color: rgb(249, 250, 251) !important;
    color-scheme: dark !important;
    user-select: auto !important;
    box-sizing: border-box !important;
}

/* Light Theme overrides for card - Transparent Sky Blue Glass with Glow Shadow */
body.light-theme .st-key-login_card {
    background: rgba(224, 242, 254, 0.35) !important;
    border: 1.5px solid rgba(14, 165, 233, 0.3) !important;
    box-shadow: 0 15px 35px rgba(14, 165, 233, 0.1), 
                0 0 20px rgba(16, 185, 129, 0.12), 
                inset 0 0 15px rgba(255, 255, 255, 0.5) !important;
}

/* Force absolute black text in light theme for all elements inside the login card */
body.light-theme .st-key-login_card * {
    color: #000000 !important;
}
/* Keep submit button text white */
body.light-theme .st-key-login_card div.stButton button,
body.light-theme .st-key-login_card div.stButton button * {
    color: #ffffff !important;
}
/* Keep links blue */
body.light-theme .st-key-login_card a,
body.light-theme .st-key-login_card a * {
    color: #0284c7 !important;
}

/* Center the horizontal columns block */
div[data-testid="stHorizontalBlock"] {
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    width: 100% !important;
}

/* Let the middle column center nicely */
div[data-testid="column"]:has(.st-key-login_card) {
    width: 100% !important;
    max-width: 480px !important;
    flex: none !important;
    margin: 0 auto !important; /* Force centering the column itself! */
    display: flex !important;
    justify-content: center !important;
}

/* Hide first and third columns in layout to focus on the login card */
div[data-testid="column"]:not(:has(.st-key-login_card)) {
    display: none !important;
}

/* Form Title styling - Dynamic Color Shift Gradient */
.st-key-login_card h1,
div[data-testid="stVerticalBlockBorderWrapper"]:has(.st-key-login_card) h1 {
    font-size: 26px !important; /* Compact title font size */
    text-align: center !important;
    margin-top: 0 !important;
    margin-bottom: 10px !important; /* Compact margin */
    font-weight: 700 !important;
    letter-spacing: -0.5px !important;
    background: linear-gradient(-45deg, #10b981, #0ea5e9, #a855f7, #10b981) !important;
    background-size: 300% 300% !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    animation: text-gradient 6s ease infinite !important;
}

/* Input container box */
div[data-testid="stTextInput"] {
    position: relative !important;
    width: 100% !important;
    height: auto !important;
    margin: 12px 0 !important;
    background: transparent !important;
}

/* Show input label */
div[data-testid="stTextInput"] label {
    display: block !important;
    font-family: 'Outfit', sans-serif !important;
    font-size: 14px !important;
    font-weight: 500 !important;
    color: rgb(249, 250, 251) !important;
    margin-bottom: 6px !important;
    width: 100% !important;
    text-align: left !important;
}

/* BaseWeb elements resets */
div[data-testid="stTextInput"] > div[data-baseweb="input"] {
    background: rgba(10, 15, 30, 0.65) !important; /* Dark solid slate fill color */
    border: 1.5px solid rgba(255, 255, 255, 0.15) !important;
    border-radius: 12px !important;
    height: 48px !important;
    width: 100% !important;
    transition: all 0.22s ease !important;
}
div[data-testid="stTextInput"] > div[data-baseweb="input"]:focus-within {
    border-color: #0ea5e9 !important;
    box-shadow: 0 0 15px rgba(14, 165, 233, 0.45) !important;
    background: rgba(10, 15, 30, 0.85) !important;
}

/* The actual input field - Dark Theme */
div[data-testid="stTextInput"] input {
    width: 100% !important;
    height: 100% !important;
    background: transparent !important;
    border: none !important;
    border-radius: 0 !important;
    font-size: 15px !important;
    color: #fff !important;
    padding: 12px 40px 12px 14px !important; /* Spaced padding-right for eye button */
    outline: none !important;
    box-shadow: none !important;
}
div[data-testid="stTextInput"] input::placeholder {
    color: rgba(255, 255, 255, 0.6) !important;
}

/* Light Theme overrides for inputs */
body.light-theme div[data-testid="stTextInput"] > div[data-baseweb="input"] {
    background: #faf8f2 !important;
    border: 2px solid rgba(10, 15, 29, 0.3) !important;
}
body.light-theme div[data-testid="stTextInput"] > div[data-baseweb="input"]:focus-within {
    border-color: #0ea5e9 !important;
    box-shadow: 0 0 12px rgba(14, 165, 233, 0.35) !important;
    background: #ffffff !important;
}
body.light-theme div[data-testid="stTextInput"] input {
    background: transparent !important;
    color: #0a0f1d !important;
    font-weight: 500 !important;
    border: none !important;
}
body.light-theme div[data-testid="stTextInput"] input::placeholder {
    color: rgba(10, 15, 29, 0.65) !important;
}

/* Set position relative for icon placement */
div[data-testid="stTextInput"] > div {
    position: relative !important;
}

/* Username Icon */
div[data-testid="stTextInput"]:has(input#login_user_input) > div::after {
    content: "\\eec4" !important;
    font-family: 'boxicons' !important;
    position: absolute !important;
    right: 20px !important;
    top: 50% !important;
    transform: translateY(-50%) !important;
    font-size: 20px !important;
    color: #fff !important;
    pointer-events: none !important;
}

/* Password Icon */
div[data-testid="stTextInput"]:has(input#login_pwd_input) > div::after {
    content: "\\eea7" !important;
    font-family: 'boxicons' !important;
    position: absolute !important;
    right: 20px !important;
    top: 50% !important;
    transform: translateY(-50%) !important;
    font-size: 20px !important;
    color: #fff !important;
    pointer-events: none !important;
}

body.light-theme div[data-testid="stTextInput"] > div::after {
    color: #0a0f1d !important;
}

/* Remember Forgot Section - Dark */
.remember-forgot {
    display: flex !important;
    justify-content: space-between !important;
    font-size: 14px !important;
    margin: 8px 0 12px !important;
    color: #fff !important;
}
body.light-theme .remember-forgot {
    color: #0a0f1d !important;
    font-weight: 500 !important;
}

.remember-forgot label {
    display: flex !important;
    align-items: center !important;
    cursor: pointer !important;
}

.remember-forgot label input {
    accent-color: #fff !important;
    margin-right: 5px !important;
    cursor: pointer !important;
}
body.light-theme .remember-forgot label input {
    accent-color: #0a0f1d !important;
}

.remember-forgot a {
    color: #fff !important;
    text-decoration: none !important;
}
body.light-theme .remember-forgot a {
    color: #0284c7 !important;
    font-weight: 600 !important;
}
.remember-forgot a:hover {
    text-decoration: underline !important;
}

/* Submit Button - Dark Theme */
div.stButton button,
div.stButton button * {
    background-color: #ffffff !important;
    background: #ffffff !important;
    color: #0c1524 !important;
    font-weight: 700 !important;
    opacity: 1 !important;
    visibility: visible !important;
}

div.stButton button {
    width: 100% !important;
    height: 45px !important;
    border: none !important;
    outline: none !important;
    border-radius: 40px !important;
    box-shadow: 0 4px 15px rgba(255, 255, 255, 0.15) !important;
    cursor: pointer !important;
    font-size: 16px !important;
    position: relative !important;
    overflow: hidden !important;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
}
div.stButton button::before {
    content: '' !important;
    position: absolute !important;
    top: 0 !important;
    left: -100% !important;
    width: 100% !important;
    height: 100% !important;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent) !important;
    transition: 0.5s ease !important;
}
div.stButton button:hover {
    background-color: #ffffff !important;
    background: #ffffff !important;
    box-shadow: 0 0 20px rgba(255, 255, 255, 0.6) !important;
    transform: translateY(-2px) !important;
}
div.stButton button:hover::before {
    left: 100% !important;
}
div.stButton button:focus, div.stButton button:active {
    border: none !important;
    outline: none !important;
    background-color: #ffffff !important;
    background: #ffffff !important;
    color: #0c1524 !important;
    box-shadow: 0 0 20px rgba(255, 255, 255, 0.6) !important;
}

/* Light Theme Button */
body.light-theme div.stButton button {
    background: #0a0f1d !important;
    color: #fff !important;
    box-shadow: 0 4px 15px rgba(10, 15, 29, 0.25) !important;
}
body.light-theme div.stButton button:hover {
    background: #000000 !important;
    box-shadow: 0 6px 20px rgba(10, 15, 29, 0.4) !important;
    transform: translateY(-2px) !important;
}

/* Register link section */
.register-link {
    text-align: center !important;
    font-size: 14px !important;
    margin: 20px 0 15px !important;
    color: #fff !important;
}
body.light-theme .register-link {
    color: #0a0f1d !important;
}

.register-link p a {
    color: #fff !important;
    text-decoration: none !important;
    font-weight: 600 !important;
}
body.light-theme .register-link p a {
    color: #0284c7 !important;
    font-weight: 700 !important;
}
.register-link p a:hover {
    text-decoration: underline !important;
}

/* Keyframes for animations */
@keyframes float-card {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-8px); }
    100% { transform: translateY(0px); }
}

/* Hide password visibility screen reader helper text but keep icon */
div[data-testid="stTextInput"] button {
    color: transparent !important;
    font-size: 0 !important;
    background: transparent !important;
    border: none !important;
}
div[data-testid="stTextInput"] button div,
div[data-testid="stTextInput"] button span,
div[data-testid="stTextInput"] [aria-live="polite"] {
    display: none !important;
}
div[data-testid="stTextInput"] button svg {
    color: #fff !important;
    width: 20px !important;
    height: 20px !important;
}
body.light-theme div[data-testid="stTextInput"] button svg {
    color: #0a0f1d !important;
}

/* Logo styling with high specificity */
.logo-container .logo-text,
.st-key-login_card .logo-container span.logo-text,
.st-key-login_card span.logo-text {
    color: #ffffff !important;
}

body.light-theme .logo-container .logo-text,
body.light-theme .st-key-login_card .logo-container span.logo-text,
body.light-theme .st-key-login_card span.logo-text {
    color: #000000 !important;
}

/* Password Hint styling */
.password-hint {
    color: rgba(255, 255, 255, 0.45) !important;
}
body.light-theme .password-hint {
    color: rgba(10, 15, 29, 0.70) !important;
}

/* Force absolute black text in light theme for all elements */
body.light-theme .remember-forgot,
body.light-theme .remember-forgot label,
body.light-theme .register-link,
body.light-theme .register-link p,
body.light-theme .register-link p strong {
    color: #000000 !important;
}

@keyframes text-gradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
</style>

<!-- Extra light-theme visibility fixes inserted by assistant -->
<style>
/* Ensure readable text and visible controls in light theme */
body.light-theme, body.light-theme * {
    color: #0a0f1d !important;
}
body.light-theme a, body.light-theme a * {
    color: #0369a1 !important;
}
body.light-theme .logo-container {
    z-index: 12 !important;
    margin-bottom: 18px !important;
}
body.light-theme .logo-emoji-circle {
    background: linear-gradient(135deg,#10b981 0%,#0ea5e9 100%) !important;
    box-shadow: 0 0 12px rgba(16,185,129,0.18) !important;
    color: #ffffff !important;
}
body.light-theme div.stButton button,
body.light-theme div.stButton button * {
    background: linear-gradient(90deg,#0a0f1d,#06202a) !important;
    color: #ffffff !important;
    border: none !important;
}
body.light-theme div[data-testid="stTextInput"] > div[data-baseweb="input"] {
    background: #ffffff !important;
    border: 1px solid rgba(10,15,29,0.12) !important;
}
body.light-theme div[data-testid="stTextInput"] input {
    background: transparent !important;
    color: #0a0f1d !important;
    border: none !important;
}
body.light-theme .remember-forgot {
    color: #0a0f1d !important;
}

/* Login form stability and responsive layout */
html, body, 
.stApp,
[data-testid="stAppViewContainer"], 
[data-testid="stAppViewBlockContainer"],
[data-testid="stMainBlockContainer"],
.main,
section.main {
    min-height: 100vh !important;
    min-height: 100dvh !important;
    height: auto !important;
    overflow-y: auto !important;
    overflow-x: hidden !important;
}

[data-testid="stMainBlockContainer"] {
    padding: 16px !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: center !important;
    align-items: center !important;
}

/* Center all child elements vertically and horizontally inside Main Block Container */
[data-testid="stMainBlockContainer"] > div {
    display: flex !important;
    flex-direction: column !important;
    justify-content: center !important;
    align-items: center !important;
    width: 100% !important;
}

.st-key-login_card {
    width: min(480px, calc(100vw - 24px)) !important;
    max-width: 480px !important;
    padding: 20px 32px !important;
}

.st-key-login_card [data-testid="stVerticalBlock"] {
    gap: 10px !important; /* Compresses vertical spacing */
}

div[data-testid="stVerticalBlockBorderWrapper"]:has(.st-key-login_card) {
    width: min(480px, calc(100vw - 24px)) !important;
    max-width: 480px !important;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
    margin: 0 auto !important; /* Force centering the wrapper! */
}

.st-key-login_card [data-testid="stVerticalBlockBorderWrapper"] {
    border: 0 !important;
    padding: 0 !important;
    background: transparent !important;
    box-shadow: none !important;
}

.st-key-login_user_input > div,
.st-key-login_pwd_input > div {
    position: relative !important;
}

</style>
"""

def get_login_javascript():
    return """
<script>
const injectLoginAnimation = () => {
    const mainDoc = window.parent.document;
    const mainWin = window.parent;
    
    // Check if canvas already exists to avoid duplicates
    if (!mainDoc.getElementById('login-animation-canvas')) {
        const canvas = mainDoc.createElement('canvas');
        canvas.id = 'login-animation-canvas';
        canvas.style.position = 'fixed';
        canvas.style.top = '0';
        canvas.style.left = '0';
        canvas.style.width = '100vw';
        canvas.style.height = '100vh';
        canvas.style.zIndex = '1'; // Layered between background image (0) and streamlit content (2)
        canvas.style.pointerEvents = 'none';
        mainDoc.body.appendChild(canvas);
        
        const ctx = canvas.getContext('2d');
        let width = canvas.width = mainWin.innerWidth;
        let height = canvas.height = mainWin.innerHeight;
        
        mainWin.addEventListener('resize', () => {
            width = canvas.width = mainWin.innerWidth;
            height = canvas.height = mainWin.innerHeight;
        });
        
        // Fare takip şeridi noktaları dizisi
        const trailPoints = [];
        
        mainDoc.addEventListener('mousemove', (e) => {
            // Fare hareket ettikçe noktaları ve ilk opaklık değerini ekliyoruz
            trailPoints.push({
                x: e.clientX,
                y: e.clientY,
                alpha: 1.0
            });
            
            // Performans için şerit uzunluğunu sınırlandırıyoruz
            if (trailPoints.length > 25) {
                trailPoints.shift();
            }
        });
        
        const animate = () => {
            if (!mainDoc.body.contains(canvas)) return;
            
            // Check theme dynamically from parent window document
            const mainEl = mainDoc.documentElement || mainDoc.body;
            const style = mainWin.getComputedStyle(mainEl);
            const textColor = style.getPropertyValue('--text-color').trim();
            const bgColor = style.getPropertyValue('--background-color').trim();
            
            // Matematiksel parlaklık hesabı yapan fonksiyon
            const getBrightness = (colorStr) => {
                if (!colorStr) return 0;
                const rgb = colorStr.match(/\\d+/g);
                if (rgb && rgb.length >= 3) {
                    return (parseInt(rgb[0]) * 0.299 + parseInt(rgb[1]) * 0.587 + parseInt(rgb[2]) * 0.114);
                }
                if (colorStr.startsWith('#')) {
                    let hex = colorStr.slice(1);
                    if (hex.length === 3) hex = hex.split('').map(x => x + x).join('');
                    if (hex.length === 6) {
                        const r = parseInt(hex.slice(0, 2), 16);
                        const g = parseInt(hex.slice(2, 4), 16);
                        const b = parseInt(hex.slice(4, 6), 16);
                        return (r * 0.299 + g * 0.587 + b * 0.114);
                    }
                }
                return 0;
            };
            
            // Eğer arka plan rengi aydınlıksa (> 120 parlaklık), kesinlikle açık moddadır
            const bgBrightness = getBrightness(bgColor);
            const textBrightness = getBrightness(textColor);
            
            let isLight = false;
            if (bgBrightness > 120) {
                isLight = true;
            } else if (textColor.includes('49') || textColor.includes('51') || textColor.toLowerCase().includes('31333f')) {
                isLight = true;
            }
            
            if (isLight) {
                mainDoc.body.classList.add('light-theme');
                mainDoc.body.classList.remove('dark-theme');
                document.body.classList.add('light-theme');
                document.body.classList.remove('dark-theme');
            } else {
                mainDoc.body.classList.add('dark-theme');
                mainDoc.body.classList.remove('light-theme');
                document.body.classList.add('dark-theme');
                document.body.classList.remove('light-theme');
            }
            
            ctx.clearRect(0, 0, width, height);
            
            // Waving flag-like gradient mesh bands (Vibrant Green & Blue themes)
            const drawWavingWaves = () => {
                const time = Date.now() * 0.001; // stable clock
                
                const bands = [
                    {
                        yCenter: height * 0.45,
                        amp: 70,
                        freq: 0.003,
                        speed: 0.8,
                        colorDarkStart: 'rgba(16, 185, 129, 0.18)',  // Logodaki Zümrüt Yeşili
                        colorDarkEnd: 'rgba(4, 120, 87, 0.03)',
                        colorLightStart: 'rgba(16, 185, 129, 0.35)', // Canlı Yeşil (Light)
                        colorLightEnd: 'rgba(16, 185, 129, 0.05)'
                    },
                    {
                        yCenter: height * 0.52,
                        amp: 90,
                        freq: 0.002,
                        speed: -0.6,
                        colorDarkStart: 'rgba(14, 165, 233, 0.15)',  // Parlak Sky Mavi
                        colorDarkEnd: 'rgba(30, 58, 138, 0.02)',
                        colorLightStart: 'rgba(14, 165, 233, 0.35)', // Canlı Sky Mavi (Light)
                        colorLightEnd: 'rgba(14, 165, 233, 0.05)'
                    },
                    {
                        yCenter: height * 0.56,
                        amp: 80,
                        freq: 0.0025,
                        speed: -0.9,
                        colorDarkStart: 'rgba(6, 182, 212, 0.38)',   // Parlak Neon Cyan Dalga (Yeni Parlak Işıklı Dalga!)
                        colorDarkEnd: 'rgba(6, 182, 212, 0.02)',
                        colorLightStart: 'rgba(6, 182, 212, 0.55)',  // Neon Cyan Light (Very bright!)
                        colorLightEnd: 'rgba(6, 182, 212, 0.05)'
                    },
                    {
                        yCenter: height * 0.62,
                        amp: 60,
                        freq: 0.004,
                        speed: 1.1,
                        colorDarkStart: 'rgba(168, 85, 247, 0.12)',  // Canlı Eflatun/Mor
                        colorDarkEnd: 'rgba(0, 0, 0, 0)',
                        colorLightStart: 'rgba(168, 85, 247, 0.30)', // Canlı Eflatun (Light)
                        colorLightEnd: 'rgba(168, 85, 247, 0.02)'
                    }
                ];
                
                bands.forEach(b => {
                    ctx.beginPath();
                    ctx.moveTo(0, height);
                    for (let x = 0; x <= width; x += 15) {
                        const y = b.yCenter + Math.sin(x * b.freq + time * b.speed) * b.amp;
                        ctx.lineTo(x, y);
                    }
                    ctx.lineTo(width, height);
                    ctx.closePath();
                    
                    // Dikey geçişli gradyan oluştur
                    const grad = ctx.createLinearGradient(0, b.yCenter - b.amp, 0, height);
                    if (isLight) {
                        grad.addColorStop(0, b.colorLightStart);
                        grad.addColorStop(1, b.colorLightEnd);
                    } else {
                        grad.addColorStop(0, b.colorDarkStart);
                        grad.addColorStop(1, b.colorDarkEnd);
                    }
                    
                    ctx.fillStyle = grad;
                    ctx.fill();
                    
                    // Üst kenara parlayan neon çizgisi ekle (Glow Effect)
                    ctx.beginPath();
                    for (let x = 0; x <= width; x += 15) {
                        const y = b.yCenter + Math.sin(x * b.freq + time * b.speed) * b.amp;
                        if (x === 0) {
                            ctx.moveTo(x, y);
                        } else {
                            ctx.lineTo(x, y);
                        }
                    }
                    ctx.save();
                    ctx.shadowBlur = 12;
                    ctx.shadowColor = isLight ? b.colorLightStart : b.colorDarkStart;
                    ctx.strokeStyle = isLight ? b.colorLightStart : b.colorDarkStart;
                    ctx.lineWidth = 2.0;
                    ctx.stroke();
                    ctx.restore();
                });
            };
            drawWavingWaves();
            
            // Fare takip şeridini (ribbon) çiz
            if (trailPoints.length > 1) {
                ctx.save();
                ctx.lineCap = 'round';
                ctx.lineJoin = 'round';
                
                // Neon parlama efekti için gölge ayarları (Hafif ve hızlı)
                ctx.shadowBlur = 10;
                ctx.shadowColor = isLight ? '#0ea5e9' : '#10b981';
                
                for (let i = 1; i < trailPoints.length; i++) {
                    const p1 = trailPoints[i - 1];
                    const p2 = trailPoints[i];
                    
                    ctx.beginPath();
                    ctx.moveTo(p1.x, p1.y);
                    ctx.lineTo(p2.x, p2.y);
                    
                    const ratio = i / trailPoints.length; // Kuyruktan imlece doğru oran (0-1)
                    ctx.lineWidth = ratio * 7 + 1.5; // Kuyruğa doğru incelme
                    
                    // Şerit opaklık sönümlemesi
                    const alpha = p2.alpha * ratio;
                    ctx.strokeStyle = isLight ? `rgba(14, 165, 233, ${alpha})` : `rgba(16, 185, 129, ${alpha})`;
                    
                    ctx.stroke();
                }
                ctx.restore();
            }
            
            // Şerit noktalarının opaklığını azalt ve bitenleri diziden çıkar
            for (let i = trailPoints.length - 1; i >= 0; i--) {
                trailPoints[i].alpha -= 0.035; // Kaybolma hızı
                if (trailPoints[i].alpha <= 0) {
                    trailPoints.splice(i, 1);
                }
            }
            
            requestAnimationFrame(animate);
        };
        animate();
    }
};

setTimeout(injectLoginAnimation, 200);
</script>
"""


