import os
import streamlit as st
import pandas as pd
from data_loader import get_prediction_history

def render_history_page():
    st.markdown("""
    <div style="margin-bottom: 25px;">
        <h1 class="animated-gradient-text" style="font-size: 34px; font-weight: 800; margin: 0;">📋 Geçmiş Churn Tahmin Kayıtları</h1>
        <p style="color: #94a3b8; margin: 5px 0 0 0; font-size: 15px;">Sistem üzerinden yapılan tüm canlı müşteri sorgularının ve aksiyon önerilerinin denetim günlüğü</p>
    </div>
    """, unsafe_allow_html=True)
    
    df_hist = get_prediction_history()
    
    if len(df_hist) > 0:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.dataframe(df_hist, use_container_width=True)
        
        col_dl1, col_dl2 = st.columns([1, 4])
        with col_dl1:
            csv_data = df_hist.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 CSV Olarak İndir",
                data=csv_data,
                file_name="loyalcart_churn_tahmin_gecmisi.csv",
                mime="text/csv",
                use_container_width=True
            )
        with col_dl2:
            if st.button("🗑️ Geçmişi Temizle"):
                if os.path.exists("tahmin_gecmisi.csv"):
                    os.remove("tahmin_gecmisi.csv")
                st.success("Tahmin geçmişi başarıyla temizlendi.")
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("ℹ️ Henüz kaydedilmiş bir Churn tahmini bulunmuyor. 'Müşteri Analiz Paneli' sekmesinden ilk tahmininizi gerçekleştirebilirsiniz.")
