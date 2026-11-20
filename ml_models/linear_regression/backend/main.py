
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from pathlib import Path
import joblib
import numpy as np

# Crear aplicación
app = FastAPI(
    title="API de Predicción de Viviendas",
    description="Predicción de precios según superficie en metros cuadrados",
    version="1.0.0"
)

# Obtener ruta del proyecto
BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "models" / "linear_model.joblib"

# Cargar modelo
if not MODEL_PATH.exists():
    raise FileNotFoundError(
        "Modelo no encontrado. Ejecuta primero train.py"
    )

model = joblib.load(MODEL_PATH)


# Esquema de entrada
class HouseData(BaseModel):
    surface: float = Field(
        gt=0,
        description="Superficie de la vivienda en metros cuadrados",
        examples=[100]
    )


# Endpoint principal
@app.get("/")
def home():
    return {
        "message": "API de predicción de viviendas funcionando",
        "docs": "/docs"
    }

# Endpoint de predicción
@app.post("/predict")
def predict(data: HouseData):
    try:
        # Obtener superficie
        surface = data.surface

        # Realizar predicción
        prediction = model.predict(
            np.array([[surface]])
        )
        price = float(prediction[0])
        return {
            "surface_m2": surface,
            "predicted_price_cop": round(price, 2),
            "currency": "COP"
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al realizar la predicción: {str(e)}"
        )
