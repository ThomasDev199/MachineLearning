from pathlib import Path

import joblib
import numpy as np
from sklearn.linear_model import LinearRegression

# Superficie en m² y precio total de la vivienda en COP.
# La referencia queda en 500 millones COP para 100 m².
x = np.array(
    [[70], [80], [95], [100], [110], [120], [130], [140], [150], [160], [170], [180], [190], [220], [250]],
    dtype=float,
)
y = np.array(
    [
        350_000_000,
        400_000_000,
        475_000_000,
        500_000_000,
        550_000_000,
        600_000_000,
        650_000_000,
        700_000_000,
        750_000_000,
        800_000_000,
        850_000_000,
        900_000_000,
        950_000_000,
        1_100_000_000,
        1_250_000_000,
    ],
    dtype=float,
)

model = LinearRegression()
model.fit(x, y)

base_dir = Path(__file__).resolve().parent
model_path = base_dir / "models" / "linear_model.joblib"
model_path.parent.mkdir(parents=True, exist_ok=True)
joblib.dump(model, model_path)

print("Modelo entrenado correctamente")
print(f"Modelo guardado en: {model_path}")
print(f"Referencia para 100 m²: ${model.predict([[100]])[0]:,.0f} COP")