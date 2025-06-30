import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Cargar el archivo CSV
df = pd.read_csv("C:\\Users\\USUARIO\\Desktop\\de.csv", sep=';', encoding='utf-8')

# Filtrar solo preguntas cerradas (3, 4 o 5 opciones)
preguntas_cerradas = [col for col in df.columns if '/3' in col or '/4' in col or '/5' in col]

# Agrupar por número de opciones
grupos = {
    '3 opciones': [col for col in preguntas_cerradas if '/3' in col],
    '4 opciones': [col for col in preguntas_cerradas if '/4' in col],
    '5 opciones': [col for col in preguntas_cerradas if '/5' in col],
}

# Crear figura para los 3 tipos de gráfico por grupo (3x3 = 9 subplots)
fig, axs = plt.subplots(nrows=3, ncols=3, figsize=(20, 15))
axs = axs.flatten()

# 1. Barras apiladas
for i, (grupo, columnas) in enumerate(grupos.items()):
    porcentajes = pd.DataFrame()
    for col in columnas:
        conteo = df[col].value_counts(normalize=True).sort_index() * 100
        porcentajes[col] = conteo
    porcentajes = porcentajes.fillna(0)
    porcentajes.T.plot(kind='bar', stacked=True, ax=axs[i], colormap='viridis')
    axs[i].set_title(f'Barras apiladas - {grupo}')
    axs[i].set_ylabel('% de respuestas')
    axs[i].legend(title='Opción', bbox_to_anchor=(1.05, 1), loc='upper left')

# 2. Barras simples por color
for i, (grupo, columnas) in enumerate(grupos.items(), start=3):
    for col in columnas:
        conteo = df[col].value_counts().sort_index()
        axs[i].bar(contador := np.arange(len(conteo)), conteo.values, label=col)
    axs[i].set_xticks(contador)
    axs[i].set_xticklabels(conteo.index)
    axs[i].set_title(f'Barras simples - {grupo}')
    axs[i].set_ylabel('Frecuencia')
    axs[i].legend(loc='upper right', fontsize='small')

# 3. Mapas de calor
for i, (grupo, columnas) in enumerate(grupos.items(), start=6):
    matriz = pd.DataFrame()
    for col in columnas:
        conteo = df[col].value_counts(normalize=True).sort_index() * 100
        matriz[col] = conteo
    matriz = matriz.fillna(0)
    sns.heatmap(matriz.T, ax=axs[i], cmap='YlGnBu', annot=True, fmt=".1f")
    axs[i].set_title(f'Mapa de calor - {grupo}')
    axs[i].set_xlabel('Opciones')
    axs[i].set_ylabel('Preguntas')

plt.tight_layout()
plt.show()
