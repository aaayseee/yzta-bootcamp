import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from components.plotly_theme import apply_plotly_theme

def render_cohort_page(df_synthetic):
    st.markdown("""
    <div style="margin-bottom: 25px;">
        <h1 class="animated-gradient-text" style="font-size: 34px; font-weight: 800; margin: 0;">📈 Kohort Analizi & Müşteri Yaşam Boyu Değeri (LTV)</h1>
        <p style="color: #94a3b8; margin: 5px 0 0 0; font-size: 15px;">Katılım dönemlerine göre müşteri tutundurma oranları (Retention) ve LTV/CAC değerleri</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Generate Synthetic Cohort Heatmap Matrix
    months = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran']
    cohort_data = []
    for i, m in enumerate(months):
        row = [100.0]
        curr = 100.0
        for j in range(1, 6 - i):
            drop = np.random.uniform(3, 12)
            curr -= drop
            row.append(round(max(curr, 20.0), 1))
        cohort_data.append(row)
        
    cohort_df = pd.DataFrame(cohort_data, index=months, columns=[f'Ay {k}' for k in range(0, 6)])
    
    col_c1, col_c2 = st.columns([2, 1])
    with col_c1:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        fig_heat = px.imshow(
            cohort_df,
            labels=dict(x="Katılım Ayı Sonrası Süre", y="Müşteri Katılım Kohortu", color="Tutundurma %"),
            x=[f'Ay {k}' for k in range(0, 6)],
            y=months,
            color_continuous_scale='Viridis',
            text_auto=True,
            title="Aylık Müşteri Tutundurma (Retention Rate) Kohort Matrisi"
        )
        st.plotly_chart(apply_plotly_theme(fig_heat), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col_c2:
        st.markdown("""
        <div class="result-card loyal" style="margin-top: 0;">
            <h4 style="margin: 0 0 10px 0;">💎 LTV & CAC Finansal Özeti</h4>
            <p style="font-size: 14px; margin: 5px 0;">Ort. Yaşam Boyu Değer (LTV): <strong>₺4,850</strong></p>
            <p style="font-size: 14px; margin: 5px 0;">Ort. Edinme Maliyeti (CAC): <strong>₺1,120</strong></p>

            <p style="font-size: 14px; margin: 5px 0;">LTV / CAC Oranı: <strong>4.33x</strong> (Çok Sağlıklı)</p>
            <hr style="border-color: rgba(255,255,255,0.1); margin: 10px 0;">
            <p style="font-size: 12px; opacity: 0.8;">3. ay sonrasındaki müşteri tutundurma oranlarında %4.2 artış kaydedildi.</p>
        </div>
        """, unsafe_allow_html=True)
