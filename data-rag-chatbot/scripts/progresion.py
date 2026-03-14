import matplotlib.pyplot as plt
import numpy as np

# Datos
categorias = ['X', 'X+', 'OK-', 'OK', 'P perfecta', 'P global']
pruebas = ['Sin Taxo', 'Con Taxo', 'Libre', 'Restringido']

gpt_data = np.array([
    [43, 25, 13, 12],  # X
    [13, 14, 4, 3],    # X+
    [9, 17, 11, 14],   # OK-
    [15, 40, 31, 35],  # OK
    [10, 12, 9, 10],   # P perfecta
    [29, 50, 38, 49]   # P global
])

gemini_data = np.array([
    [43, 25, 16, 15],  # X
    [13, 14, 4, 5],    # X+
    [9, 17, 5, 7],     # OK-
    [15, 40, 81, 84],  # OK
    [10, 12, 17, 18],  # P perfecta
    [29, 50, 86, 91]   # P global
])

# Colores de fondo por categoría (claros) y sus versiones oscuras para títulos
colores_fondo = {
    'X': ('#ffcccc', '#990000'),        # Rojo claro y oscuro
    'X+': ('#ffd9b3', '#b25900'),       # Naranja claro y oscuro
    'OK-': ('#ffffcc', '#999900'),      # Amarillo claro y oscuro
    'OK': ('#ccffcc', '#006600'),       # Verde claro y oscuro
    'P perfecta': ('#cce5ff', '#004c99'), # Azul claro y oscuro
    'P global': ('#e6ccff', '#4b0082')    # Lila claro y oscuro (índigo)
}

# Colores para barras: verde fluorescente y violeta
color_gpt = '#39FF14'      # Verde fluorescente
color_gemini = '#9B30FF'    # Violeta

# Configuración del gráfico
fig, axes = plt.subplots(2, 3, figsize=(20, 12))
axes = axes.ravel()

for i, (categoria, ax) in enumerate(zip(categorias, axes)):
    x = np.arange(len(pruebas))
    width = 0.35
    
    # Fondo de color para todo el subplot
    ax.set_facecolor(colores_fondo[categoria][0])
    
    # Título con color más oscuro
    ax.set_title(categoria, fontsize=16, fontweight='bold', pad=15, 
                color=colores_fondo[categoria][1])
    
    # Para Sin Taxo y Con Taxo (índices 0 y 1) - una sola barra (promedio)
    for j in [0, 1]:  # Sin Taxo, Con Taxo
        valor_unico = int(round((gpt_data[i][j] + gemini_data[i][j]) / 2))
        bar = ax.bar(x[j], valor_unico, width*2, color='gray', alpha=0.6, 
                     edgecolor='black', linewidth=0.5,
                     label='etapa previa' if j==0 and i==0 else "")
        # Anotar el valor con margen superior
        ax.text(x[j], valor_unico + 2, f'{valor_unico}', 
                ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    # Para Libre y Restringido (índices 2 y 3) - barras separadas GPT vs Gemini
    # Libre
    bar1 = ax.bar(x[2] - width/2, gpt_data[i][2], width, 
                  color=color_gpt, edgecolor='black', linewidth=0.5,
                  alpha=0.9, label='GPT' if i==0 else "")
    bar2 = ax.bar(x[2] + width/2, gemini_data[i][2], width, 
                  color=color_gemini, edgecolor='black', linewidth=0.5,
                  alpha=0.9, label='Gemini' if i==0 else "")
    
    # Restringido
    bar3 = ax.bar(x[3] - width/2, gpt_data[i][3], width, 
                  color=color_gpt, edgecolor='black', linewidth=0.5, alpha=0.9)
    bar4 = ax.bar(x[3] + width/2, gemini_data[i][3], width, 
                  color=color_gemini, edgecolor='black', linewidth=0.5, alpha=0.9)
    
    # Anotar valores con margen superior (enteros)
    ax.text(x[2] - width/2, gpt_data[i][2] + 2, f'{gpt_data[i][2]}', 
            ha='center', va='bottom', fontsize=9, fontweight='bold')
    ax.text(x[2] + width/2, gemini_data[i][2] + 2, f'{gemini_data[i][2]}', 
            ha='center', va='bottom', fontsize=9, fontweight='bold')
    ax.text(x[3] - width/2, gpt_data[i][3] + 2, f'{gpt_data[i][3]}', 
            ha='center', va='bottom', fontsize=9, fontweight='bold')
    ax.text(x[3] + width/2, gemini_data[i][3] + 2, f'{gemini_data[i][3]}', 
            ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    # Configurar ejes con márgenes
    ax.set_xticks(x)
    ax.set_xticklabels(pruebas, fontsize=11)
    ax.set_ylabel('Valor', fontsize=11, labelpad=10)
    
    # Asegurar que los valores del eje Y sean enteros
    max_valor = max(max(gpt_data[i]), max(gemini_data[i]))
    ax.set_ylim(0, max_valor * 1.15)
    ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True))
    
    ax.grid(True, alpha=0.3, axis='y', linestyle='--', linewidth=0.5)
    
    # Leyenda en la esquina superior derecha del primer subplot
    if i == 0:
        ax.legend(loc='upper right', fontsize=10, framealpha=0.9)

# Ajustar espaciado entre subplots
plt.subplots_adjust(hspace=0.3, wspace=0.25, top=0.9)

plt.suptitle('Comparación GPT vs Gemini por Categoría', 
             fontsize=18, fontweight='bold', y=0.98)
plt.figtext(0.5, 0.94, 'Sin Taxo/Con Taxo: etapa previa | Libre/Restringido: comparación directa', 
            ha='center', fontsize=12, style='italic')

plt.show()