# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

num = int(input('Ведите натуральное число: '))

def is_simple(x):
    for i in range (2, x//2 + 1):
        if x % i == 0:
            return False
    return True

lis = [i for i in range(2, num) if num % i == 0 and is_simple(i)]
print(lis)

lis2 =[]
ind = 0
while num != 0:
    if num % lis[ind] == 0:
        lis2.append(lis[ind])
        num = num / lis[ind]
    else:
        ind += 1
    if ind >= len(lis):
        num = 0
print(lis2) #Разложение на простые множители
    