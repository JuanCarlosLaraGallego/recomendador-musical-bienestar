import json
from pathlib import Path
import joblib
import pandas as pd

from src.config import MODEL_PATH, THRESHOLD_PATH
from src.features import build_input_dataframe

DEFAULT_THRESHOLD = 0.60

def load_threshold() -> float:
    if THRESHOLD_PATH.exists():
        with open(THRESHOLD_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        return float(data.get("threshold", DEFAULT_THRESHOLD))
    return DEFAULT_THRESHOLD

def model_available() -> bool:
    return MODEL_PATH.exists()

def predict_user(payload: dict) -> dict:
    df_input = build_input_dataframe(payload)
    threshold = load_threshold()

    if not model_available():
        return {
            "status": "missing_model",
            "threshold": threshold,
            "features_used": df_input.columns.tolist(),
            "message": "No se encontró models/model_pipeline.joblib. La app funciona como plantilla, pero falta exportar el modelo real.",
        }

    model = joblib.load(MODEL_PATH)
    proba = float(model.predict_proba(df_input)[0, 1])
    flag = int(proba >= threshold)

    return {
        "status": "ok",
        "probability_improve": proba,
        "recommend_flag": flag,
        "threshold": threshold,
        "features_used": df_input.columns.tolist(),
    }
