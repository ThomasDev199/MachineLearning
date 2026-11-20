import joblib 
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 

# # # Predecir precios de viviendas según la superficie en m2

# Datos de entrenamiento X y Y
x = np.array([[70], [80], [95], [100], [110], [120], [130], [140], [150]]) # metros cuadrados de superficie

y = np.array([420000000, 800000000,1700000, 1900000, 2500000, 3000000, 3500000, 4000000, 4500000]) # precios en pesos colombianos

#Entrenar el modelode regresion lineal
model = LinearRegression()
model.fit(x,y)

# # Predicciones de prueba
# y_pred = model.predict(x)

# #Imprimir los coeficientes del modelo
# print('Coeficiente de regresión:', model.coef_[0])
# print('Termino independiente:', model.intercept_)

# #Graficar  datos reales 
# plt.scatter(x,y, color='blue', label='Datos reales')

# # Graficar la línea de regresión
# plt.plot(x, y_pred, color='red', label='Línea de regresión')

# #Agregar etiquetas y título
# plt.xlabel('Superficie (m2)')
# plt.ylabel('Precio (COP)')
# plt.title('Regresión lineal: Precio de vivienda según superficie')
# plt.legend()
# plt.grid(True)

# # Mostrar la grafica
# plt.show()

# # Guardar(Serializar) el modelo entrenado en un archivo
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "linear_model.joblib"

# Crear carpeta si no existe
MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)

# Guardar modelo
joblib.dump(model, MODEL_PATH)

print("Modelo entrenado correctamente")
print(f"Modelo guardado en: {MODEL_PATH}")