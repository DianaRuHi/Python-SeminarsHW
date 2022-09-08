# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import math

lis = [abs(float(i)) for i in input('Введите строку из элементов: ').split()]
print(lis)

min_ch = lis[0] - math.floor(lis[0])
max_ch = lis[0] - math.floor(lis[0])


for i in lis:
    if i - math.floor(i) < min_ch:
        min_ch = i - math.floor(i)
    if i - math.floor(i) > max_ch:
        max_ch = i - math.floor(i)
print(max_ch - min_ch) # в конце появляются лишние цифры, что-то с этим сделать не получается 
