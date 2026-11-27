<div align="center">

# MachineLearning

**Proyectos prácticos de aprendizaje automático con Python**

<a href="https://randomforestweb.streamlit.app/"><img src="https://img.shields.io/badge/Random_Forest-Abrir_app-FF4B4B?logo=streamlit&logoColor=white" alt="Abrir app Random Forest"></a>
<a href="[https://machinelearningapp.up.railway.app/](https://machinelearningapp.up.railway.app/)"><img src="https://img.shields.io/badge/Estimador_de_vivienda-Abrir_app-0B7C77?logo=railway&logoColor=white" alt="Abrir estimador de vivienda"></a>
<a href="https://machinelearningapp.up.railway.app/docs"><img src="https://img.shields.io/badge/API-FastAPI_docs-009688?logo=fastapi&logoColor=white" alt="Documentación FastAPI"></a>

</div>

Dos demos que muestran flujos distintos de machine learning: clasificación con Random Forest y regresión lineal para estimar precios de vivienda.

## Navegación

- [Random Forest](#random-forest)
- [Regresión lineal](#regresion-lineal)
- [Despliegues](#despliegues)
- [Ejecutar Random Forest localmente](#ejecutar-random-forest-localmente)
- [Estructura del repositorio](#estructura-del-repositorio)

## Random Forest

Clasificador interactivo construido con Streamlit. Permite ingresar variables clínicas y comparar las probabilidades estimadas para cinco clases: infarto, neumonía, gripe, ansiedad y gastroenteritis.

El flujo genera un dataset sintético de 5.000 registros, entrena un `RandomForestClassifier` y guarda el modelo en `models/`. Los scripts resuelven sus rutas desde la ubicación del propio archivo.

**[🚀 Abrir la app Random Forest](https://randomforestweb.streamlit.app/)** · [Ver el código de la app](ml_models/randomforest/3.Predecir_enfermedad.py)

<details>
<summary>Pasos de generación y entrenamiento</summary>

1. `1.Crear_dataset.py` crea `data/dataset_medico_ampliado.csv`.
2. `2.Entrenar_modelo.py` evalúa y guarda `models/modelo_random_forest_ampliado.pkl`.
3. `3.Predecir_enfermedad.py` carga el modelo y presenta el formulario interactivo.

</details>

## Regresión lineal

Estimador de precio de vivienda servido como una sola app: Django presenta el formulario y FastAPI ofrece la predicción. El servicio recibe la superficie en metros cuadrados y devuelve un precio estimado en COP.

**[🏠 Abrir el estimador](https://machinelearningapp.up.railway.app/)** · [Documentación de la API](https://machinelearningapp.up.railway.app/docs) · [Estado de la API](https://machinelearningapp.up.railway.app/health)

## Despliegues

| Proyecto | Plataforma | Enlace |
|---|---|---|
| Clasificador Random Forest | Streamlit Community Cloud | [randomforestweb.streamlit.app](https://randomforestweb.streamlit.app/) |
| Estimador de vivienda | Railway | [machinelearningapp.up.railway.app](https://machinelearningapp.up.railway.app/) |
| API de predicción | Railway | [FastAPI `/docs`](https://machinelearningapp.up.railway.app/docs) |

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

La app local estará en [http://localhost:8501](http://localhost:8501). Para detener el servidor, pulsa `Ctrl+C` en la terminal.

<details>
<summary>Dependencias principales</summary>

- Streamlit para la interfaz.
- pandas y NumPy para los datos.
- scikit-learn para entrenar y evaluar el clasificador.
- joblib para guardar y cargar el modelo.
- Plotly para visualizar las probabilidades.

</details>

## Estructura del repositorio

```text
ml_models/
├── linear_regression/
│   ├── backend/       # API FastAPI y modelo de regresión
│   └── frontend/      # Interfaz Django
└── randomforest/
    ├── data/          # Dataset generado
    ├── models/        # Modelo Random Forest entrenado
    ├── 1.Crear_dataset.py
    ├── 2.Entrenar_modelo.py
    ├── 3.Predecir_enfermedad.py
    └── requirements.txt
```

> **Nota:** Random Forest usa datos sintéticos para demostrar el flujo técnico. No es una herramienta clínica ni sustituye la evaluación de un profesional de salud.
