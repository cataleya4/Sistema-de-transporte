# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

num_datos = 1000

horas_dia = np.random.randint(0, 24, size=num_datos)
dias_semana = np.random.randint(0, 7, size=num_datos)
trafico = np.random.randint(1, 11, size=num_datos)
pasajeros = np.random.randint(1, 101, size=num_datos)
duracion_viaje = np.random.randint(10, 60, size=num_datos)

datos = pd.DataFrame({
    'Hora del día': horas_dia,
    'Día de la semana': dias_semana,
    'Tráfico': trafico,
    'Cantidad de pasajeros': pasajeros,
    'Duración del viaje': duracion_viaje
})

datos['Costo del viaje'] = 5 + 0.1 * datos['Duración del viaje'] + 0.5 * datos['Cantidad de pasajeros']

print(datos.head())

datos.to_csv('datos_transporte.csv', index=False)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

datos = pd.read_csv('datos_transporte.csv')

X = datos.drop('Costo del viaje', axis=1)
y = datos['Costo del viaje']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = LinearRegression()

modelo.fit(X_train, y_train)

predicciones = modelo.predict(X_test)

mse = mean_squared_error(y_test, predicciones)
print("Error cuadrático medio:", mse)