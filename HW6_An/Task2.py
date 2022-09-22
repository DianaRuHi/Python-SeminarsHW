# Задача: предложить улучшения кода для уже решённых задач(не менее 4 задач нужно улучшить):
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

#1
# Напишите программу, которая принимает на вход число N и 
# выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
import math
n = int(input('Введите число: '))
print(list(map(lambda x: math.factorial(x), range(1, n+1))))

#2
# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.
lis = [int(i) for i in input('Введите последовательность: ').split()]
print(list(filter(lambda x: lis.count(x) == 1, lis)))

#3
# Напишите программу, удаляющую из текста все слова, содержащие "абв".
text = [i for i in input ('Введите текст: ').split()]
print(' '.join(list(filter(lambda x: not 'абв' in x.lower(), text))))

#4
# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль (он собирает с данного куста и двух по бокам), находясь 
# перед некоторым кустом заданной на круговой грядке.
berry = [int(i) for i in input('Введите количество ягод на каждом кусте: ').split()]
print(max(list(map(lambda x: berry[x-1] + berry[x] + berry[(x+1)%(len(berry))], range(len(berry))))))
