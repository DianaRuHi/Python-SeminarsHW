# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import math

lis = [int(i) for i in input('Введите строку из элементов: ').split()]
lis_new=[]
for i in range(math.ceil(len(lis)/2)):
    lis_new.append(lis[i]*lis[len(lis)-i-1])
print(lis_new)
