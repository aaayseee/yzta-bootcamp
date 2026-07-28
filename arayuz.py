import streamlit as st
import os
import sqlite3

# Compatibility helper for Streamlit rerun across versions
def _safe_rerun():
    try:
        # Preferred in older/newer Streamlit versions
        st.experimental_rerun()
    except Exception:
        # Fallback: stop execution; session state changes persist and UI will update on next interaction
        st.stop()

# Query parameters compatibility helpers
def _get_query_param(key):
    try:
        params = st.query_params
        if key in params:
            val = params[key]
            if isinstance(val, list):
                return val[0] if val else None
            return val
    except AttributeError:
        try:
            params = st.experimental_get_query_params()
            if key in params:
                val = params[key]
                if isinstance(val, list):
                    return val[0] if val else None
                return val
        except Exception:
            pass
    return None

def _clear_query_params():
    try:
        st.query_params.clear()
    except AttributeError:
        try:
            st.experimental_set_query_params()
        except Exception:
            pass

# User database functions
def _init_user_db():
    db_path = os.environ.get('SQLITE_PATH', 'loyalcart.db')
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            email TEXT,
            password TEXT,
            role TEXT
        )
    ''')
    # Default admin
    cur.execute("SELECT * FROM users WHERE username = 'admin'")
    if not cur.fetchone():
        cur.execute("INSERT INTO users (username, email, password, role) VALUES ('admin', 'admin@loyalcart.com', '12345', 'administrator')")
        conn.commit()
    conn.close()

def _verify_user(username, password):
    try:
        _init_user_db()
        db_path = os.environ.get('SQLITE_PATH', 'loyalcart.db')
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("SELECT password FROM users WHERE LOWER(username) = ?", (username.lower(),))
        row = cur.fetchone()
        conn.close()
        if row and row[0] == password:
            return True
    except Exception:
        pass
    return False

def _register_user(username, email, password, role="manager"):
    try:
        _init_user_db()
        db_path = os.environ.get('SQLITE_PATH', 'loyalcart.db')
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("INSERT INTO users (username, email, password, role) VALUES (?, ?, ?, ?)", 
                    (username, email, password, role))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        pass
    except Exception:
        pass
    return False

# 1. Page Configuration
st.set_page_config(
    page_title="LoyalCart Yönetici Paneli Girişi",
    page_icon="🔑",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Imports from custom modules
from styles import get_custom_css, get_3d_javascript, get_login_css, get_login_javascript
from data_loader import get_synthetic_data
from components.sidebar import render_sidebar

# Import page view renderers
from pages_views.dashboard import render_dashboard_page
from pages_views.customer_analysis import render_customer_analysis_page
from pages_views.segmentation import render_segmentation_page
from pages_views.history import render_history_page
from pages_views.simulation import render_simulation_page
from pages_views.early_warning import render_early_warning_page
from pages_views.cohort import render_cohort_page
from pages_views.complaints import render_complaints_page
from pages_views.nps_league import render_nps_league_page
from pages_views.integrations import render_integrations_page

# 3. Authentication Check & Styling Dispatcher
if st.session_state.get("just_logged_out"):
    st.iframe("""
    <script>
        parent.window.localStorage.removeItem("loyalcart_remembered_user");
        parent.window.localStorage.removeItem("loyalcart_remembered_token");
        parent.window.location.href = parent.window.location.origin + parent.window.location.pathname;
    </script>
    """, height=1, width=1)
    st.session_state.logged_in = False
    st.session_state.just_logged_out = False
    st.stop()

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = os.environ.get('AUTO_LOGIN', '0') == '1'

# Check auto-login from query params
auto_user = _get_query_param("auto_login")
auto_token = _get_query_param("token")

if auto_user and auto_token:
    if _verify_user(auto_user, auto_token):
        st.session_state.logged_in = True
        st.session_state.username = auto_user
        st.session_state.save_remember_me = True
        _clear_query_params()
        _safe_rerun()

is_forgot = _get_query_param("forgot") == "true"
is_register = _get_query_param("register") == "true"

if not st.session_state.logged_in:
    # Check if we should auto-login using browser localStorage
    if not auto_user:
        st.iframe("""
        <script>
            const rememberedUser = parent.window.localStorage.getItem("loyalcart_remembered_user");
            const rememberedToken = parent.window.localStorage.getItem("loyalcart_remembered_token");
            if (rememberedUser && rememberedToken && !parent.window.location.search.includes("auto_login")) {
                const url = new URL(parent.window.location.href);
                url.searchParams.set("auto_login", rememberedUser);
                url.searchParams.set("token", rememberedToken);
                parent.window.location.href = url.toString();
            }
        </script>
        """, height=1, width=1)

    # Inject Login styling + custom fixes (left-aligned to prevent markdown code block formatting)
    st.markdown(get_login_css() + """
<style>
/* Inner rectangular card wrapper - scoped to login column */
div[data-testid="column"]:has(.logo-container) div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(0, 0, 0, 0.28) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: 12px !important;
    padding: 24px !important;
    box-shadow: inset 0 0 15px rgba(0, 0, 0, 0.25) !important;
    margin-top: 10px !important;
}
body.light-theme div[data-testid="column"]:has(.logo-container) div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255, 255, 255, 0.8) !important;
    border: 1px solid rgba(10, 15, 29, 0.12) !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04) !important;
}

/* Absolute label collapse to fix click/focus shifts - scoped to login column */
div[data-testid="column"]:has(.logo-container) div[data-testid="stTextInput"] label, 
div[data-testid="column"]:has(.logo-container) div[data-testid="stTextInput"] label * {
    display: none !important;
    height: 0px !important;
    min-height: 0px !important;
    margin: 0px !important;
    padding: 0px !important;
}
</style>
""", unsafe_allow_html=True)
    st.iframe(get_login_javascript(), height=1, width=1)
    
    col1, col2, col3 = st.columns([1, 1.8, 1])
    with col2:
        if is_forgot:
            st.markdown("""
            <div class="logo-container" style="text-align: center; margin-bottom: 35px; width: 100%;">
                <span class="logo-text" style="font-weight: 900; font-size: 44px; display: inline-flex; align-items: center; justify-content: center; gap: 6px; letter-spacing: -1px; line-height: 1;">
                    L<span class="logo-emoji-circle" style="background: linear-gradient(135deg, #10b981 0%, #0ea5e9 100%); width: 48px; height: 48px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 24px; box-shadow: 0 0 20px rgba(16, 185, 129, 0.6); margin: 0 3px; color: #fff !important; transform: translateY(1px);">🛒</span>yalCart
                </span>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<h1 style='font-size: 28px; text-align: center; margin-bottom: 20px;'>Şifre Sıfırlama</h1>", unsafe_allow_html=True)
            
            with st.container(border=True):
                email_or_user = st.text_input("Kullanıcı Adı veya E-posta", placeholder="Kullanıcı Adı veya E-posta", key="reset_user_input", label_visibility="collapsed")
                
                if st.button("Şifre Sıfırlama Kodu Gönder", width='stretch'):
                    if not email_or_user:
                        st.error("❌ Lütfen kullanıcı adınızı veya e-posta adresinizi girin!")
                    elif email_or_user.lower() not in ["admin", "yonetici", "yönetici", "manager"]:
                        # check DB as well
                        _init_user_db()
                        db_path = os.environ.get('SQLITE_PATH', 'loyalcart.db')
                        conn = sqlite3.connect(db_path)
                        cur = conn.cursor()
                        cur.execute("SELECT * FROM users WHERE LOWER(username) = ? OR LOWER(email) = ?", (email_or_user.lower(), email_or_user.lower()))
                        exists = cur.fetchone()
                        conn.close()
                        if not exists:
                            st.error("❌ Bu kullanıcı adına veya e-postaya sahip bir yönetici bulunamadı!")
                        else:
                            st.success("✉️ Şifre sıfırlama bağlantısı e-posta adresinize başarıyla gönderildi!")
                    else:
                        st.success("✉️ Şifre sıfırlama bağlantısı e-posta adresinize başarıyla gönderildi!")
                        st.info("💡 İpucu: Yönetici şifresi varsayılan olarak **12345**'tir.")
                
                st.markdown("""
                <div class="register-link" style="margin-top: 15px; margin-bottom: 0;">
                    <p><a href="?forgot=false" target="_self">Giriş Ekranına Dön</a></p>
                </div>
                """, unsafe_allow_html=True)
        elif is_register:
            st.markdown("""
            <div class="logo-container" style="text-align: center; margin-bottom: 35px; width: 100%;">
                <span class="logo-text" style="font-weight: 900; font-size: 44px; display: inline-flex; align-items: center; justify-content: center; gap: 6px; letter-spacing: -1px; line-height: 1;">
                    L<span class="logo-emoji-circle" style="background: linear-gradient(135deg, #10b981 0%, #0ea5e9 100%); width: 48px; height: 48px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 24px; box-shadow: 0 0 20px rgba(16, 185, 129, 0.6); margin: 0 3px; color: #fff !important; transform: translateY(1px);">🛒</span>yalCart
                </span>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<h1 style='font-size: 28px; text-align: center; margin-bottom: 20px;'>Yönetici Kaydı</h1>", unsafe_allow_html=True)
            
            with st.container(border=True):
                reg_username = st.text_input("Kullanıcı Adı", placeholder="Kullanıcı Adı", key="reg_user_input", label_visibility="collapsed")
                reg_email = st.text_input("E-posta Adresi", placeholder="E-posta Adresi", key="reg_email_input", label_visibility="collapsed")
                reg_password = st.text_input("Şifre", type="password", placeholder="Şifre", key="reg_pwd_input", label_visibility="collapsed")
                reg_pwd_confirm = st.text_input("Şifre Tekrar", type="password", placeholder="Şifre Tekrar", key="reg_pwd_confirm_input", label_visibility="collapsed")
                reg_invite = st.text_input("Yönetici Davet Kodu", placeholder="Yönetici Davet Kodu (İpucu: LOYALADMIN)", key="reg_invite_input", label_visibility="collapsed")
                
                if st.button("Kayıt Ol", width='stretch'):
                    if not reg_username or not reg_email or not reg_password or not reg_pwd_confirm or not reg_invite:
                        st.error("❌ Lütfen tüm alanları doldurun!")
                    elif reg_password != reg_pwd_confirm:
                        st.error("❌ Şifreler uyuşmuyor!")
                    elif reg_invite != "LOYALADMIN":
                        st.error("❌ Geçersiz Yönetici Davet Kodu!")
                    else:
                        success = _register_user(reg_username, reg_email, reg_password)
                        if success:
                            st.success("🎉 Yönetici kaydı başarıyla oluşturuldu!")
                            st.info("💡 Giriş ekranına dönerek yeni bilgilerinizle giriş yapabilirsiniz.")
                        else:
                            st.error("❌ Bu kullanıcı adı zaten kullanımda!")
                
                st.markdown("""
                <div class="register-link" style="margin-top: 15px; margin-bottom: 0;">
                    <p><a href="?register=false" target="_self">Giriş Ekranına Dön</a></p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="logo-container" style="text-align: center; margin-bottom: 35px; width: 100%;">
                <span class="logo-text" style="font-weight: 900; font-size: 44px; display: inline-flex; align-items: center; justify-content: center; gap: 6px; letter-spacing: -1px; line-height: 1;">
                    L<span class="logo-emoji-circle" style="background: linear-gradient(135deg, #10b981 0%, #0ea5e9 100%); width: 48px; height: 48px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 24px; box-shadow: 0 0 20px rgba(16, 185, 129, 0.6); margin: 0 3px; color: #fff !important; transform: translateY(1px);">🛒</span>yalCart
                </span>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<h1 style='font-size: 28px; text-align: center; margin-bottom: 20px;'>Yönetici Girişi</h1>", unsafe_allow_html=True)
            
            with st.container(border=True):
                # Username Input
                username = st.text_input("Username", value="admin", placeholder="Kullanıcı Adı", key="login_user_input", label_visibility="collapsed")
                
                # Password Input
                password = st.text_input("Password", type="password", placeholder="Şifre", key="login_pwd_input", label_visibility="collapsed")
                
                # Remember & Forgot Link using columns to host Streamlit native checkbox and styled link
                col_rem, col_forg = st.columns([1.1, 0.9])
                with col_rem:
                    remember_me = st.checkbox("Beni Hatırla", value=True, key="login_remember_me")
                with col_forg:
                    st.markdown("""
                    <style>
                    .forgot-link {
                        color: #ffffff !important;
                        text-decoration: none !important;
                        font-weight: 500 !important;
                        font-size: 14px !important;
                    }
                    body.light-theme .forgot-link {
                        color: #0284c7 !important;
                        font-weight: 600 !important;
                    }
                    .forgot-link:hover {
                        text-decoration: underline !important;
                    }
                    </style>
                    <div style="text-align: right; padding-top: 4px;">
                        <a href="?forgot=true" target="_self" class="forgot-link">Şifremi unuttum</a>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Login Button
                if st.button("Giriş Yap", width='stretch'):
                    if not username or not password:
                        st.error("❌ Lütfen kullanıcı adı ve şifrenizi girin!")
                    elif _verify_user(username, password):
                        st.session_state.logged_in = True
                        st.session_state.username = username
                        st.session_state.password = password
                        if remember_me:
                            st.session_state.save_remember_me = True
                        else:
                            st.session_state.clear_remember_me = True
                        _safe_rerun()
                    else:
                        st.error("❌ Geçersiz kullanıcı adı veya şifre!")
                        
                # Register Link and Hint
                st.markdown("""
                <div class="register-link" style="margin-top: 15px; margin-bottom: 0;">
                    <p>Hesabınız yok mu? <a href="?register=true" target="_self">Kayıt Ol</a></p>
                    <p class="password-hint" style="font-size: 11px; margin-top: 15px; font-weight: 400;">
                        🔑 Şifre İpucu: <strong>12345</strong>
                    </p>
                </div>
                """, unsafe_allow_html=True)
    st.stop()

# 4. Inject Dashboard CSS & Javascript when logged in
st.markdown(get_custom_css(), unsafe_allow_html=True)
st.markdown(get_3d_javascript(), unsafe_allow_html=True)

# Save/Clear localStorage credentials if flags are set
if st.session_state.get("save_remember_me"):
    st.iframe(f"""
    <script>
        parent.window.localStorage.setItem("loyalcart_remembered_user", "{st.session_state.username}");
        parent.window.localStorage.setItem("loyalcart_remembered_token", "{st.session_state.get('password')}");
    </script>
    """, height=1, width=1)
    st.session_state.save_remember_me = False

if st.session_state.get("clear_remember_me"):
    st.iframe("""
    <script>
        parent.window.localStorage.removeItem("loyalcart_remembered_user");
        parent.window.localStorage.removeItem("loyalcart_remembered_token");
    </script>
    """, height=1, width=1)
    st.session_state.clear_remember_me = False

# 5. Load Data & Render Sidebar
df_synthetic = get_synthetic_data()
selected_menu = render_sidebar()

# 6. Page Routing Dispatcher
if selected_menu == "📊 Genel Durum (Dashboard)":
    render_dashboard_page(df_synthetic)
elif selected_menu == "🔮 Churn Simülasyonu (What-If)":
    render_simulation_page(df_synthetic)
elif selected_menu == "🚨 Erken Uyarı & Aksiyon Merkezi":
    render_early_warning_page(df_synthetic)
elif selected_menu == "📈 Kohort Analiz Raporu":
    render_cohort_page(df_synthetic)
elif selected_menu == "💬 Şikayet & Bilet Yönetimi":
    render_complaints_page(df_synthetic)
elif selected_menu == "⭐ NPS & Müşteri Bağlılık Ligi":
    render_nps_league_page(df_synthetic)
elif selected_menu == "🔍 Müşteri Analiz Paneli":
    render_customer_analysis_page(df_synthetic)
elif selected_menu == "👥 Müşteri Segmentasyonu":
    render_segmentation_page(df_synthetic)
elif selected_menu == "📋 Geçmiş Tahmin Kayıtları":
    render_history_page()
elif selected_menu == "🔌 Sistem Entegrasyonları":
    render_integrations_page()