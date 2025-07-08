import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import glob
from functools import reduce

# Ruta
carpeta = 'OPENCAMPUS\\notas-opencampus2020'

# Leer todos los archivos
archivos = glob.glob(os.path.join(carpeta, '*.csv'))
dataframes = [pd.read_csv(archivo, encoding='utf-8') for archivo in archivos]

# Obtener columnas comunes entre todos los DataFrames
columnas_comunes = list(reduce(lambda x, y: set(x) & set(y), [df.columns for df in dataframes]))
print(f"Columnas comunes encontradas: {columnas_comunes}")

# Unir solo por columnas comunes
df_comun = pd.concat([df[columnas_comunes] for df in dataframes], ignore_index=True)

# Mostrar resumen
print(f"\nTotal de filas unificadas: {len(df_comun)}")
print(df_comun.head())

# Análisis solo si existen columnas clave como 'grade'
if 'grade' in df_comun.columns:
    plt.figure(figsize=(10, 5))
    sns.histplot(df_comun['grade'], bins=20, kde=True)
    plt.title('Distribución de notas finales (con columnas comunes)')
    plt.xlabel('Nota final')
    plt.ylabel('Cantidad de estudiantes')
    plt.show()

    if 'Enrollment Track' in df_comun.columns:
        plt.figure(figsize=(10, 5))
        sns.countplot(data=df_comun, x='Enrollment Track', order=df_comun['Enrollment Track'].value_counts().index)
        plt.title('Distribución por modalidad de inscripción')
        plt.xticks(rotation=45)
        plt.ylabel('Cantidad de estudiantes')
        plt.show()

    aprobados = df_comun[df_comun['grade'] >= 70]
    print(f"Aprobaron (estimado con columnas comunes): {len(aprobados)} estudiantes ({len(aprobados)/len(df_comun)*100:.2f}%)")
else:
    print("No se encontró la columna 'grade'. No se puede hacer análisis de notas.")

