# Реализуйте алгоритм перемешивания списка.
import random

list = [i for i in range(10)]
print(list)

for i in range(20):
    r1 = random.randint(0, len(list)-1)
    r2 = random.randint(0, len(list)-1)
    temp = list[r1]
    list[r1] = list[r2]
    list[r2] = temp
print(list)
