import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.markdown("""
        <div style="display: flex; align-items: center; justify-content: flex-start; margin-bottom: 25px; padding-left: 5px;">
            <span style="font-weight: 800; font-size: 26px; color: #f8fafc; display: inline-flex; align-items: center; gap: 3px; letter-spacing: -0.5px;">
                L<span style="background: linear-gradient(135deg, #10b981 0%, #0ea5e9 100%); width: 26px; height: 26px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 14px; box-shadow: 0 0 10px rgba(16, 185, 129, 0.5); margin: 0 2px; transform: translateY(1px);">🛒</span>yalCart
            </span>
        </div>
        """, unsafe_allow_html=True)
        
        menu_options = [
            "📊 Genel Durum (Dashboard)",
            "🔮 Churn Simülasyonu (What-If)",
            "🚨 Erken Uyarı & Aksiyon Merkezi",
            "📈 Kohort Analiz Raporu",
            "💬 Şikayet & Bilet Yönetimi",
            "⭐ NPS & Müşteri Bağlılık Ligi",
            "🔍 Müşteri Analiz Paneli",
            "👥 Müşteri Segmentasyonu",
            "📋 Geçmiş Tahmin Kayıtları"
        ]
        
        default_index = 0
        if 'active_menu' in st.session_state and st.session_state.active_menu in menu_options:
            default_index = menu_options.index(st.session_state.active_menu)
            
        selected_menu = st.radio(
            "Gezinme Menüsü",
            menu_options,
            index=default_index,
            key="main_sidebar_radio"
        )
        
        st.session_state.active_menu = selected_menu
        
        st.markdown("---")
        st.markdown("""
        <div style="font-size: 12px; color: #64748b; text-align: center;">
            L🛒yalCart v2.5 Executive Pro<br>
            © 2026 LoyalCart AI Core
        </div>
        """, unsafe_allow_html=True)
        
        return selected_menu
