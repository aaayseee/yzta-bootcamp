"""FastAPI backend for LoyalCart churn predictions."""

import os
from typing import Optional

from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

from db.repository import initialize_database, save_prediction
from prediction_service import predict_churn


app = FastAPI(title="LoyalCart Prediction API", version="3.0.0")


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
    CustomerId: Optional[str] = None
    CreatedBy: Optional[str] = None


def _model_dump(instance: BaseModel):
    if hasattr(instance, "model_dump"):
        return instance.model_dump()
    return instance.dict()


def _require_api_key(x_api_key: Optional[str]) -> None:
    expected = os.getenv("LOYALCART_API_KEY")
    if expected and x_api_key != expected:
        raise HTTPException(status_code=401, detail="Geçersiz API anahtarı.")


@app.on_event("startup")
def startup() -> None:
    initialize_database()


@app.get("/health")
def health():
    return {"status": "ok", "service": "loyalcart-api"}


@app.post("/tahmin_et/")
@app.post("/predict/")
@app.post("/predict")
def tahmin_et(
    veri: MusteriVerisi,
    x_api_key: Optional[str] = Header(default=None),
):
    _require_api_key(x_api_key)
    payload = _model_dump(veri)
    outcome = predict_churn(payload)
    database_saved = True
    prediction_id = None
    try:
        prediction_id = save_prediction(
            customer_id=payload.get("CustomerId"),
            features={
                key: value
                for key, value in payload.items()
                if key not in {"CustomerId", "CreatedBy"}
            },
            prediction=outcome["prediction"],
            probability=outcome["probability"],
            model_version=outcome["model_version"],
            result=outcome["result"],
            action=outcome["action"],
            source="api",
            created_by=payload.get("CreatedBy"),
        )
    except Exception:
        database_saved = False

    return {
        "Tahmin_Sonucu": outcome["result"],
        "Olasilik": outcome["probability"],
        "Aksiyon": outcome["action"],
        "churn_prediction": outcome["prediction"],
        "churn_probability": outcome["probability"],
        "prediction_id": prediction_id,
        "database_saved": database_saved,
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
