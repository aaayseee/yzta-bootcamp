import streamlit as st
import plotly.express as px
from components.plotly_theme import apply_plotly_theme

def render_dashboard_page(df_synthetic):
    st.markdown("""
    <div style="margin-bottom: 25px;">
        <h1 class="animated-gradient-text" style="font-size: 38px; font-weight: 800; margin: 0; letter-spacing: -0.5px;">Yönetici Churn Analiz Paneli</h1>
        <p style="color: #94a3b8; margin: 5px 0 0 0; font-size: 15px;">Müşteri sadakat metrikleri, kayıp riskleri ve genel performans göstergeleri</p>
    </div>
    """, unsafe_allow_html=True)
    
    total_customers = len(df_synthetic)
    churned_customers = df_synthetic['Churn'].sum()
    churn_rate = (churned_customers / total_customers) * 100
    complain_rate = (df_synthetic['Complain'].sum() / total_customers) * 100
    avg_sat = df_synthetic['SatisfactionScore'].mean()
    
    # KPI Kartları (Green and Blue themed)
    col_kpi1, col_kpi2, col_kpi3, col_kpi4, col_kpi5 = st.columns(5)
    
    with col_kpi1:
        st.markdown(f"""
        <div class="kpi-card blue">
            <div class="kpi-title">Toplam Müşteri</div>
            <div class="kpi-value">{total_customers}</div>
        </div>
        """, unsafe_allow_html=True)
            
    with col_kpi2:
        st.markdown(f"""
        <div class="kpi-card red">
            <div class="kpi-title">Kayıp (Churn) Riski Sayısı</div>
            <div class="kpi-value">{churned_customers}</div>
        </div>
        """, unsafe_allow_html=True)
            
    with col_kpi3:
        st.markdown(f"""
        <div class="kpi-card orange">
            <div class="kpi-title">Genel Churn Oranı</div>
            <div class="kpi-value">%{churn_rate:.1f}</div>
        </div>
        """, unsafe_allow_html=True)
            
    with col_kpi4:
        st.markdown(f"""
        <div class="kpi-card green">
            <div class="kpi-title">Şikayet Oranı</div>
            <div class="kpi-value">%{complain_rate:.1f}</div>
        </div>
        """, unsafe_allow_html=True)
            
    with col_kpi5:
        st.markdown(f"""
        <div class="kpi-card purple">
            <div class="kpi-title">Ort. Memnuniyet Skoru</div>
            <div class="kpi-value">{avg_sat:.2f} / 5.0</div>
        </div>
        """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        fig_pie = px.pie(
            df_synthetic, 
            names='Churn', 
            values=None, 
            title='Müşteri Kayıp Risk Dağılımı',
            color='Churn',
            color_discrete_map={0: '#0ea5e9', 1: '#10b981'},
            hole=0.45
        )
        fig_pie.update_traces(labels=['Sadık Müşteri', 'Kayıp Riski Var'], textinfo='percent+label')
        st.plotly_chart(apply_plotly_theme(fig_pie), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        fig_bar = px.histogram(
            df_synthetic, 
            x='Tenure', 
            color='Churn',
            title='Müşterilik Süresi (Tenure) & Churn İlişkisi',
            labels={'Tenure': 'Tenure (Ay)', 'count': 'Müşteri Sayısı'},
            color_discrete_map={0: '#0ea5e9', 1: '#10b981'},
            barmode='overlay',
            opacity=0.8
        )
        st.plotly_chart(apply_plotly_theme(fig_bar), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.markdown("<h4 style='color: #f8fafc; margin-bottom: 15px;'>Müşteri Segment Veri Özeti</h4>", unsafe_allow_html=True)
    st.dataframe(df_synthetic.head(10), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
