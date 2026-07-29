import streamlit as st


def render_sidebar():
    with st.sidebar:
        st.markdown(
            """
            <div style="display:flex;align-items:center;margin-bottom:25px;padding-left:5px">
              <span style="font-weight:800;font-size:26px;color:#f8fafc">
                L<span style="background:linear-gradient(135deg,#10b981,#0ea5e9);
                  width:26px;height:26px;border-radius:50%;display:inline-flex;
                  align-items:center;justify-content:center;font-size:14px">🛒</span>yalCart
              </span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        role = st.session_state.get("role", "viewer")
        username = st.session_state.get("username", "Kullanıcı")
        st.caption(f"{username} · {role}")

        menu_options = [
            "📊 Genel Durum (Dashboard)",
            "🔮 Churn Simülasyonu (What-If)",
            "🚨 Erken Uyarı & Aksiyon Merkezi",
            "📈 Kohort Analiz Raporu",
            "💬 Şikayet & Bilet Yönetimi",
            "⭐ NPS & Müşteri Bağlılık Ligi",
            "🔍 Müşteri Analiz Paneli",
            "👥 Müşteri Segmentasyonu",
            "📋 Geçmiş Tahmin Kayıtları",
        ]
        if role == "administrator":
            menu_options.append("🔌 Sistem Entegrasyonları")

        active_menu = st.session_state.get("active_menu")
        default_index = (
            menu_options.index(active_menu) if active_menu in menu_options else 0
        )
        selected_menu = st.radio(
            "Gezinme Menüsü",
            menu_options,
            index=default_index,
            key="main_sidebar_radio",
        )
        st.session_state.active_menu = selected_menu

        st.markdown("---")
        if st.button("🚪 Çıkış Yap", use_container_width=True, key="logout_btn"):
            for key in ("logged_in", "username", "role", "active_menu"):
                st.session_state.pop(key, None)
            st.rerun()

        st.markdown("---")
        st.markdown(
            """
            <div style="font-size:12px;color:#64748b;text-align:center">
              L🛒yalCart v3.0<br>© 2026 LoyalCart AI Core
            </div>
            """,
            unsafe_allow_html=True,
        )
        return selected_menu
