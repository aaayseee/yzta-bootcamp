import requests
import streamlit as st
import pandas as pd
import plotly.express as px
from components.plotly_theme import apply_plotly_theme
from data_loader import save_to_history

def render_customer_analysis_page(df_synthetic):
    st.markdown("""
    <div style="margin-bottom: 25px;">
        <h1 class="animated-gradient-text" style="font-size: 34px; font-weight: 800; margin: 0;">🔍 Bireysel Müşteri Churn Analiz & Tahmin Paneli</h1>
        <p style="color: #94a3b8; margin: 5px 0 0 0; font-size: 15px;">Seçilen veya girilen müşteri parametrelerine göre AI modeliyle anlık kayıp riski tahmini</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.markdown("<h4 style='color: #f8fafc; margin-bottom: 15px;'>Müşteri Parametreleri (Girdiler)</h4>", unsafe_allow_html=True)
    
    selected_customer_id = st.selectbox(
        "⚡ Sentez Veri Setinden Hazır Müşteri Seç (Opsiyonel):",
        options=["Manuel Giriş Yap"] + [f"Müşteri #{i+1} (Tenure: {row['Tenure']} ay, Şikayet: {'Var' if row['Complain']==1 else 'Yok'})" for i, row in df_synthetic.head(30).iterrows()]
    )
    
    default_vals = {
        "Tenure": 12.0, "PreferredLoginDevice": "Mobile Phone", "CityTier": 1,
        "WarehouseToHome": 15.0, "PreferredPaymentMode": "Debit Card", "Gender": "Female",
        "HourSpendOnApp": 3.0, "NumberOfDeviceRegistered": 3, "PreferedOrderCat": "Laptop & Accessory",
        "SatisfactionScore": 3, "MaritalStatus": "Single", "NumberOfAddress": 2,
        "Complain": 0, "OrderAmountHikeFromlastYear": 15.0, "CouponUsed": 1,
        "OrderCount": 2, "DaySinceLastOrder": 5.0, "CashbackAmount": 160.0
    }
    
    if selected_customer_id != "Manuel Giriş Yap":
        idx = int(selected_customer_id.split("#")[1].split(" ")[0]) - 1
        row = df_synthetic.iloc[idx]
        for k in default_vals.keys():
            if k in row:
                default_vals[k] = row[k]

    col_a, col_b, col_c = st.columns(3)
    
    with col_a:
        tenure = st.number_input("Tenure (Üyelik Süresi - Ay)", min_value=0.0, max_value=100.0, value=float(default_vals["Tenure"]))
        login_device = st.selectbox("Giriş Cihazı", ["Mobile Phone", "Computer", "Phone"], index=["Mobile Phone", "Computer", "Phone"].index(default_vals["PreferredLoginDevice"]) if default_vals["PreferredLoginDevice"] in ["Mobile Phone", "Computer", "Phone"] else 0)
        city_tier = st.selectbox("Şehir Tier", [1, 2, 3], index=[1, 2, 3].index(int(default_vals["CityTier"])) if int(default_vals["CityTier"]) in [1, 2, 3] else 0)
        warehouse_dist = st.number_input("Depo-Ev Mesafesi (km)", min_value=0.0, max_value=200.0, value=float(default_vals["WarehouseToHome"]))
        payment_mode = st.selectbox("Ödeme Yöntemi", ["Debit Card", "Credit Card", "E wallet", "UPI", "Cash on Delivery"], index=["Debit Card", "Credit Card", "E wallet", "UPI", "Cash on Delivery"].index(default_vals["PreferredPaymentMode"]) if default_vals["PreferredPaymentMode"] in ["Debit Card", "Credit Card", "E wallet", "UPI", "Cash on Delivery"] else 0)
        gender = st.selectbox("Cinsiyet", ["Female", "Male"], index=["Female", "Male"].index(default_vals["Gender"]) if default_vals["Gender"] in ["Female", "Male"] else 0)

    with col_b:
        hours_app = st.number_input("Uygulamada Geçirilen Saat", min_value=0.0, max_value=24.0, value=float(default_vals["HourSpendOnApp"]))
        devices = st.number_input("Kayıtlı Cihaz Sayısı", min_value=1, max_value=10, value=int(default_vals["NumberOfDeviceRegistered"]))
        order_cat = st.selectbox("Tercih Edilen Kategori", ["Laptop & Accessory", "Mobile Phone", "Fashion", "Grocery", "Others"], index=["Laptop & Accessory", "Mobile Phone", "Fashion", "Grocery", "Others"].index(default_vals["PreferedOrderCat"]) if default_vals["PreferedOrderCat"] in ["Laptop & Accessory", "Mobile Phone", "Fashion", "Grocery", "Others"] else 0)
        satisfaction = st.slider("Memnuniyet Skoru (1-5)", 1, 5, int(default_vals["SatisfactionScore"]))
        marital = st.selectbox("Medeni Durum", ["Single", "Married", "Divorced"], index=["Single", "Married", "Divorced"].index(default_vals["MaritalStatus"]) if default_vals["MaritalStatus"] in ["Single", "Married", "Divorced"] else 0)
        addresses = st.number_input("Adres Sayısı", min_value=1, max_value=20, value=int(default_vals["NumberOfAddress"]))

    with col_c:
        complain = st.selectbox("Şikayet Var mı?", [0, 1], format_func=lambda x: "Evet (1)" if x == 1 else "Hayır (0)", index=int(default_vals["Complain"]))
        hike = st.number_input("Sipariş Tutar Artış Oranı (%)", min_value=0.0, max_value=100.0, value=float(default_vals["OrderAmountHikeFromlastYear"]))
        coupon = st.number_input("Kullanılan Kupon Sayısı", min_value=0, max_value=50, value=int(default_vals["CouponUsed"]))
        order_count = st.number_input("Toplam Sipariş Sayısı", min_value=1, max_value=100, value=int(default_vals["OrderCount"]))
        days_since_last = st.number_input("Son Siparişten Beri Geçen Gün", min_value=0.0, max_value=365.0, value=float(default_vals["DaySinceLastOrder"]))
        cashback = st.number_input("Kazanılan Cashback (₺)", min_value=0.0, max_value=1000.0, value=float(default_vals["CashbackAmount"]))

    st.markdown("</div>", unsafe_allow_html=True)
    
    predict_btn = st.button("🚀 Churn Riskini Tahmin Et", use_container_width=True)
    
    if predict_btn:
        payload = {
            "Tenure": tenure, "PreferredLoginDevice": login_device, "CityTier": city_tier,
            "WarehouseToHome": warehouse_dist, "PreferredPaymentMode": payment_mode, "Gender": gender,
            "HourSpendOnApp": hours_app, "NumberOfDeviceRegistered": devices, "PreferedOrderCat": order_cat,
            "SatisfactionScore": satisfaction, "MaritalStatus": marital, "NumberOfAddress": addresses,
            "Complain": complain, "OrderAmountHikeFromlastYear": hike, "CouponUsed": coupon,
            "OrderCount": order_count, "DaySinceLastOrder": days_since_last, "CashbackAmount": cashback
        }
        
        with st.spinner("AI Modeli Tahmin Yapıyor..."):
            try:
                response = requests.post("http://127.0.0.1:8000/predict", json=payload, timeout=5)
                if response.status_code == 200:
                    res = response.json()
                    prob = res["churn_probability"] * 100
                    prediction = res["churn_prediction"]
                    
                    risk_status = "YÜKSEK CHURN RİSKİ (Kayıp Olabilir)" if prediction == 1 else "DÜŞÜK CHURN RİSKİ (Sadık Müşteri)"
                    action = "Özel İndirim Kuponu & VIP Müşteri Temsilcisi Ataması" if prediction == 1 else "Sadakat Puanı & Standart Kampanya Bildirimi"
                    
                    target_cust = selected_customer_id if selected_customer_id != "Manuel Giriş Yap" else "Manuel Test Müşterisi"
                    save_to_history(target_cust, risk_status, prob, tenure, complain, action)
                    
                    card_class = "risk" if prediction == 1 else "loyal"
                    icon = "🚨" if prediction == 1 else "✅"
                    
                    st.markdown(f"""
                    <div class="result-card {card_class}">
                        <h3 style="margin: 0 0 10px 0; display: flex; align-items: center; gap: 10px;">
                            <span>{icon}</span> {risk_status}
                        </h3>
                        <p style="font-size: 18px; margin: 5px 0;">Tahmin Edilen Churn İhtimali: <strong>%{prob:.1f}</strong></p>
                        <p style="font-size: 15px; margin: 10px 0 0 0; opacity: 0.9;"><strong>Önerilen Aksiyon:</strong> {action}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    fig_gauge = px.pie(
                        values=[prob, 100 - prob], 
                        names=['Kayıp Riski', 'Güvenli Bölge'],
                        hole=0.7,
                        color_discrete_sequence=['#ef4444' if prediction == 1 else '#10b981', '#1e293b']
                    )
                    fig_gauge.update_layout(title="Müşteri Churn Risk Göstergesi")
                    st.plotly_chart(apply_plotly_theme(fig_gauge), use_container_width=True)
                    
                else:
                    st.error(f"Backend Hata Döndürdü: Status Code {response.status_code}")
            except Exception as e:
                st.error(f"FastAPI Sunucusuna Ulaşılamadı (main.py çalışıyor mu?): {e}")
