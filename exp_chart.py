import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("experiment.csv")

fig, ax1 = plt.subplots(figsize=(10, 6))

color = 'blue'
ax1.set_xlabel('Кількість міст', fontsize=12)
ax1.set_ylabel('Час виконання (хвилини)', color=color, fontsize=12)
ax1.plot(df["Кількість міст (вершин)"], df["Середній час виконання алгоримту (у хвилинах)"], color=color, marker='o', linewidth=2, label='Реальний час')
ax1.tick_params(axis='y', labelcolor=color)
ax1.grid(True, alpha=0.3)

ax2 = ax1.twinx()  
color = 'red'
ax2.set_ylabel('Теоретична складність', color=color, fontsize=12)
ax2.plot(df["Кількість міст (вершин)"], df["Складність"], color=color, linestyle='--', marker='x', linewidth=2, label='Розрахована складність')
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Порівняння реального часу та теоретичної складності', fontsize=14)
fig.legend(loc="upper left", bbox_to_anchor=(0.15, 0.85))

plt.show()