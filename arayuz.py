import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="L🛒yalCart - Churn Tahmin & Segmentasyon Portalı",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Imports from custom modules
from styles import get_custom_css, get_3d_javascript
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

# 3. Inject CSS Styles & 3D Parallax Script
st.markdown(get_custom_css(), unsafe_allow_html=True)
st.markdown(get_3d_javascript(), unsafe_allow_html=True)

# 4. Authentication Check
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    # Render the Power Switch and the styled Logo
    st.markdown("""
    <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; margin-top: 50px;">
        <!-- Logo Section -->
        <div id="login-logo-container" class="logo-dimmed" style="display: flex; align-items: center; justify-content: center; margin-bottom: 5px;">
            <span style="font-weight: 800; font-size: 54px; color: #f8fafc; display: inline-flex; align-items: center; gap: 3px; letter-spacing: -2px;">
                L<span class="logo-cart-glow" style="background: linear-gradient(135deg, #10b981 0%, #0ea5e9 100%); width: 38px; height: 38px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 20px; box-shadow: 0 0 15px rgba(16, 185, 129, 0.4); margin: 0 2px; transform: translateY(2px);">🛒</span>yalCart
            </span>
        </div>
        <p id="login-sub" style="color: #64748b; font-size: 15px; margin: 0 0 25px 0; transition: color 0.5s;">E-Ticaret Müşteri Kayıp (Churn) Tahmin ve Segmentasyon Paneli</p>
        
        <!-- Power Switch -->
        <div class="power-container">
            <span class="power-label" id="pwr-lbl">SİSTEM GÜCÜ</span>
            <label class="switch">
                <input type="checkbox" id="power-toggle">
                <span class="slider"></span>
            </label>
        </div>
    </div>
    
    <script>
    // Watch power switch toggle
    setTimeout(() => {
        const toggle = document.getElementById('power-toggle');
        const logo = document.getElementById('login-logo-container');
        const sub = document.getElementById('login-sub');
        const lbl = document.getElementById('pwr-lbl');
        const card = document.querySelector('.login-card-wrapper');
        
        if (toggle) {
            toggle.addEventListener('change', (e) => {
                if (e.target.checked) {
                    document.body.classList.add('portal-powered');
                    logo.classList.remove('logo-dimmed');
                    logo.classList.add('logo-powered');
                    if(sub) sub.style.color = '#94a3b8';
                    if(lbl) {
                        lbl.style.color = '#10b981';
                        lbl.style.textShadow = '0 0 10px rgba(16, 185, 129, 0.5)';
                    }
                    if(card) {
                        card.classList.add('card-visible');
                    }
                } else {
                    document.body.classList.remove('portal-powered');
                    logo.classList.add('logo-dimmed');
                    logo.classList.remove('logo-powered');
                    if(sub) sub.style.color = '#64748b';
                    if(lbl) {
                        lbl.style.color = '#64748b';
                        lbl.style.textShadow = 'none';
                    }
                    if(card) {
                        card.classList.remove('card-visible');
                    }
                }
            });
        }
    }, 200);
    </script>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="login-card-wrapper">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.8, 1])
    with col2:
        st.markdown('<div class="login-card" style="padding: 30px;">', unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; margin-bottom: 25px; color: #f8fafc; font-weight: 700;'>Yönetici Paneli Girişi</h3>", unsafe_allow_html=True)
        password = st.text_input("Giriş Şifresi", type="password", key="login_pwd_input", label_visibility="collapsed")
        st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
        if st.button("Sisteme Giriş Yap 🔐", use_container_width=True):
            if password == "12345":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("❌ Hatalı şifre! Lütfen tekrar deneyin.")
        st.markdown("""
        <p style="text-align: center; color: #64748b; font-size: 13px; margin: 15px 0 0 0;">
            🔑 Şifre İpucu: <strong>12345</strong>
        </p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

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