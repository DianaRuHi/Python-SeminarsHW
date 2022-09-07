# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, находясь 
# перед некоторым кустом заданной во входном файле грядки.

with open('HW2_Prog/Task5r.txt', 'r') as f:
    len = int(f.readline())
    lis = [int(i) for i in f.readline().split()]

count = []
for i in range(len):
    count.append(lis[i-1] + lis[i] + lis[(i+1)%(len)])

with open('HW2_Prog/Task5w.txt', 'w') as f:
    print(max(count), file = f)
