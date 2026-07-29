import streamlit as st

from data_loader import clear_prediction_history, get_prediction_history


def render_history_page():
    st.markdown(
        """
        <div style="margin-bottom:25px">
          <h1 class="animated-gradient-text"
            style="font-size:34px;font-weight:800;margin:0">
            📋 Geçmiş Churn Tahmin Kayıtları
          </h1>
          <p style="color:#94a3b8;margin:5px 0 0;font-size:15px">
            Veritabanında tutulan canlı müşteri sorguları ve aksiyon önerileri
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    history = get_prediction_history()
    if history.empty:
        st.info(
            "Henüz kaydedilmiş bir Churn tahmini bulunmuyor. "
            "Müşteri Analiz Paneli'nden ilk tahmini oluşturabilirsiniz."
        )
        return

    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.dataframe(history, use_container_width=True)
    download_column, clear_column = st.columns([1, 4])
    with download_column:
        st.download_button(
            label="📥 CSV Olarak İndir",
            data=history.to_csv(index=False).encode("utf-8"),
            file_name="loyalcart_churn_tahmin_gecmisi.csv",
            mime="text/csv",
            use_container_width=True,
        )
    with clear_column:
        if st.button("🗑️ Geçmişi Temizle"):
            if st.session_state.get("role") != "administrator":
                st.error("Bu işlem için administrator rolü gerekir.")
            else:
                clear_prediction_history()
                st.success("Tahmin geçmişi temizlendi.")
                st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
