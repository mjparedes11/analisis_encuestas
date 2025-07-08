import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
import glob
from collections import Counter

# Ruta a la carpeta donde están tus archivos CSV
carpeta = 'OPENCAMPUS\\notas-opencampus2020'
archivos = glob.glob(os.path.join(carpeta, '*.csv'))

# Descubrir columnas comunes
columnas_comunes = None
estructuras = {}  # opcional, para debug


for archivo in archivos:
    df_temp = pd.read_csv(archivo, sep=',', encoding='utf-8')
    estructuras[os.path.basename(archivo)] = df_temp.columns.tolist()
    if columnas_comunes is None:
        columnas_comunes = set(df_temp.columns)
    else:
        columnas_comunes = columnas_comunes.intersection(set(df_temp.columns))

# Mostrar columnas comunes encontradas
columnas_comunes = list(columnas_comunes)
print("Columnas comunes en todos los archivos:", columnas_comunes)

# Cargar y combinar solo columnas comunes
dataframes = []
for archivo in archivos:
    df_temp = pd.read_csv(archivo, sep=',', encoding='utf-8')[columnas_comunes]
    dataframes.append(df_temp)

df_completo = pd.concat(dataframes, ignore_index=True)

# Resultado final
print(f'\nTotal de filas combinadas: {df_completo.shape[0]}')
print(f'Columnas finales: {df_completo.shape[1]}')
print(df_completo.head())

# Histograma de notas
plt.figure(figsize=(10, 5))
sns.histplot(df_completo['grade'], bins=20, kde=True)
plt.title('Distribución de notas finales')
plt.xlabel('Nota final')
plt.ylabel('Cantidad de estudiantes')
plt.show()

# Porcentaje de aprobados
aprobados = df_completo[df_completo['grade'] >= 0.7]
print(f"Aprobaron: {len(aprobados)} estudiantes ({len(aprobados)/len(df_completo)*100:.2f}%)")
