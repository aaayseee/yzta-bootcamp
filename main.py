from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

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
    
    return {
        "Tahmin_Sonucu": sonuc,
        "Olasilik": olasilik,
        "Aksiyon": aksiyon_onerisi_uret(sonuc, veri.model_dump())
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)