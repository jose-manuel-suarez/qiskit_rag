import matplotlib.pyplot as plt
import numpy as np

# Datos actualizados según tu tabla
# Columnas: [Sin Taxo, Con Taxo, RAG Free Gemini, RAG Restricted Gemini, RAG Free GPT-OSS, RAG Restricted GPT-OSS]
# Filas: X, X+, OK-, OK, P perfecta, P global

datos = np.array([
    [43, 25, 0, 0, 0, 0],  # X
    [13, 14, 0, 0, 0, 0],  # X+
    [9, 17, 0, 0, 0, 0],   # OK-
    [15, 40, 0, 0, 0, 0],  # OK
    [10, 12, 0, 0, 0, 0],  # P perfecta
    [31, 51, 0, 0, 0, 0]   # P global
])

# Configuración
categorias_filas = ['X', 'X+', 'OK-', 'OK', 'P perfecta', 'P global']
columnas_grupos = ['Sin Taxo', 'Con Taxo', 
                   'RAG Free\nGemini', 'RAG Restricted\nGemini',
                   'RAG Free\nGPT-OSS', 'RAG Restricted\nGPT-OSS']

# Colores para cada categoría (fila)
colores = ['#FF0000', '#FFA500', '#FFFF00', '#00FF00', '#1E90FF', '#4169E1']  # Rojo, Naranja, Amarillo, Verde, Azul claro, Azul oscuro

# Configurar el gráfico
x = np.arange(len(columnas_grupos))  # Posiciones para los 6 grupos
width = 0.12  # Ancho de cada barra (para 6 barras por grupo)

fig, ax = plt.subplots(figsize=(14, 7))

# Crear barras para cada categoría (fila)
for i, (categoria, color) in enumerate(zip(categorias_filas, colores)):
    offset = (i - 2.5) * width  # Centrar 6 barras
    barras = ax.bar(x + offset, datos[i], width, 
                    label=categoria, color=color, 
                    edgecolor='black', linewidth=0.5)
    
    # Añadir valores sobre las barras
    for barra, valor in zip(barras, datos[i]):
        if valor > 0:
            height = barra.get_height()
            ax.annotate(f'{valor}',
                        xy=(barra.get_x() + barra.get_width()/2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=8)

# Personalizar
ax.set_ylabel('Cantidad', fontsize=12)
ax.set_title('Comparación de Estrategias RAG', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(columnas_grupos, fontsize=10)
ax.legend(title='Categorías', loc='upper left', bbox_to_anchor=(1, 1))
ax.grid(axis='y', alpha=0.3)
ax.set_axisbelow(True)

plt.tight_layout()
plt.show()