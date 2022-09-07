# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('Введите число: '))

list = range(-n,n+1)
mult = 1

with open('HW2_An/Task4r.txt', "r") as f:
    positions = f.readlines()


for i in range(len(positions)):
    mult *= list[int(positions[i][0])]

print(mult)    
