#Дана последовательность из N целых чисел и число K. Необходимо 
# сдвинуть всю последовательность (сдвиг - циклический) на |K| элементов 
# вправо, если K – положительное и влево, если отрицательное.

with open('HW3/DopR.txt', 'r') as file:
    lenn = int(file.readline())
    lis = [int(i) for i in file.readline().split()]
    k = int(file.readline())

lis_new = []
for i in range(lenn):
    lis_new.append(lis[(i-k) % lenn])

with open('HW3/DopW.txt','a') as file:
    print(lis_new, file=file)
