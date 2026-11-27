from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from pathlib import Path
import joblib
import numpy as np
import os
import sys

from a2wsgi import WSGIMiddleware

# Initialize Django from the sibling frontend directory.
PROJECT_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = PROJECT_DIR / "frontend"
sys.path.insert(0, str(FRONTEND_DIR))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
from config.wsgi import application as django_application

app = FastAPI(
    title="API de Predicción de Viviendas",
    description="Predicción de precios según superficie en metros cuadrados",
    version="1.0.0",
)

MODEL_PATH = Path(__file__).resolve().parent / "models" / "linear_model.joblib"
if not MODEL_PATH.exists():
    raise FileNotFoundError("Modelo no encontrado. Ejecuta primero train.py")
model = joblib.load(MODEL_PATH)


class HouseData(BaseModel):
    surface: float = Field(
        gt=0,
        description="Superficie de la vivienda en metros cuadrados",
        examples=[100],
    )


@app.get("/health")
def health():
    return {"message": "API de predicción de viviendas funcionando", "docs": "/docs"}


@app.post("/predict")
def predict(data: HouseData):
    try:
        prediction = model.predict(np.array([[data.surface]]))
        return {
            "surface_m2": data.surface,
            "predicted_price_cop": round(float(prediction[0]), 2),
            "currency": "COP",
        }
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Error al realizar la predicción: {exc}",
        )


# API endpoints are declared first; Django handles the remaining paths.
app.mount("/", WSGIMiddleware(django_application), name="frontend")