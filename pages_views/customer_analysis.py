import os

import pandas as pd
import plotly.express as px
import requests
import streamlit as st

from components.plotly_theme import apply_plotly_theme
from db.repository import save_prediction
from prediction_service import predict_churn


def render_customer_analysis_page(df_synthetic):
    st.markdown(
        """
        <div style="margin-bottom:25px">
          <h1 class="animated-gradient-text"
            style="font-size:34px;font-weight:800;margin:0">
            🔍 Bireysel Müşteri Churn Analiz & Tahmin Paneli
          </h1>
          <p style="color:#94a3b8;margin:5px 0 0;font-size:15px">
            Müşteri parametrelerine göre anlık kayıp riski tahmini
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    customer_options = ["Manuel Giriş Yap"] + [
        f"Müşteri #{index + 1}" for index in range(min(30, len(df_synthetic)))
    ]
    selected_customer = st.selectbox(
        "Sentez veri setinden müşteri seçin", customer_options
    )
    customer_id = (
        st.text_input("Müşteri ID", value="MANUEL")
        if selected_customer == "Manuel Giriş Yap"
        else selected_customer
    )

    defaults = {
        "Tenure": 12.0,
        "PreferredLoginDevice": "Mobile Phone",
        "CityTier": 1,
        "WarehouseToHome": 15.0,
        "PreferredPaymentMode": "Debit Card",
        "Gender": "Female",
        "HourSpendOnApp": 3.0,
        "NumberOfDeviceRegistered": 3,
        "PreferedOrderCat": "Laptop & Accessory",
        "SatisfactionScore": 3,
        "MaritalStatus": "Single",
        "NumberOfAddress": 2,
        "Complain": 0,
        "OrderAmountHikeFromlastYear": 15.0,
        "CouponUsed": 1,
        "OrderCount": 2,
        "DaySinceLastOrder": 5.0,
        "CashbackAmount": 160.0,
    }
    if selected_customer != "Manuel Giriş Yap":
        row = df_synthetic.iloc[int(selected_customer.split("#")[1]) - 1]
        for key in defaults:
            if key in row:
                defaults[key] = row[key]

    first, second, third = st.columns(3)
    with first:
        tenure = st.number_input("Tenure (Ay)", 0.0, 100.0, float(defaults["Tenure"]))
        login_device = st.selectbox(
            "Giriş Cihazı",
            ["Mobile Phone", "Computer", "Phone"],
            index=["Mobile Phone", "Computer", "Phone"].index(
                defaults["PreferredLoginDevice"]
            ),
        )
        city_tier = st.selectbox(
            "Şehir Tier", [1, 2, 3], index=int(defaults["CityTier"]) - 1
        )
        warehouse_distance = st.number_input(
            "Depo-Ev Mesafesi", 0.0, 200.0, float(defaults["WarehouseToHome"])
        )
        payment_mode = st.selectbox(
            "Ödeme Yöntemi",
            ["Debit Card", "Credit Card", "E wallet", "UPI", "Cash on Delivery"],
        )
        gender = st.selectbox("Cinsiyet", ["Female", "Male"])
    with second:
        hours_on_app = st.number_input(
            "Uygulamada Geçirilen Saat",
            0.0,
            24.0,
            float(defaults["HourSpendOnApp"]),
        )
        devices = st.number_input(
            "Kayıtlı Cihaz Sayısı",
            1,
            10,
            int(defaults["NumberOfDeviceRegistered"]),
        )
        order_category = st.selectbox(
            "Tercih Edilen Kategori",
            ["Laptop & Accessory", "Mobile Phone", "Fashion", "Grocery", "Others"],
        )
        satisfaction = st.slider(
            "Memnuniyet Skoru", 1, 5, int(defaults["SatisfactionScore"])
        )
        marital_status = st.selectbox(
            "Medeni Durum", ["Single", "Married", "Divorced"]
        )
        addresses = st.number_input(
            "Adres Sayısı", 1, 20, int(defaults["NumberOfAddress"])
        )
    with third:
        complain = st.selectbox(
            "Şikayet Var mı?",
            [0, 1],
            index=int(defaults["Complain"]),
            format_func=lambda value: "Evet" if value else "Hayır",
        )
        order_hike = st.number_input(
            "Sipariş Tutar Artış Oranı",
            0.0,
            100.0,
            float(defaults["OrderAmountHikeFromlastYear"]),
        )
        coupons = st.number_input(
            "Kullanılan Kupon", 0, 50, int(defaults["CouponUsed"])
        )
        order_count = st.number_input(
            "Toplam Sipariş", 1, 100, int(defaults["OrderCount"])
        )
        days_since_last = st.number_input(
            "Son Siparişten Beri Geçen Gün",
            0.0,
            365.0,
            float(defaults["DaySinceLastOrder"]),
        )
        cashback = st.number_input(
            "Cashback", 0.0, 1000.0, float(defaults["CashbackAmount"])
        )

    if not st.button("🚀 Churn Riskini Tahmin Et", use_container_width=True):
        return

    features = {
        "Tenure": tenure,
        "PreferredLoginDevice": login_device,
        "CityTier": city_tier,
        "WarehouseToHome": warehouse_distance,
        "PreferredPaymentMode": payment_mode,
        "Gender": gender,
        "HourSpendOnApp": hours_on_app,
        "NumberOfDeviceRegistered": devices,
        "PreferedOrderCat": order_category,
        "SatisfactionScore": satisfaction,
        "MaritalStatus": marital_status,
        "NumberOfAddress": addresses,
        "Complain": complain,
        "OrderAmountHikeFromlastYear": order_hike,
        "CouponUsed": coupons,
        "OrderCount": order_count,
        "DaySinceLastOrder": days_since_last,
        "CashbackAmount": cashback,
    }
    api_payload = {
        **features,
        "CustomerId": customer_id,
        "CreatedBy": st.session_state.get("username"),
    }

    outcome = None
    source = "api"
    api_url = os.getenv("LOYALCART_API_URL", "http://127.0.0.1:8000").rstrip("/")
    api_key = os.getenv("LOYALCART_API_KEY")
    headers = {"X-API-Key": api_key} if api_key else {}
    with st.spinner("AI modeli tahmin yapıyor..."):
        try:
            response = requests.post(
                f"{api_url}/predict", json=api_payload, headers=headers, timeout=3
            )
            response.raise_for_status()
            result = response.json()
            outcome = {
                "prediction": int(result["churn_prediction"]),
                "probability": float(result["churn_probability"]),
                "result": result["Tahmin_Sonucu"],
                "action": result["Aksiyon"],
                "model_version": result.get("model_version"),
            }
        except (requests.RequestException, KeyError, TypeError, ValueError):
            source = "streamlit-fallback"
            try:
                outcome = predict_churn(features)
                save_prediction(
                    customer_id=customer_id,
                    features=features,
                    prediction=outcome["prediction"],
                    probability=outcome["probability"],
                    model_version=outcome["model_version"],
                    result=outcome["result"],
                    action=outcome["action"],
                    source=source,
                    created_by=st.session_state.get("username"),
                )
            except Exception as exc:
                st.error(f"Tahmin oluşturulamadı: {exc}")
                return

    probability_percent = outcome["probability"] * 100
    card_class = "risk" if outcome["prediction"] == 1 else "loyal"
    icon = "🚨" if outcome["prediction"] == 1 else "✅"
    st.markdown(
        f"""
        <div class="result-card {card_class}">
          <h3>{icon} {outcome["result"]}</h3>
          <p>Tahmin edilen churn ihtimali:
            <strong>%{probability_percent:.1f}</strong></p>
          <p><strong>Önerilen aksiyon:</strong> {outcome["action"]}</p>
          <small>Tahmin kaynağı: {source}</small>
        </div>
        """,
        unsafe_allow_html=True,
    )
    gauge = px.pie(
        values=[probability_percent, 100 - probability_percent],
        names=["Kayıp Riski", "Güvenli Bölge"],
        hole=0.7,
        color_discrete_sequence=[
            "#ef4444" if outcome["prediction"] == 1 else "#10b981",
            "#1e293b",
        ],
    )
    gauge.update_layout(title="Müşteri Churn Risk Göstergesi")
    st.plotly_chart(apply_plotly_theme(gauge), use_container_width=True)
