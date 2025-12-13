import numpy as np
from scipy.spatial import distance_matrix

def create_matrix (num_cities, a, b, Q):
    coords = np.random.rand(num_cities, 2) * 100
    lenghts = distance_matrix(coords, coords)
    np.fill_diagonal(lenghts, np.nan)


    pheromone_matrix = np.ones((lenghts.shape[0], lenghts.shape[0]))/ lenghts.shape[0] * 10
    np.fill_diagonal(pheromone_matrix, 0)

    # Поточна матриця бажань мурах
    attractiveness = (pheromone_matrix ** a) * ((Q / lenghts) ** b)
    np.fill_diagonal(attractiveness , 0)

    # Створюємо вершини
    nods = np.array([i for i in range(lenghts.shape[0])])
    return [lenghts, nods, attractiveness, pheromone_matrix, coords]

def algorithm(evaporation_rate, num_ants, lenghts, nods, attractiveness, pheromone_matrix, a, b, Q):
    best_path = ([], float('inf'))
    history_best_path = []
    history_best_distence = np.array([])
    global_best_distance = np.array([float('inf')])
    for i in range(200):
        ant_pathes = []
        for n in range(num_ants):

            #Випадково вибираємо початкову вершину
            attractiveness_for_ant = attractiveness.copy()
            start_nod = np.random.choice(nods)
            path = np.array([]).astype(int)
            path = np.append(path, start_nod)
            attractiveness_for_ant[:,start_nod] = 0
            new_nod = start_nod

            # Цикл щоб кожна мураха пройшла маршруne
            for j in range(attractiveness_for_ant .shape[0] - 2):

                # Оцінюємо ймовірність переходу на нову вершину
                propobility = attractiveness_for_ant[new_nod, :] / attractiveness_for_ant.sum(axis=1)[new_nod]

                # Вибираємо нову вершину
                new_nod = np.random.choice(a=nods,p=propobility)

                # Робимо йомовірність потрапити на поточну вершину 0
                attractiveness_for_ant[:, new_nod] = 0

                # Додаємо нову вершину до маршруту мурахи
                path = np.append(path, new_nod)
                if j == (attractiveness_for_ant.shape[0] - 3):
                    path = np.append(path, np.setdiff1d(nods, path))

            distance = lenghts[path[0], path[-1]]
            for j in range(len(path) - 1):
                distance += lenghts[path[j], path[j+1]]
            ant_pathes.append((path, distance))

        ant_pathes = sorted(ant_pathes, key=lambda x:x[1])

        if ant_pathes[0][1] < best_path[1]:
            best_path = ant_pathes[0]

        if global_best_distance[-1] > best_path[1]:
            global_best_distance = np.append(global_best_distance, best_path[1])
        else:
            global_best_distance = np.append(global_best_distance, global_best_distance[-1])

        history_best_path.append(ant_pathes[0][0])
        history_best_distence = np.append(history_best_distence, ant_pathes[0][1])


        pheromone_matrix *= (1 - evaporation_rate)

        for ant in range(num_ants):
            a_path = ant_pathes[ant][0]
            delta = Q / ant_pathes[ant][1]

            pheromone_matrix[a_path[-1], a_path[0]] += delta
            pheromone_matrix[a_path[0], a_path[-1]] += delta
            for j in range(a_path.shape[0] - 1):

                pheromone_matrix[a_path[j], a_path[j+1]] += delta
                pheromone_matrix[a_path[j+1], a_path[j]] += delta

        attractiveness = (pheromone_matrix ** a) * ((Q / lenghts) ** b)
        np.fill_diagonal(attractiveness , 0)
    
        if i > 30:
            if history_best_distence[-1] == history_best_distence[-2] == history_best_distence[-3] == history_best_distence[-4] == history_best_distence[-5] == history_best_distence[-6] == history_best_distence[-7] == history_best_distence[-8] == history_best_distence[-9]:
                break
    
    return history_best_distence

def together(num_cities, a, b, Q, evaporation_rate, num_ants):
    def1 = create_matrix(num_cities, a, b, Q)
    coords = def1[4]

    history_best_distence = algorithm(evaporation_rate, num_ants, def1[0], def1[1], def1[2], def1[3], a, b, Q)
    return [coords, history_best_distence]