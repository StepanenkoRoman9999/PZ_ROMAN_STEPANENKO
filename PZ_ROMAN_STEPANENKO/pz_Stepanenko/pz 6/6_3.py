#3. Дано множество A из N точек (N > 2, точки заданы своими координатами x, у). Найти
#наибольший периметр треугольника, вершины которого принадлежат различным
#точкам множества A, и сами эти точки (точки выводятся в том же порядке, в котором они перечислены при задании множества A).
#Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по формуле:
#R = √(x2 – x1)2 + (у2 – y1)2
#Для хранения данных о каждом наборе точек следует использовать по два список: первый
#список для хранения абсцисс, второй — для хранения ординат.
import math
import random
n = int(input("Введи количество точек N: "))
x_list = []
y_list = []
t = 0
while t < n:
    x_list.append(random.randint(-10, 10))
    y_list.append(random.randint(-10, 10))
    t += 1
print("Исходные точки")
for i in range(n):
    print(f"Точка {i}: ({x_list[i]}, {y_list[i]})")
max_p = -1
best_i, best_j, best_k = -1, -1, -1
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            d1 = math.sqrt((x_list[j] - x_list[i]) ** 2 + (y_list[j] - y_list[i]) ** 2)
            d2 = math.sqrt((x_list[k] - x_list[j]) ** 2 + (y_list[k] - y_list[j]) ** 2)
            d3 = math.sqrt((x_list[i] - x_list[k]) ** 2 + (y_list[i] - y_list[k]) ** 2)
            p = d1 + d2 + d3
            if p > max_p:
                max_p = p
                best_i, best_j, best_k = i, j, k
print("Результат работы")
print(f"Наибольший периметр: {round(max_p, 2)}")
print("Вершины треугольника:")
print(f"Точка {best_i}: ({x_list[best_i]}, {y_list[best_i]})")
print(f"Точка {best_j}: ({x_list[best_j]}, {y_list[best_j]})")
print(f"Точка {best_k}: ({x_list[best_k]}, {y_list[best_k]})")