import functions as f
import matplotlib.pyplot as plt
from matplotlib import animation
import networkx as nx
from itertools import combinations

#num_cities = int(input("Введіть кількість міст: "))
#num_iterations = int(input("Введіть бажану к-сть ітерацій: "))
num_cities = 15
num_iterations = 150
a = 1
b = 3
Q = 1
evaporation_rate = 0.2
num_ants = 100

def1 = f.create_matrix(num_cities, a, b, Q)
lengths = def1[0]
nods = def1[1]
attractiveness = def1[2]
pheromone_matrix = def1[3]
coords = def1[4]

history_best_distence = f.algorithm(evaporation_rate, num_ants, lengths, nods, attractiveness, pheromone_matrix, a, b, Q)

#Малювання графіків

fig, ax = plt.subplots(dpi=150)
ax.set(xlabel="Ітерація", ylabel="Довжина шляху", xlim=(0, len(history_best_distence) - 1))
ax.plot(history_best_distence)
plt.show()

G = nx.from_numpy_array(lengths)
pos = {i: coords[i] for i in range(num_cities)}
plt.figure(figsize=(8, 8))
nx.draw(G, pos, with_labels=False, node_color='lightblue', node_size=500)
plt.axis("off")
plt.show()