# MachineLearning

Repositorio con proyectos de aprendizaje automático en Python.

## Proyectos

### Regresión lineal de precios de vivienda

La app combina un frontend Django con una API FastAPI. El modelo estima el precio de una vivienda a partir de su superficie.

- App: [machinelearningapp.up.railway.app](https://machinelearningapp.up.railway.app/)
- Documentación de la API: [FastAPI `/docs`](https://machinelearningapp.up.railway.app/docs)
- Estado de la API: [FastAPI `/health`](https://machinelearningapp.up.railway.app/health)

### Random Forest para clasificación de enfermedades

App Streamlit demostrativa que clasifica cinco diagnósticos usando variables clínicas simuladas: infarto, neumonía, gripe, ansiedad y gastroenteritis. El dataset se genera con 5.000 registros y el modelo se guarda en `models/`.

- Código de la app: [`3.Predecir_enfermedad.py`](ml_models/randomforest/3.Predecir_enfermedad.py)
- Deploy de Streamlit Community Cloud: pendiente de crear; la URL se añade aquí cuando Streamlit la asigne.

Para publicarla en Streamlit Community Cloud, selecciona este repositorio, la rama `master` y el archivo `ml_models/randomforest/3.Predecir_enfermedad.py` como entrada.

## Ejecutar Random Forest localmente

Desde la raíz del repositorio, en PowerShell:

```powershell
cd ml_models/randomforest
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python 1.Crear_dataset.py
python 2.Entrenar_modelo.py
streamlit run 3.Predecir_enfermedad.py
```

La interfaz local se abre en `http://localhost:8501`. Los scripts guardan el dataset y el modelo junto a ellos, así que funcionan independientemente de la carpeta desde la que se invoquen.

## Estructura

```text
ml_models/
├── linear_regression/
│   ├── backend/       # API FastAPI y modelo de regresión
│   └── frontend/      # Interfaz Django
└── randomforest/
    ├── data/          # Dataset generado
    ├── models/        # Random Forest entrenado
    ├── 1.Crear_dataset.py
    ├── 2.Entrenar_modelo.py
    ├── 3.Predecir_enfermedad.py
    └── requirements.txt
```

> El clasificador Random Forest usa datos sintéticos y sirve como demostración técnica; no sustituye una evaluación ni un diagnóstico médico.
