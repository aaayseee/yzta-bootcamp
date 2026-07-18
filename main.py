from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# API uygulamasını başlatıyoruz
app = FastAPI(title="Churn Prediction API", version="1.0")

# Eğittiğimiz beyni sisteme yüklüyoruz
model = joblib.load('churn_modeli.pkl')

# 1. Dışarıdan gelecek veri paketinin iskeletini (Şemasını) kuruyoruz
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

@app.post("/tahmin_et/")
def churn_tahmini_yap(veri: MusteriVerisi):
    # 2. Gelen verideki mükerrer metinleri tekilleştiriyoruz (Colab'deki veri temizliği kuralımız)
    cihaz = "Mobile Phone" if veri.PreferredLoginDevice in ["Phone", "Mobile Phone"] else veri.PreferredLoginDevice
    odeme = "Credit Card" if veri.PreferredPaymentMode == "CC" else ("Cash on Delivery" if veri.PreferredPaymentMode == "COD" else veri.PreferredPaymentMode)
    kategori = "Mobile Phone" if veri.PreferedOrderCat == "Mobile" else veri.PreferedOrderCat

    # 3. Modelin beklediği tam 25 sütunluk One-Hot Encoded iskeleti canlı olarak inşa ediyoruz
    model_girdisi = pd.DataFrame([{
        'Tenure': veri.Tenure,
        'CityTier': veri.CityTier,
        'WarehouseToHome': veri.WarehouseToHome,
        'HourSpendOnApp': veri.HourSpendOnApp,
        'NumberOfDeviceRegistered': veri.NumberOfDeviceRegistered,
        'SatisfactionScore': veri.SatisfactionScore,
        'NumberOfAddress': veri.NumberOfAddress,
        'Complain': veri.Complain,
        'OrderAmountHikeFromlastYear': veri.OrderAmountHikeFromlastYear,
        'CouponUsed': veri.CouponUsed,
        'OrderCount': veri.OrderCount,
        'DaySinceLastOrder': veri.DaySinceLastOrder,
        'CashbackAmount': veri.CashbackAmount,
        # Matematiksel Dönüşümler (Eşleşirse 1, eşleşmezse 0)
        'PreferredLoginDevice_Mobile Phone': 1 if cihaz == 'Mobile Phone' else 0,
        'PreferredPaymentMode_Credit Card': 1 if odeme == 'Credit Card' else 0,
        'PreferredPaymentMode_Debit Card': 1 if odeme == 'Debit Card' else 0,
        'PreferredPaymentMode_E wallet': 1 if odeme == 'E wallet' else 0,
        'PreferredPaymentMode_UPI': 1 if odeme == 'UPI' else 0,
        'Gender_Male': 1 if veri.Gender == 'Male' else 0,
        'PreferedOrderCat_Grocery': 1 if kategori == 'Grocery' else 0,
        'PreferedOrderCat_Laptop & Accessory': 1 if kategori == 'Laptop & Accessory' else 0,
        'PreferedOrderCat_Mobile Phone': 1 if kategori == 'Mobile Phone' else 0,
        'PreferedOrderCat_Others': 1 if kategori == 'Others' else 0,
        'MaritalStatus_Married': 1 if veri.MaritalStatus == 'Married' else 0,
        'MaritalStatus_Single': 1 if veri.MaritalStatus == 'Single' else 0
    }])

    # 4. Yapay Zeka Karar Veriyor
    tahmin_sonucu = model.predict(model_girdisi)
    
    # 5. Sonucu sisteme döndürüyoruz
    return {
        "Tahmin_Sonucu": "Terk Edecek (Riskli Müşteri) 🚨" if tahmin_sonucu[0] == 1 else "Sistemde Kalacak (Güvenli) ✅",
        "Sistem_Mesaji": "Arka plan veri akışı başarılı, model tahmini üretti."
    }