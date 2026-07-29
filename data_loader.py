import json
import os

import numpy as np
import pandas as pd
import streamlit as st

from db.repository import clear_predictions, list_predictions, save_prediction


@st.cache_data
def get_synthetic_data():
    file_path = "sentez_veri.csv"
    if os.path.exists(file_path):
        return pd.read_csv(file_path)

    np.random.seed(42)
    n = 200
    tenures = np.clip(np.random.exponential(11.5, n).round(1), 0, 45)
    data = {
        "Tenure": tenures,
        "PreferredLoginDevice": np.random.choice(["Mobile Phone", "Computer", "Phone"], n, p=[0.60, 0.30, 0.10]),
        "CityTier": np.random.choice([1, 2, 3], n, p=[0.60, 0.10, 0.30]),
        "WarehouseToHome": np.random.gamma(2.5, 6, n).round(1).clip(5, 100),
        "PreferredPaymentMode": np.random.choice(["Debit Card", "Credit Card", "E wallet", "UPI", "Cash on Delivery"], n, p=[0.38, 0.32, 0.15, 0.10, 0.05]),
        "Gender": np.random.choice(["Male", "Female"], n, p=[0.58, 0.42]),
        "HourSpendOnApp": np.random.choice([1, 2, 3, 4, 5], n, p=[0.05, 0.20, 0.45, 0.25, 0.05]).astype(float),
        "NumberOfDeviceRegistered": np.random.choice([1, 2, 3, 4, 5, 6], n, p=[0.05, 0.10, 0.25, 0.35, 0.20, 0.05]),
        "PreferedOrderCat": np.random.choice(["Laptop & Accessory", "Mobile Phone", "Fashion", "Grocery", "Others"], n, p=[0.38, 0.28, 0.15, 0.12, 0.07]),
        "SatisfactionScore": np.random.choice([1, 2, 3, 4, 5], n, p=[0.08, 0.12, 0.40, 0.28, 0.12]),
        "MaritalStatus": np.random.choice(["Single", "Married", "Divorced"], n, p=[0.32, 0.48, 0.20]),
        "NumberOfAddress": np.random.randint(1, 10, n),
        "Complain": np.random.choice([0, 1], n, p=[0.78, 0.22]),
        "OrderAmountHikeFromlastYear": np.random.normal(15, 3, n).round(1).clip(11, 28),
        "CouponUsed": np.random.poisson(1.8, n).clip(0, 10),
        "OrderCount": np.random.poisson(2.8, n).clip(1, 12),
        "DaySinceLastOrder": np.random.exponential(6.5, n).round(1).clip(0, 25),
        "CashbackAmount": np.random.normal(165, 45, n).round(1).clip(0, 320),
    }
    df = pd.DataFrame(data)
    try:
        from prediction_service import predict_churn

        df["Churn"] = [
            predict_churn(row.to_dict())["prediction"] for _, row in df.iterrows()
        ]
    except Exception:
        churn_probability = (
            (df["Tenure"] < 6).astype(int) * 0.35
            + (df["Complain"] == 1).astype(int) * 0.35
            + (df["DaySinceLastOrder"] > 10).astype(int) * 0.20
            + (df["SatisfactionScore"] <= 2).astype(int) * 0.20
        )
        df["Churn"] = (churn_probability > 0.40).astype(int)
    return df


def get_prediction_history():
    rows = []
    for item in list_predictions():
        try:
            features = json.loads(item.get("features") or "{}")
        except (TypeError, json.JSONDecodeError):
            features = {}
        probability = float(item.get("probability") or 0.0)
        rows.append(
            {
                "Tarih": item.get("created_at"),
                "Müşteri ID": item.get("customer_id") or "Belirtilmedi",
                "Sonuç": item.get("result")
                or ("Terk Riski Var" if item.get("prediction") else "Sadık Müşteri"),
                "Risk İhtimali": f"%{probability * 100:.1f}",
                "Tenure (Ay)": features.get("Tenure"),
                "Şikayet Durumu": "Var" if features.get("Complain") == 1 else "Yok",
                "Önerilen Aksiyon": item.get("action") or "-",
                "Kaynak": item.get("source") or "-",
                "İşlemi Yapan": item.get("created_by") or "-",
                "Model": item.get("model_version") or "-",
            }
        )
    return pd.DataFrame(rows)


def save_to_history(
    id_val,
    pred_result,
    prob_val,
    tenure_val,
    complain_val,
    action_val,
    source="streamlit",
    created_by=None,
):
    return save_prediction(
        customer_id=str(id_val),
        features={"Tenure": tenure_val, "Complain": complain_val},
        prediction=1 if "YÜKSEK" in pred_result.upper() else 0,
        probability=float(prob_val) / 100,
        result=pred_result,
        action=action_val,
        source=source,
        created_by=created_by,
    )


def clear_prediction_history():
    clear_predictions()
