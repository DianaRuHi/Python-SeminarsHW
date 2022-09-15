# Задана натуральная степень k. Сформировать случайным 
# образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

k = int(input('Введите натуральную степень: '))
rd_lis = [ random.randint(0, 100) for i in range(k+1)]
print(rd_lis)

with open('HW4_An/Task4-1.txt','w') as fi:
    stri = ''
    for i in range(k+1):
        if rd_lis[i] != 0 and k-i > 1:
            stri += str(rd_lis[i]) + '*x^'+ str(k-i)
        elif rd_lis[i] != 0 and k-i == 1:
           stri += str(rd_lis[i]) + '*x'
        elif rd_lis[i] != 0 and k-i == 0:
            stri += str(rd_lis[i])
        if sum(rd_lis[i+1:]) !=0:
            stri += '+'
    stri += '=0'
    print(stri, file = fi)

k = int(input('Введите натуральную степень: '))
rd_lis = [ random.randint(-100, 100) for i in range(k+1)]
print(rd_lis)

with open('HW4_An/Task4-2.txt','w') as fi:
    stri = ''
    for i in range(k+1):
        if rd_lis[i] != 0 and k-i > 1:
            stri += str(rd_lis[i]) + '*x^'+ str(k-i)
        elif rd_lis[i] != 0 and k-i == 1:
           stri += str(rd_lis[i]) + '*x'
        elif rd_lis[i] != 0 and k-i == 0:
            stri += str(rd_lis[i])
        if i < k and rd_lis[i+1] >0:
            stri += '+'
    stri += '=0'
    print(stri, file = fi)
