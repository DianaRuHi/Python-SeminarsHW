# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# (1+n!)^n     ???

n = int(input('Введите число: '))
list = []
fac = 1
sum = 0
for i in range(1, n + 1):
    fac *= i 
    list.append((1+fac)**i)
    sum += list[i-1]
print(list)
print(sum)