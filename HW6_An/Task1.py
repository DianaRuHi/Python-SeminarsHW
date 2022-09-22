# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# *Пример:* 
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

lis = [int(i) for i in input('Введите последовательность через пробел: ').split()]
lis2 = []
for i in range(len(lis)):
    num = lis[i]
    lis.pop(i)
    if not num in lis:
        lis2.append(num)
    lis.insert(0, num)
print(lis2)
