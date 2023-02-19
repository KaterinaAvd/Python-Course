# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

n = int(input("Количество элементов массива: "))

import random
data = [random.randint(-100, 100) for i in range(n)]
print(data)

min = int(input("Задайте нижнюю границу диапазона: "))
max = int(input("Задайте верхнюю границу диапазона: "))

list_1 = list()
for i in range(n):
    if min < data[i] < max:
        list_1.append(i)

print(list_1)