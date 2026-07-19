import os
import pandas as pd
import numpy as np
import streamlit as st

@st.cache_data
def get_synthetic_data():
    file_path = "sentez_veri.csv"
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    
    np.random.seed(42)
    n = 200
    
    tenures = np.random.exponential(11.5, n).round(1)
    tenures = np.clip(tenures, 0, 45)
    
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
        "CashbackAmount": np.random.normal(165, 45, n).round(1).clip(0, 320)
    }
    df = pd.DataFrame(data)
    
    try:
        import joblib
        model = joblib.load("churn_modeli.pkl")
        raw_df = df.copy()
        df_encoded = pd.get_dummies(raw_df)
        
        if hasattr(model, "feature_names_in_"):
            missing_cols = set(model.feature_names_in_) - set(df_encoded.columns)
            for c in missing_cols:
                df_encoded[c] = 0
            df_encoded = df_encoded[model.feature_names_in_]
            
        preds = model.predict(df_encoded)
        df["Churn"] = preds
    except Exception:
        churn_prob = (
            (df['Tenure'] < 6).astype(int) * 0.35 +
            (df['Complain'] == 1).astype(int) * 0.35 +
            (df['DaySinceLastOrder'] > 10).astype(int) * 0.20 +
            (df['SatisfactionScore'] <= 2).astype(int) * 0.20
        )
        df['Churn'] = (churn_prob > 0.40).astype(int)
        
    return df


def get_prediction_history():
    hist_path = "tahmin_gecmisi.csv"
    if os.path.exists(hist_path):
        return pd.read_csv(hist_path)
    return pd.DataFrame(columns=["Tarih", "Müşteri ID", "Sonuç", "Risk İhtimali", "Tenure (Ay)", "Şikayet Durumu", "Önerilen Aksiyon"])


def save_to_history(id_val, pred_result, prob_val, tenure_val, complain_val, action_val):
    hist_path = "tahmin_gecmisi.csv"
    new_entry = {
        "Tarih": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Müşteri ID": id_val,
        "Sonuç": pred_result,
        "Risk İhtimali": f"%{prob_val:.1f}",
        "Tenure (Ay)": tenure_val,
        "Şikayet Durumu": "Var" if complain_val == 1 else "Yok",
        "Önerilen Aksiyon": action_val
    }
    if os.path.exists(hist_path):
        df_hist = pd.read_csv(hist_path)
        df_hist = pd.concat([pd.DataFrame([new_entry]), df_hist], ignore_index=True)
    else:
        df_hist = pd.DataFrame([new_entry])
    df_hist.to_csv(hist_path, index=False)
