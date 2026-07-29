"""Shared churn prediction service used by FastAPI and Streamlit."""

from functools import lru_cache
from typing import Any, Dict

import joblib
import pandas as pd
import sklearn


@lru_cache(maxsize=1)
def get_model():
    return joblib.load("churn_modeli.pkl")


def action_recommendation(prediction: int, features: Dict[str, Any]) -> str:
    if prediction == 1:
        if int(features.get("Complain", 0)) == 1:
            return (
                "Müşteri şikayetli: 24 saat içinde kişiselleştirilmiş geri "
                "dönüş ve uygun bir telafi kampanyası planlayın."
            )
        return (
            "Müşteri etkileşimi azalmış: kişiselleştirilmiş geri kazanım "
            "kampanyası planlayın."
        )
    return "Sadakat programı ve kişiselleştirilmiş tekliflerle ilişkiyi koruyun."


def predict_churn(features: Dict[str, Any]) -> Dict[str, Any]:
    model = get_model()
    model_features = {
        key: value
        for key, value in features.items()
        if key not in {"CustomerId", "CreatedBy"}
    }
    raw_df = pd.DataFrame([model_features])
    encoded = pd.get_dummies(raw_df)
    expected_features = list(model.feature_names_in_)
    final_df = encoded.reindex(columns=expected_features, fill_value=0)

    prediction = int(model.predict(final_df)[0])
    probability = float(model.predict_proba(final_df)[0][1])
    result = "Terk Riski Var" if prediction == 1 else "Sadık Müşteri"
    return {
        "prediction": prediction,
        "probability": probability,
        "result": result,
        "action": action_recommendation(prediction, model_features),
        "model_version": f"sklearn-{sklearn.__version__}",
    }

