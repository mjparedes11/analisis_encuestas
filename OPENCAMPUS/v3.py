import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import glob

# Configuración inicial
carpeta = 'OPENCAMPUS\\notas-opencampus2020'
columnas_requeridas = ['test 01', 'test 02', 'test 03', 'test 04', 'test 05', 'test 06', 'test Avg', 'reto', 'grade']

# Buscar todos los archivos CSV
archivos = glob.glob(os.path.join(carpeta, '*.csv'))

# Cargar solo archivos con columnas requeridas
dataframes_validos = []
for archivo in archivos:
    df_temp = pd.read_csv(archivo, encoding='utf-8')
    if all(col in df_temp.columns for col in columnas_requeridas):
        dataframes_validos.append(df_temp)
        print(f"✔ {os.path.basename(archivo)} incluido (columnas válidas)")
    else:
        print(f"✖ {os.path.basename(archivo)} omitido (faltan columnas)")

# Unir archivos válidos
df = pd.concat(dataframes_validos, ignore_index=True)

print(f'\nTotal de filas después de concatenar: {len(df)}')
print(df[columnas_requeridas + ['grade']].head())

# ---------- Análisis ----------

# Histograma de notas finales
plt.figure(figsize=(10, 5))
sns.histplot(df['grade'], bins=20, kde=True)
plt.title('Distribución de notas finales')
plt.xlabel('Nota final')
plt.ylabel('Cantidad de estudiantes')
plt.show()

# Aprobados
aprobados = df[df['grade'] >= 70]
porcentaje = len(aprobados) / len(df) * 100
print(f"Aprobaron: {len(aprobados)} estudiantes ({porcentaje:.2f}%)")

# Correlación entre columnas
plt.figure(figsize=(12, 6))
sns.heatmap(df[columnas_requeridas].corr(), annot=True, cmap='coolwarm')
plt.title('Correlación entre pruebas y nota final')
plt.show()

# Dispersión entre promedio de test y nota final
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='test Avg', y='grade')
plt.title('Relación entre test promedio y nota final')
plt.xlabel('Promedio de tests')
plt.ylabel('Nota final')
plt.show()

# Boxplot por test
df_tests = df[['test 01', 'test 02', 'test 03', 'test 04', 'test 05', 'test 06']]
plt.figure(figsize=(10, 6))
sns.boxplot(data=df_tests)
plt.title('Distribución de calificaciones por test')
plt.ylabel('Nota')
plt.show()
