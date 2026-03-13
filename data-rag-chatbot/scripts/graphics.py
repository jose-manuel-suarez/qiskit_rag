import matplotlib.pyplot as plt
import numpy as np

# Datos actualizados según tu tabla
# Columnas: [Sin Taxo, Con Taxo, Free Gemini, Restricted Gemini, Free GPT-OSS, Restricted GPT-OSS]
# Filas: X, X+, OK-, OK, P perfecta, P global

datos = np.array([
    [43, 25, 16, 15, 13, 12],   # X
    [13, 14, 4, 5, 4, 3],       # X+
    [9, 17, 5, 7, 11, 14],      # OK-
    [15, 40, 81, 84, 31, 35],   # OK
    [10, 12, 17, 18, 9, 10],    # P perfecta
    [24, 57, 86, 91, 38, 49]    # P global
])

# Configuración
categorias_filas = ['X', 'X+', 'OK-', 'OK', 'P perfecta', 'P global']
columnas_grupos = ['Sin Taxonomia', 'Con Taxonomia', 'Libre', 'Restringido', 'Libre', 'Restringido']
# Colores originales (los que te gustaron más)
colores = ["#F17E7E", "#EEA55C", "#F3F3A6", "#93E793", "#45A0FA", "#C1A0FF"]

# Configurar el gráfico
x = np.arange(len(columnas_grupos))  # Posiciones para los 6 grupos
width = 0.12  # Ancho de cada barra (para 6 barras por grupo)

fig, ax = plt.subplots(figsize=(15, 8))

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
                        ha='center', va='bottom', fontsize=7)

# Añadir línea vertical divisoria después de las dos primeras columnas
ax.axvline(x=1.5, color='gray', linestyle='--', linewidth=2, alpha=0.7)

# Personalizar
ax.set_ylabel('Cantidad', fontsize=12)
ax.set_title('Comparación de Estrategias RAG', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(columnas_grupos, fontsize=10)
ax.legend(title='Categorías', loc='upper left', bbox_to_anchor=(1, 1))
ax.grid(axis='y', alpha=0.3)
ax.set_axisbelow(True)

# Añadir etiqueta "ETAPA EXPERIMENTAL PREVIA" arriba (entre 80 y 100)
ax.text(0.5, 95, 'ETAPA EXPERIMENTAL\nPREVIA', 
        transform=ax.transData, ha='center', va='center',
        fontsize=11, fontweight='bold', color='#8B4513',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#FDF5E6', alpha=0.9, 
                  edgecolor='#8B4513', linewidth=2))

# Añadir etiqueta "ARQUITECTURA RAG" arriba (centrada en los modelos)
ax.text(3.5, 95, 'ARQUITECTURA RAG', 
        transform=ax.transData, ha='center', va='center',
        fontsize=11, fontweight='bold', color='#1A5276',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#EBF5FB', alpha=0.9,
                  edgecolor='#1A5276', linewidth=2))

# Añadir sub-etiquetas inferiores para los modelos
# Google Gemini (entre 3ra y 4ta columna - índices 2 y 3)
ax.text(2.5, -8, 'GEMINI', 
        transform=ax.transData, ha='center', va='top',
        fontsize=10, fontweight='bold', color='#1A5276',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#EBF5FB', alpha=0.8))

# GPT-OSS (entre las últimas dos columnas - índices 4 y 5)
ax.text(4.5, -8, 'GPT-OSS', 
        transform=ax.transData, ha='center', va='top',
        fontsize=10, fontweight='bold', color='#117A65',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8F8F5', alpha=0.8))

# Ajustar límites del eje y para dar espacio a las etiquetas
ax.set_ylim(0, 105)  # Fijamos el límite superior en 105 para dejar espacio arriba

plt.tight_layout()
plt.subplots_adjust(bottom=0.2, top=0.9)  # Ajustar espacio superior e inferior
plt.show()