import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from components.plotly_theme import apply_plotly_theme

def render_complaints_page(df_synthetic):
    st.markdown("""
    <div style="margin-bottom: 25px;">
        <h1 class="animated-gradient-text" style="font-size: 34px; font-weight: 800; margin: 0;">💬 Müşteri Şikayet & Destek Bilet Yönetimi</h1>
        <p style="color: #94a3b8; margin: 5px 0 0 0; font-size: 15px;">Şikayetlerin kök neden analizi, SLA çözüm süreleri ve müşteri memnuniyet etkisi</p>
    </div>
    """, unsafe_allow_html=True)
    
    categories = ["Lojistik & Teslimat Gecikmesi", "Hasarlı / Yanlış Ürün", "İade & Ücret İadesi", "Ödeme Adımı Hatası", "Müşteri Hizmetleri İletişim"]
    counts = [42, 28, 19, 11, 8]
    
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        fig_pie_comp = px.pie(
            names=categories,
            values=counts,
            title="Gelen Müşteri Şikayet Kategorileri Dağılımı",
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        st.plotly_chart(apply_plotly_theme(fig_pie_comp), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col_t2:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        sla_df = pd.DataFrame({
            "Kategori": categories,
            "Ort. Çözüm Süresi (Saat)": [14.2, 8.5, 24.0, 4.1, 2.8],
            "Churn Riski Etkisi": ["Yüksek", "Orta", "Çok Yüksek", "Düşük", "Orta"]
        })
        st.markdown("<h4 style='color: #f8fafc;'>SLA & Çözüm Hızı Özeti</h4>", unsafe_allow_html=True)
        st.dataframe(sla_df, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
