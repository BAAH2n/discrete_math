import timeit
import functions as f
import pandas as pd

numbers_cities = [25, 250, 500]
num_iterations = 150
a = 1
b = 3
Q = 1
evaporation_rate = 0.2
num_ants = 100

execution_time = []


for num_cities in numbers_cities:
    execution_time.append(timeit.timeit("f.together(num_cities, a, b, Q, evaporation_rate, num_ants)", globals=globals(), number=3))
    print(f"Ітерація для {num_cities} міст завершилась")

d = {
    "Кількість міст (вершин)": numbers_cities,
    "Кількість проходок по всьому графу": num_iterations,
    "Кількість мурах": num_ants,
    "Середній час виконання алгоримту (у хвилинах)": execution_time
}   
df = pd.DataFrame(data=d) 
df["Складність"] = df["Кількість міст (вершин)"]**2 * num_iterations * num_ants
df["Середній час виконання алгоримту (у хвилинах)"] = round(df["Середній час виконання алгоримту (у хвилинах)"]/60, 2)
df.to_csv("experiment.csv")
print (df)