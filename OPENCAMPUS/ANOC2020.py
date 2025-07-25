import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
import glob


print(os.getcwd())
ruta = 'OPENCAMPUS\\notas-opencampus2020\\UTPL_AKOMP14_2020_2_grade_report_2020-12-29-1816.csv'
df = pd.read_csv(ruta, sep=',', encoding='utf-8')


print(df.info())


# Gráfico de barras de la cantidad de estudiantes por nota final
plt.figure(figsize=(10, 5))
sns.histplot(df['grade'], bins=20, kde=True)
plt.title('Distribución de notas finales')
plt.xlabel('Nota final')
plt.ylabel('Cantidad de estudiantes')
plt.show()

# Gráfico de barras de la cantidad de estudiantes por carrera
aprobados = df[df['grade'] >= 70]
print(f"Aprobaron: {len(aprobados)} estudiantes ({len(aprobados)/len(df)*100:.2f}%)")

columnas_tests = ['test 01', 'test 02', 'test 03', 'test 04', 'test 05', 'test 06', 'test Avg', 'reto', 'grade']
plt.figure(figsize=(12, 6))
sns.heatmap(df[columnas_tests].corr(), annot=True, cmap='coolwarm')
plt.title('Correlación entre pruebas y nota final')
plt.show()


import pandas as pd

# Ruta a la carpeta donde están tus archivos CSV
carpeta = 'OPENCAMPUS\\notas-opencampus2020'

# Buscar todos los archivos CSV dentro de esa carpeta
archivos = glob.glob(os.path.join(carpeta, '*.csv'))

# Lista para almacenar los DataFrames
dataframes = []

# Cargar cada archivo y agregarlo a la lista
for archivo in archivos:
    df_temp = pd.read_csv(archivo, sep=',', encoding='utf-8')
    dataframes.append(df_temp)

# Unir todos los DataFrames en uno solo
df_completo = pd.concat(dataframes, ignore_index=True)

# Verificar resultado
print(f'Total de filas combinadas: {df_completo.shape[0]}')
print(df_completo.head())
print(df_completo.info())
for archivo in archivos:
    df_temp = pd.read_csv(archivo, sep=',', encoding='utf-8')
    print(f"{os.path.basename(archivo)} -> columnas: {len(df_temp.columns)}")

