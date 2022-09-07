# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

with open('HW2_Prog/Task3r.txt', 'r') as f:
    n = int(f.readline())

flag = 2
while flag != 0:
    if n % flag == 0:
        with open('HW2_Prog/Task3w.txt', 'w') as f:
            print(flag, file = f)
        flag = 0    
    else:
        flag += 1
