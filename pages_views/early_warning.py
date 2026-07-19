import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from components.plotly_theme import apply_plotly_theme

def render_early_warning_page(df_synthetic):
    st.markdown("""
    <div style="margin-bottom: 25px;">
        <h1 class="animated-gradient-text" style="font-size: 34px; font-weight: 800; margin: 0;">🚨 Erken Uyarı & Otomatik Aksiyon Merkezi</h1>
        <p style="color: #94a3b8; margin: 5px 0 0 0; font-size: 15px;">Yüksek riskli müşterilerin anlık radar takibi ve otomatik müdahale senaryoları</p>
    </div>
    """, unsafe_allow_html=True)
    
    high_risk_df = df_synthetic[df_synthetic['Churn'] == 1].copy()
    high_risk_df['RiskSkoru'] = np.random.uniform(70, 98, len(high_risk_df)).round(1)
    high_risk_df['ÖnerilenMüdahale'] = np.random.choice([
        "VIP Müşteri Temsilcisi Araması",
        "₺150 Özel Alışveriş Çeki",
        "Ücretsiz Kargo & Hızlı İade Daveti",
        "Kişiselleştirilmiş İndirim Kodu"
    ], len(high_risk_df))
    
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.markdown(f"<h4 style='color: #f8fafc;'>Yüksek Risk Altındaki Müşteri Listesi ({len(high_risk_df)} Müşteri Bulundu)</h4>", unsafe_allow_html=True)
    
    st.dataframe(high_risk_df[['Tenure', 'Complain', 'DaySinceLastOrder', 'SatisfactionScore', 'RiskSkoru', 'ÖnerilenMüdahale']].head(15), use_container_width=True)
    
    col_act1, col_act2 = st.columns(2)
    with col_act1:
        st.markdown('<div class="result-card risk">', unsafe_allow_html=True)
        st.markdown("<h4>⚡ Toplu Aksiyon Tetikle</h4>", unsafe_allow_html=True)
        selected_campaign = st.selectbox("Gönderilecek Kampanya Tipi", [
            "Tüm Yüksek Riskli Müşterilere %20 İndirim SMS'i Gönder",
            "Şikayeti Olan Müşterilere VIP Destek Bileti Aç",
            "30 Gündür Sipariş Vermeyenlere ₺100 Cashback Tanımla"
        ])
        if st.button("🚀 Kampanyayı Hemen Başlat", use_container_width=True):
            st.success(f"✅ Otomatik Aksiyon Başlatıldı: {selected_campaign} ({len(high_risk_df)} Müşteriye İletildi)")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col_act2:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        fig_radar = px.scatter(
            high_risk_df,
            x='RiskSkoru',
            y='DaySinceLastOrder',
            size='Tenure',
            color='RiskSkoru',
            title='Risk Skoru vs Son Sipariş Aralığı Radar Matrisi',
            color_continuous_scale='Reds'
        )
        st.plotly_chart(apply_plotly_theme(fig_radar), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
