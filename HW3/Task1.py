# Задайте список из нескольких чисел. Напишите программу, которая 
# найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

list_num = [int(i) for i in input('Введите строку из элементов: ').split()]

print('На нечетных позициях элементы ', end=' ')
summa = 0
for i in range(1, len(list_num), 2):
    summa += list_num[i]
    print(f'{list_num[i]}', end=', ')
print(f'ответ: {summa}')