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
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Cargar los datos desde el archivo CSV
datos = pd.read_csv('datos_transporte.csv')

# Seleccionar las características relevantes para el clustering
X = datos[['Tráfico', 'Cantidad de pasajeros', 'Duración del viaje']]

# Escalar las características para que tengan media 0 y desviación estándar 1
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Aplicar el algoritmo de k-means para encontrar clusters
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X_scaled)

# Agregar los clusters como una nueva columna en el DataFrame original
datos['Cluster'] = clusters

# Visualizar los clusters en un diagrama de dispersión 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(X_scaled[:, 0], X_scaled[:, 1], X_scaled[:, 2], c=clusters, cmap='viridis')
ax.set_xlabel('Tráfico')
ax.set_ylabel('Cantidad de pasajeros')
ax.set_zlabel('Duración del viaje')
ax.set_title('Clustering de datos de transporte')

plt.show()