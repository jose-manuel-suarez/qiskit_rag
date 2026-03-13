import matplotlib.pyplot as plt

# Datos organizados por filas según tu descripción
# Fila 1 y 2: Modo Libre (Gemini y GPT-OSS)
# Fila 3 y 4: Modo Restrictivo (Gemini y GPT-OSS)
datos = [
    [79, 21], [28, 72],  # Modo Libre
    [91, 9], [94, 5]    # Modo Restrictivo
]

modelos = ['Google Gemini Flash-2.5', 'OpenAI GPT-OSS-20b', 'Google Gemini Flash-2.5', 'OpenAI GPT-OSS-20b']
modos = ['Modo Libre', 'Modo Libre', 'Modo Restrictivo', 'Modo Restrictivo']
etiquetas = ['Taxonomía', 'Conocimiento Interno']
colores = ["#63B9DB", "#E2A127"]  # Celeste y Naranja

# Crear la figura con 4 subgráficos (2x2)
fig, axs = plt.subplots(2, 2, figsize=(10, 10))
axs = axs.flatten()

for i, ax in enumerate(axs):
    # Crear el gráfico de torta
    wedges, texts, autotexts = ax.pie(
        datos[i], 
        autopct='%1.1f%%', 
        startangle=140, 
        colors=colores,
        textprops={'color':"w", 'weight':'bold'}
    )
    
    # Título arriba de cada torta con el Modo y el Modelo debajo
    ax.set_title(f"{modos[i]}\nModelo: {modelos[i]}", pad=20, fontsize=12, fontweight='bold')

# Añadir una leyenda única en la parte inferior
fig.legend(wedges, etiquetas, loc='lower center', ncol=2, fontsize=11)

# Ajustar diseño para que no se solapen
plt.tight_layout(rect=[0, 0.05, 1, 0.95])
plt.show()
