# Создайте программу для игры в ""Крестики-нолики""
import time

def vivodPole(lis, h):
    with open('HW5\Task3.txt', 'w+') as f:
        f.write('Now is '+ h + ' turn.\n')
        for i in lis:
            f.write(i+'\n')

def vvod():
    with open('HW5\Task3.txt', 'r') as f:
        lis = f.readlines()
    flag = 1
    while flag:
        with open('HW5\Task3.txt', 'r') as f:
            time.sleep(1)
            lis1 = f.readlines()
            for i in range(1, len(lis)):
                for j in range(len(lis[1])):
                    if lis[i][j] != lis1[i][j]:
                        x = i
                        y = j
                        flag = 0
    return [x-1, y, lis[x][y], lis1[x][y]]

def win(lis):
    if lis[0][1] == lis [0][5] and lis[0][1] == lis [0][9] and lis[0][1] != '-':
        return lis[0][1]
    if lis[2][1] == lis [2][5] and lis[2][1] == lis [2][3] and lis[2][1] != '-':
        return lis[2][1]
    if lis[4][1] == lis [4][5] and lis[4][1] == lis [4][9] and lis[4][1] != '-':
        return lis[4][1]
    if lis[0][1] == lis [2][1] and lis[0][1] == lis [4][1] and lis[0][1] != '-':
        return lis[0][1]    
    if lis[0][5] == lis [2][5] and lis[0][5] == lis [4][5] and lis[0][5] != '-':
        return lis[0][5] 
    if lis[0][9] == lis [2][9] and lis[0][9] == lis [4][9] and lis[0][9] != '-':
        return lis[0][9] 
    if lis[0][1] == lis [2][5] and lis[0][1] == lis [4][9] and lis[0][1] != '-':
        return lis[0][1] 
    if lis[0][9] == lis [2][5] and lis[0][9] == lis [4][1] and lis[0][9] != '-':
        return lis[0][9] 
    return ''

pole = [' - | - | - ','___|___|___',' - | - | - ','___|___|___',' - | - | - ']
hod = {0:'X', 1:'O'}
ind_hod = 0

for i in range(9):
    vivodPole(pole, hod[ind_hod])
    flag = 1
    while flag:
        move = vvod()
        if move[2] == '-' and move[3] == hod[ind_hod]:
            flag = 0
        else:
            vivodPole(pole, hod[ind_hod])
            with open('HW5\Task3.txt', 'a') as f:
                f.write('You made a mistake, try again.\n')
    pole[move[0]] = list(pole[move[0]])
    pole[move[0]][move[1]] = hod[ind_hod]
    pole[move[0]] = "".join(pole[move[0]])
    
    if win(pole) != '':
        with open('HW5\Task3.txt', 'a') as f:
            f.write('The winner is ' + hod[ind_hod] + '\n')
            f.write('Congratulations!!!')
        break
    if i == 8:
        with open('HW5\Task3.txt', 'a') as f:
            f.write('Draw.')
    ind_hod = (ind_hod + 1)%2



