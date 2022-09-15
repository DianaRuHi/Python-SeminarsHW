# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
import re
import numbers

with open('HW4_An/Task4-1.txt','r') as fi:
    mn1 = fi.readline()

with open('HW4_An/Task4-2.txt','r') as fi:
    mn2 = fi.readline()

def razbit(st):
    lis1 = re.split(r'[\n*^ =]+', st)
    lis2 =[]
    for i in lis1:
        if (not '-' in i) and (not '+' in i):
            lis2.append(i)
        elif '-' in i:
            ind = i.find('-')
            lis2.append(i[:ind])
            lis2.append(i[ind:]) 
        elif '+' in i:
            ind = i.find('+')
            lis2.append(i[:ind])
            lis2.append(i[ind:])  
    for i in range(0, len(lis2)):
        if len(lis2[len(lis2)-i-1]) == 0: #Удаление пустых элементов
            lis2.pop(len(lis2)-i-1)
        if lis2[len(lis2)-i-1] == '+':
            lis2[len(lis2)-i-1] == '+1'
        if lis2[len(lis2)-i-1] == '-':
            lis2[len(lis2)-i-1] == '-1'
    if lis2[0] == 'x':
        lis2.insert(0, '+1')
    lis2.reverse()
    return lis2

mn1_lis = razbit(mn1)
mn2_lis = razbit(mn2)

res = [mn1_lis[0]]

