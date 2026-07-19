import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from components.plotly_theme import apply_plotly_theme

def render_nps_league_page(df_synthetic):
    st.markdown("""
    <div style="margin-bottom: 25px;">
        <h1 class="animated-gradient-text" style="font-size: 34px; font-weight: 800; margin: 0;">⭐ Net Promoter Score (NPS) & Müşteri Bağlılık Ligi</h1>
        <p style="color: #94a3b8; margin: 5px 0 0 0; font-size: 15px;">Tavsiye skorları (NPS), en sadık müşteriler sıralaması ve rozet ödülleri</p>
    </div>
    """, unsafe_allow_html=True)
    
    col_n1, col_n2, col_n3 = st.columns(3)
    with col_n1:
        st.markdown("""
        <div class="kpi-card green">
            <div class="kpi-title">Genel NPS Skoru</div>
            <div class="kpi-value">+52 NPS</div>
        </div>
        """, unsafe_allow_html=True)
    with col_n2:
        st.markdown("""
        <div class="kpi-card blue">
            <div class="kpi-title">Promoter (Tavsiye Eden) Oranı</div>
            <div class="kpi-value">%64.2</div>
        </div>
        """, unsafe_allow_html=True)
    with col_n3:
        st.markdown("""
        <div class="kpi-card red">
            <div class="kpi-title">Detractor (Kötüleyen) Oranı</div>
            <div class="kpi-value">%12.2</div>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.markdown("<h4 style='color: #f8fafc; margin-bottom: 15px;'>👑 En Sadık Müşteriler Liderlik Tablosu (Top 5 Loyal Champions)</h4>", unsafe_allow_html=True)
    
    top_loyal = df_synthetic.sort_values(by=['Tenure', 'CashbackAmount'], ascending=False).head(5).copy()
    top_loyal['Rozet'] = ["👑 Şampiyon VIP", "💎 Elmas Sadakat", "🥇 Altın Üye", "🥇 Altın Üye", "🥈 Gümüş Üye"]
    top_loyal['ToplamHarcamaTahmini'] = top_loyal['OrderCount'] * top_loyal['CashbackAmount'] * 2.5
    
    st.dataframe(top_loyal[['Tenure', 'OrderCount', 'CashbackAmount', 'ToplamHarcamaTahmini', 'Rozet']], use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
