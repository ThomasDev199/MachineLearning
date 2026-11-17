import joblib 
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 

# Predecir precios de viviendas según la superficie en m2

# Datos de entrenamiento X y Y
x = np.array([70], [80], [90], [100], [110], [120], [130], [140], [150]) # metros cuadrados de superficie

y = np.array([420000000, 800000000])