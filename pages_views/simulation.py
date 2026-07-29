import streamlit as st
import plotly.express as px
from components.plotly_theme import apply_plotly_theme

def render_simulation_page(df_synthetic):
    st.markdown("""
    <div style="margin-bottom: 25px;">
        <h1 class="animated-gradient-text" style="font-size: 34px; font-weight: 800; margin: 0;">🔮 Churn Simülasyonu (What-If Analizi)</h1>
        <p style="color: #94a3b8; margin: 5px 0 0 0; font-size: 15px;">Şirket stratejilerinin müşteri tutundurma ve ciro üzerindeki finansal etkisini anlık simüle edin</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.markdown("<h4 style='color: #f8fafc;'>Simülasyon Senaryo Parametreleri</h4>", unsafe_allow_html=True)
    
    col_s1, col_s2, col_s3 = st.columns(3)
    with col_s1:
        discount_rate = st.slider("Özel İndirim Kupon Oranı (%)", 0, 50, 15)
        cashback_boost = st.slider("Cashback Artış Miktarı (₺)", 0, 200, 50)
    with col_s2:
        support_speed = st.slider("Şikayet Çözüm Hızı Artışı (%)", 0, 100, 30)
        app_engagement = st.slider("Mobil Uygulama Kampanya Etkileşimi (%)", 0, 100, 20)
    with col_s3:
        target_risk_group = st.selectbox("Hedef Müşteri Grubu", ["Tüm Müşteriler", "Yüksek Riskli Müşteriler (>= 70%)", "Orta Riskli Müşteriler"])
        campaign_budget = st.number_input("Ayırılan Kampanya Bütçesi (₺)", min_value=1000, max_value=500000, value=25000)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Calculate simulation ROI
    base_churn = df_synthetic['Churn'].sum()
    reduced_churn = int(base_churn * (1 - (discount_rate*0.012 + support_speed*0.008 + cashback_boost*0.002)))
    recovered_users = max(0, base_churn - reduced_churn)
    saved_revenue = recovered_users * 1450 # Avg LTV estimate
    net_roi = saved_revenue - campaign_budget
    
    col_r1, col_r2, col_r3, col_r4 = st.columns(4)
    with col_r1:
        st.markdown(f"""
        <div class="kpi-card green">
            <div class="kpi-title">Kurtarılan Müşteri Sayısı</div>
            <div class="kpi-value">+{recovered_users} Kişi</div>
        </div>
        """, unsafe_allow_html=True)
    with col_r2:
        st.markdown(f"""
        <div class="kpi-card blue">
            <div class="kpi-title">Korunan Tahmini Ciro</div>
            <div class="kpi-value">₺{saved_revenue:,.0f}</div>
        </div>
        """, unsafe_allow_html=True)
    with col_r3:
        st.markdown(f"""
        <div class="kpi-card purple">
            <div class="kpi-title">Kampanya Net ROI</div>
            <div class="kpi-value">₺{net_roi:,.0f}</div>
        </div>
        """, unsafe_allow_html=True)
    with col_r4:
        st.markdown(f"""
        <div class="kpi-card orange">
            <div class="kpi-title">Yeni Churn Oranı</div>
            <div class="kpi-value">%{(reduced_churn/len(df_synthetic))*100:.1f}</div>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    fig_sim = px.bar(
        x=["Mevcut Durum Churn", "Simülasyon Sonrası Churn"],
        y=[base_churn, reduced_churn],
        color=["Mevcut", "Hedef"],
        title="Simülasyon Öncesi ve Sonrası Churn Karşılaştırması",
        color_discrete_map={"Mevcut": "#ef4444", "Hedef": "#10b981"}
    )
    st.plotly_chart(apply_plotly_theme(fig_sim), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
