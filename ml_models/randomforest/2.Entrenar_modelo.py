from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

BASE_DIR = Path(__file__).resolve().parent
DATASET_PATH = BASE_DIR / "data" / "dataset_medico_ampliado.csv"
MODEL_PATH = BASE_DIR / "models" / "modelo_random_forest_ampliado.pkl"
TARGET_COLUMN = "diagnostico"


def log(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def main():
    if not DATASET_PATH.is_file():
        raise FileNotFoundError(
            f"No se encontró {DATASET_PATH}. Ejecuta primero 1.Crear_dataset.py."
        )

    log("1. CARGA DEL DATASET")
    df = pd.read_csv(DATASET_PATH)
    if TARGET_COLUMN not in df.columns:
        raise ValueError(f"El dataset debe incluir la columna {TARGET_COLUMN!r}.")
    print(f"Dataset cargado: {df.shape[0]} filas, {df.shape[1]} columnas")

    log("2. PREPARACIÓN DE DATOS")
    X = df.drop(columns=[TARGET_COLUMN])
    y = df[TARGET_COLUMN]
    if y.nunique() < 2:
        raise ValueError("Se necesitan al menos dos diagnósticos para entrenar.")
    print(f"Variables: {len(X.columns)}")
    print(f"Clases: {', '.join(map(str, sorted(y.unique())))}")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )
    print(f"Entrenamiento: {len(X_train)} | Evaluación: {len(X_test)}")

    log("3. ENTRENAMIENTO")
    model = RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)
    print("Modelo entrenado")

    log("4. EVALUACIÓN")
    y_pred = model.predict(X_test)
    print(f"Exactitud: {model.score(X_test, y_test):.4f}")
    print(classification_report(y_test, y_pred, zero_division=0))
    print("Matriz de confusión:")
    print(confusion_matrix(y_test, y_pred, labels=model.classes_))

    log("5. IMPORTANCIA DE VARIABLES")
    importances = pd.DataFrame({
        "Variable": X.columns,
        "Importancia (%)": (model.feature_importances_ * 100).round(2),
    }).sort_values("Importancia (%)", ascending=False)
    print(importances.head(15).to_string(index=False))

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"\nModelo guardado en: {MODEL_PATH}")


if __name__ == "__main__":
    main()