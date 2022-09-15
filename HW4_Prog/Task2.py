# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

def is_simple(x):
    for i in range (2, x//2 + 1):
        if x % i == 0:
            return False
    return True
def razloj(n):
    lis = [i for i in range(2, n) if n % i == 0 and is_simple(i)]
    lis2 =[]
    ind = 0
    while n != 0:
        if n % lis[ind] == 0:
            lis2.append(lis[ind])
            n = n / lis[ind]
        else:
            ind += 1
        if ind >= len(lis):
            n = 0
    return lis2

num = int(input('Ведите натуральное число: '))
if is_simple(num) or num == 1:
    print('Простых множителей нет')
else:
    print(razloj(num)) #Разложение на простые множители