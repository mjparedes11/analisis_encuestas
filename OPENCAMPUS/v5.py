import pandas as pd
import os
import glob
import numpy as np
from IPython.display import display  # Importar display para mejor salida en Jupyter

# Ruta de la carpeta con los CSV
carpeta = 'OPENCAMPUS\\notas-opencampus2020'

# Definir los rangos de nota final
rangos = np.round(np.arange(0.44, 0.701, 0.01), 2)  # De 0.44 a 0.70
rangos_labels = [f"{r:.2f}" for r in rangos]

# Lista para almacenar resumen por curso
resumen = []

# Leer todos los archivos CSV de la carpeta
archivos = glob.glob(os.path.join(carpeta, '*.csv'))

for archivo in archivos:
    try:
        df = pd.read_csv(archivo, encoding='utf-8')

        # Verificar si existe la columna 'grade'
        if 'grade' not in df.columns:
            continue

        notas = df['grade']
        notas = notas[(notas >= 0) & (notas <= 1)]  # Asegurar datos válidos

        # Contar por rango definido
        conteo, _ = np.histogram(notas, bins=np.append(rangos, 1.01))  # Añadir 1.01 para incluir 1.0

        fila = {
            'Curso': os.path.basename(archivo),
            'Participantes': len(notas)
        }

        for i, etiqueta in enumerate(rangos_labels):
            fila[etiqueta] = conteo[i]

        fila['Total ≥ 0.70'] = (notas >= 0.70).sum()

        resumen.append(fila)

    except Exception as e:
        print(f"⚠ Error en {archivo}: {e}")

# Crear DataFrame
df_resumen = pd.DataFrame(resumen)

# Ordenar columnas
columnas_ordenadas = ['Curso', 'Participantes'] + rangos_labels + ['Total ≥ 0.70']
df_resumen = df_resumen[columnas_ordenadas]

# Agregar fila total
totales = df_resumen[rangos_labels + ['Participantes', 'Total ≥ 0.70']].sum(numeric_only=True)
totales['Curso'] = 'ΣUMA'
df_resumen = pd.concat([df_resumen, pd.DataFrame([totales])], ignore_index=True)

# Mostrar usando display (mejor presentación en Jupyter o VSCode)
display(df_resumen)