ind1 = 1
ind2 = 1
flag = 1
while flag:
    if ind1 < len(mn1_lis) and ind2 < len(mn2_lis) and (not '-' in mn1_lis[ind1]) and (not '+' in mn1_lis[ind1]) and (not '-' in mn2_lis[ind2]) and (not '+' in mn2_lis[ind2]) and mn1_lis[ind1+1] == 'x' and  mn2_lis[ind2+1] == 'x':
        if mn1_lis[ind1] == mn2_lis[ind2]:
            res.append(mn1_lis[ind1])
            res.append(mn1_lis[ind1+1])
            res.append(int(mn1_lis[ind1+2])+int(mn2_lis[ind2+2]))
            if int(mn1_lis[ind1+2])+int(mn2_lis[ind2+2]) > 0:
                res.append('+')
            ind1 += 3
            ind2 +=3
        elif mn1_lis[ind1] < mn2_lis[ind2]:
            res.append(mn1_lis[ind1])
            res.append(mn1_lis[ind1+1])
            res.append(int(mn1_lis[ind1+2]))
            if int(mn1_lis[ind1+2]) > 0:
                res.append('+')
            ind1 += 3
        elif mn1_lis[ind1] > mn2_lis[ind2]:
            res.append(mn2_lis[ind2])
            res.append(mn2_lis[ind2+1])
            res.append(int(mn2_lis[ind2+2]))
            if int(mn2_lis[ind2+2]) > 0:
                res.append('+')
            ind2 += 3
    elif ind1 < len(mn1_lis) and ind2 < len(mn2_lis) and ('-' in mn1_lis[ind1] or '+' in mn1_lis[ind1]) and ('-' in mn2_lis[ind2] or '+' in mn2_lis[ind2]):
        res.append(int(mn1_lis[ind1])+int(mn2_lis[ind2]))
        if int(mn1_lis[ind1])+int(mn2_lis[ind2]) > 0:
            res.append('+')
        ind1 += 1
        ind2 += 1
    elif ind1 < len(mn1_lis) and ind2 < len(mn2_lis) and mn1_lis[ind1] == 'x' and  mn2_lis[ind2] == 'x':
        res.append(mn1_lis[ind1])
        res.append(int(mn1_lis[ind1+1])+int(mn2_lis[ind2+1]))
        if int(mn1_lis[ind1+1])+int(mn2_lis[ind2+1]) > 0:
            res.append('+')
        ind1 += 2
        ind2 += 2

    elif ind1 < len(mn1_lis) and ind2 < len(mn2_lis) and ('-' in mn1_lis[ind1] or '+' in mn1_lis[ind1]):
        res.append(int(mn1_lis[ind1]))
        if int(mn1_lis[ind1]) > 0:
            res.append('+')
        ind1 += 1
    elif ind1 < len(mn1_lis) and ind2 < len(mn2_lis) and ('-' in mn2_lis[ind2] or '+' in mn2_lis[ind2]):
        res.append(int(mn2_lis[ind2]))
        if int(mn2_lis[ind2]) > 0:
            res.append('+')
        ind2 += 1
    elif ind1 < len(mn1_lis) and ind2 < len(mn2_lis) and mn1_lis[ind1] == 'x':
        res.append(mn1_lis[ind1])
        res.append(int(mn1_lis[ind1+1]))
        if int(mn1_lis[ind1+1]) > 0:
            res.append('+')
        ind1 += 2
    elif ind1 < len(mn1_lis) and ind2 < len(mn2_lis) and mn2_lis[ind2] == 'x':
        res.append(mn2_lis[ind2])
        res.append(int(mn2_lis[ind2+1]))
        if int(mn2_lis[ind2+1]) > 0:
            res.append('+')
        ind2 += 2
    elif ind1 < len(mn1_lis) and ind2 < len(mn2_lis) and (not '-' in mn1_lis[ind1]) and (not '+' in mn1_lis[ind1]) and mn1_lis[ind1+1] == 'x':
        res.append(mn1_lis[ind1])
        res.append(mn1_lis[ind1+1])
        res.append(int(mn1_lis[ind1+2]))
        if int(mn1_lis[ind1+2]) > 0:
            res.append('+')
        ind1 += 3
    elif ind1 < len(mn1_lis) and ind2 < len(mn2_lis) and (not '-' in mn2_lis[ind2]) and (not '+' in mn2_lis[ind2]) and mn2_lis[ind2+1] == 'x':
        res.append(mn2_lis[ind2])
        res.append(mn2_lis[ind2+1])
        res.append(int(mn2_lis[ind2+2]))
        if int(mn2_lis[ind2+2]) > 0:
            res.append('+')
        ind2 += 3

    elif ind1 < len(mn1_lis) and ind2 >= len(mn2_lis) and (not '-' in mn1_lis[ind1]) and (not '+' in mn1_lis[ind1]) and mn1_lis[ind1+1] == 'x':
        res.append(mn1_lis[ind1])
        res.append(mn1_lis[ind1+1])
        res.append(int(mn1_lis[ind1+2]))
        if int(mn1_lis[ind1+2]) > 0:
            res.append('+')
        ind1 += 3
    elif ind1 >= len(mn1_lis) and ind2 < len(mn2_lis) and (not '-' in mn2_lis[ind2]) and (not '+' in mn2_lis[ind2]) and mn2_lis[ind2+1] == 'x':
        res.append(mn2_lis[ind2])
        res.append(mn2_lis[ind2+1])
        res.append(int(mn2_lis[ind2+2]))
        if int(mn2_lis[ind2+2]) > 0:
            res.append('+')
        ind2 += 3
    elif ind1 < len(mn1_lis) and ind2 >= len(mn2_lis) and ('-' in mn1_lis[ind1] or '+' in mn1_lis[ind1]):
        res.append(int(mn1_lis[ind1]))
        if int(mn1_lis[ind1]) > 0:
            res.append('+')
        ind1 += 1
    elif ind1 >= len(mn1_lis) and ind2 < len(mn2_lis) and ('-' in mn2_lis[ind2] or '+' in mn2_lis[ind2]):
        res.append(int(mn2_lis[ind2]))
        if int(mn2_lis[ind2]) > 0:
            res.append('+')
        ind2 += 1
    elif ind1 < len(mn1_lis) and ind2 >= len(mn2_lis) and mn1_lis[ind1] == 'x':
        res.append(mn1_lis[ind1])
        res.append(int(mn1_lis[ind1+1]))
        if int(mn1_lis[ind1+1]) > 0:
            res.append('+')
        ind1 += 2
    elif ind1 >= len(mn1_lis) and ind2 < len(mn2_lis) and mn2_lis[ind2] == 'x':
        res.append(mn2_lis[ind2])
        res.append(int(mn2_lis[ind2+1]))
        if int(mn2_lis[ind2+1]) > 0:
            res.append('+')
        ind2 += 2
    else:
        flag = 0
res.reverse()
print (res)

with open('HW4_An/Task5.txt','w') as fi:
    resul = ''
    ind = 0
    if res[ind] == '+':
        ind += 1
    while ind < len(res) - 1:
        if res[ind] == 0:
            if res[ind+1] == '0':
                ind += 1
            elif res[ind+2] == '+' or res[ind+2] == '-' or res[ind+2] == '0':
                ind += 2
            else:
                ind += 3
        elif res[ind+1] == 'x' and res[ind] == 1:
            ind += 1
        elif res[ind+1] == 'x' and res[ind] == -1:
            resul += '-'
            ind += 1    

        elif res[ind+1] == 'x':
            resul += str(res[ind]) + '*'
            ind += 1
        elif res[ind] == 'x' and res[ind+1] != '+' and (not '-' in str(res[ind+1])) and res[ind+1] != '0':
            resul += str(res[ind]) + '^'
            ind += 1
        else: 
            resul += str(res[ind])
            ind += 1
    resul += '=0'
    print(resul, file = fi)
