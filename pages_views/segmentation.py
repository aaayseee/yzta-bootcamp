import streamlit as st
import plotly.express as px
from components.plotly_theme import apply_plotly_theme

def render_segmentation_page(df_synthetic):
    st.markdown("""
    <div style="margin-bottom: 25px;">
        <h1 class="animated-gradient-text" style="font-size: 34px; font-weight: 800; margin: 0;">👥 Müşteri Segmentasyonu & Davranış Analizi</h1>
        <p style="color: #94a3b8; margin: 5px 0 0 0; font-size: 15px;">Müşteri kitlelerinin davranışsal kırılımları ve churn faktör analizleri</p>
    </div>
    """, unsafe_allow_html=True)
    
    selected_kpi_filter = st.session_state.get('selected_kpi_filter', None)
    if selected_kpi_filter:
        st.info(f"💡 KPI Kartı Filtresi Uygulandı: **{selected_kpi_filter.upper()}** grubu inceleniyor.")
        if st.button("Filtreyi Temizle ✕"):
            st.session_state.selected_kpi_filter = None
            st.rerun()
            
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        fig_cat = px.bar(
            df_synthetic, 
            x='PreferedOrderCat', 
            color='Churn', 
            barmode='group',
            title='Tercih Edilen Kategoriye Göre Churn Dağılımı',
            labels={'PreferedOrderCat': 'Kategori', 'count': 'Müşteri Sayısı'},
            color_discrete_map={0: '#0ea5e9', 1: '#10b981'}
        )
        st.plotly_chart(apply_plotly_theme(fig_cat), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        fig_comp = px.bar(
            df_synthetic, 
            x='Complain', 
            color='Churn', 
            barmode='group',
            title='Şikayet Durumuna Göre Churn Dağılımı',
            labels={'Complain': 'Şikayet (0: Yok, 1: Var)', 'count': 'Müşteri Sayısı'},
            color_discrete_map={0: '#0ea5e9', 1: '#10b981'}
        )
        st.plotly_chart(apply_plotly_theme(fig_comp), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        fig_scatter = px.scatter(
            df_synthetic, 
            x='DaySinceLastOrder', 
            y='CashbackAmount', 
            color='Churn',
            size='HourSpendOnApp',
            title='Son Siparişten Geçen Gün vs Cashback (Balon: Harcanan Saat)',
            color_discrete_map={0: '#0ea5e9', 1: '#10b981'}
        )
        st.plotly_chart(apply_plotly_theme(fig_scatter), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col4:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        fig_box = px.box(
            df_synthetic, 
            x='SatisfactionScore', 
            y='Tenure', 
            color='Churn',
            title='Memnuniyet Skoru & Tenure Kutu Grafiği (BoxPlot)',
            color_discrete_map={0: '#0ea5e9', 1: '#10b981'}
        )
        st.plotly_chart(apply_plotly_theme(fig_box), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
