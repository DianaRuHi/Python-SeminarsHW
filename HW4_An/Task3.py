# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

lis = [int(i) for i in input('Введите последовательность чисел через пробелы: ').split()]
lis2 = []
for i in range(len(lis)):
    if lis[i] not in lis2:
        lis2.append(lis[i])

print(lis2)
