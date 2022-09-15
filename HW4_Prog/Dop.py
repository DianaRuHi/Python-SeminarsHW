# В первой строке находятся целые числа M и N (1  ≤ M ≤ N ≤ 1 000 000).
# Выходные данные
# В каждой строке вывести по паре чисел через пробел. Первое 
# число пары должно быть меньше второго. Строки должны 
# быть отсортированы в порядке возрастания первого числа пары. 
# Если пар дружественных чисел в промежутке нет, вывести "Absent"

def mn_razloj(n):
    lis =[1]
    ind = 0
    for i in range(2, n//2+1):
        if n % i == 0:
            lis.append(i)
    return lis

nums = [int(i) for i in input('Введите числа: ').split()]
res =[]

for i in range(nums[0], nums[1]+1):
    j = sum(mn_razloj(i))
    if i == sum(mn_razloj(j)) and i < j < nums[1]:
        res.append(i)
        res.append(j)
for i in range(0, len(res), 2):
    print(res[i], res[i+1])
