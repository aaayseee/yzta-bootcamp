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
    st.markdown("""
    <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; margin-top: 80px;">
        <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 10px;">
            <span style="font-weight: 800; font-size: 54px; color: #f8fafc; display: inline-flex; align-items: center; gap: 3px; letter-spacing: -2px;">
                L<span style="background: linear-gradient(135deg, #10b981 0%, #0ea5e9 100%); width: 38px; height: 38px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 20px; box-shadow: 0 0 15px rgba(16, 185, 129, 0.6); margin: 0 2px; transform: translateY(2px);">🛒</span>yalCart
            </span>
        </div>
        <p style="color: #94a3b8; font-size: 16px; margin-bottom: 30px;">E-Ticaret Müşteri Kayıp (Churn) Tahmin ve Segmentasyon Paneli</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1.8, 1])
    with col2:
        st.markdown('<div class="login-card" style="padding: 30px;">', unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; margin-bottom: 25px; color: #f8fafc; font-weight: 700;'>Yönetici Paneli Girişi</h3>", unsafe_allow_html=True)
        password = st.text_input("Giriş Şifresi", type="password", key="login_pwd_input", label_visibility="collapsed")
        st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
        if st.button("Sisteme Giriş Yap 🔐", use_container_width=True):
            if password == "1234":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("❌ Hatalı şifre! Lütfen tekrar deneyin.")
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