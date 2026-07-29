from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import os
import json
import sqlite3
try:
    import mysql.connector
except Exception:
    mysql = None
import sklearn

app = FastAPI()

# Modelini yükle (Dosya yolunun doğru olduğundan emin ol)
model = joblib.load("churn_modeli.pkl")

class MusteriVerisi(BaseModel):
    Tenure: float
    PreferredLoginDevice: str
    CityTier: int
    WarehouseToHome: float
    PreferredPaymentMode: str
    Gender: str
    HourSpendOnApp: float
    NumberOfDeviceRegistered: int
    PreferedOrderCat: str
    SatisfactionScore: int
    MaritalStatus: str
    NumberOfAddress: int
    Complain: int
    OrderAmountHikeFromlastYear: float
    CouponUsed: float
    OrderCount: float
    DaySinceLastOrder: float
    CashbackAmount: float

def aksiyon_onerisi_uret(durum, veri):
    # Basit bir mantıkla öneri üreten "YZ Asistanı"
    if "Terk" in durum:
        if veri["Complain"] == 1:
            return "🚨 Acil Durum: Müşteri şikayetli! 24 saat içinde kişiselleştirilmiş bir özür maili gönderilmeli ve %20 indirim tanımlanmalı."
        else:
            return "📉 Müşteri etkileşimi azalmış. Müşteriye 'Seni özledik' temalı özel bir kampanya göndererek sadakatini artır."
    return "✅ Müşteri Sadık. VIP ayrıcalıkları ve özel tekliflerle bu bağı korumaya devam et."

@app.post("/tahmin_et/")
@app.post("/predict/")
@app.post("/predict")
async def tahmin_et(veri: MusteriVerisi):
    # Convert input to DataFrame
    raw_df = pd.DataFrame([veri.model_dump()])
    
    # One-hot encode categorical features
    df_encoded = pd.get_dummies(raw_df)
    
    # Reindex to match the exact 25 features model expects, filling missing columns with 0
    expected_features = list(model.feature_names_in_)
    df_final = df_encoded.reindex(columns=expected_features, fill_value=0)
    
    # Modelin predict fonksiyonuna veriyi gönder
    tahmin = model.predict(df_final)
    olasilik = float(model.predict_proba(df_final)[0][1])
    sonuc = "Terk Riski Var" if tahmin[0] == 1 else "Sadık Müşteri"

    # Save prediction to database (best-effort)
    try:
        save_prediction(
            customer_id=None,
            features=veri.model_dump(),
            prediction=int(tahmin[0]),
            probability=olasilik,
            model_version=getattr(model, 'version', f"sklearn-{sklearn.__version__}")
        )
    except Exception as e:
        # Don't fail the API if DB save fails
        print(f"Warning: failed to save prediction to DB: {e}")
    
    return {
        "Tahmin_Sonucu": sonuc,
        "Olasilik": olasilik,
        "Aksiyon": aksiyon_onerisi_uret(sonuc, veri.model_dump()),
        "churn_prediction": int(tahmin[0]),
        "churn_probability": olasilik
    }


DB_ENGINE = os.getenv('DB_ENGINE', os.getenv('USE_SQLITE', '1') == '1' and 'sqlite' or 'sqlite')


def _get_mysql_conn():
    if mysql is None:
        raise RuntimeError("mysql-connector-python not installed")
    host = os.getenv('MYSQL_HOST', '127.0.0.1')
    port = int(os.getenv('MYSQL_PORT', '3306'))
    user = os.getenv('MYSQL_USER', 'root')
    password = os.getenv('MYSQL_PASSWORD', '')
    database = os.getenv('MYSQL_DB', 'loyalcart')
    conn = mysql.connector.connect(host=host, port=port, user=user, password=password, database=database)
    return conn


def _get_sqlite_conn():
    db_path = os.getenv('SQLITE_PATH', 'loyalcart.db')
    conn = sqlite3.connect(db_path, check_same_thread=False)
    return conn


def _ensure_sqlite_table():
    conn = _get_sqlite_conn()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          customer_id TEXT,
          features TEXT,
          prediction INTEGER NOT NULL,
          probability REAL,
          model_version TEXT,
          created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    cur.close()
    conn.close()


def save_prediction(customer_id, features: dict, prediction: int, probability: float, model_version: str = None):
    """Insert a prediction row into the configured DB. Supports 'mysql' and 'sqlite'."""
    engine = os.getenv('DB_ENGINE', DB_ENGINE)
    features_json = json.dumps(features, default=str, ensure_ascii=False)
    if engine == 'mysql' and mysql is not None:
        conn = _get_mysql_conn()
        cursor = conn.cursor()
        insert_sql = (
            "INSERT INTO predictions (customer_id, features, prediction, probability, model_version)"
            " VALUES (%s, %s, %s, %s, %s)"
        )
        cursor.execute(insert_sql, (customer_id, features_json, prediction, float(probability), model_version))
        conn.commit()
        cursor.close()
        conn.close()
    else:
        # default to sqlite
        _ensure_sqlite_table()
        conn = _get_sqlite_conn()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO predictions (customer_id, features, prediction, probability, model_version) VALUES (?, ?, ?, ?, ?)",
            (customer_id, features_json, int(prediction), float(probability), model_version),
        )
        conn.commit()
        cur.close()
        conn.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)