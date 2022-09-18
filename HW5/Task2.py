# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг 
# после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать 
# не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
from dataclasses import replace
import random
import time

def vvod():
    with open('HW5\Task2.txt', 'r') as f:
        text = f.read()
    flag = 1
    while flag:
        with open('HW5\Task2.txt', 'r') as f:
            time.sleep(1)
            lines = f.read()
            if lines != text:
                flag = 0          
    return(lines.replace(text, ''))

def vivod(txt):
    with open('HW5\Task2.txt', 'a') as f:
        f.write('\n'+ txt)

candies = 2021 # В файле 100 чтобы игра была короче

with open('HW5\Task2.txt', 'w+') as f:
    f.write('There is a 2021 candy on the table. Two players are playing making a move after each other.')
    f.write('\nThe first move is determined by drawing lots. In one move, you can pick up no more than 28 candies.')
    f.write('\nAll the opponents candies go to the one who made the last move.\n')
    f.write('\nNOTE: If a player tries to take more than 28 candies, it is regarded as cheating and the player automatically loses!\n')

vivod('Choose who you want to play with (1 - a person, 2 - a bot, 3 - a smart bot): ')
mode = int(vvod())

if mode == 1:
    vivod('Name of the first player: ')
    players ={}
    players[0] = vvod()
    vivod('Name of the second player: ')
    players[1] = vvod()

    hod = random.randint(0, 1)
    vivod('The order of the move is determined randomly.')
    vivod('The first one will be ' + players[hod] + '.')
    while candies > 0:
        vivod('Candies left ' + str(candies))
        vivod(players[hod] + ' takes candies: ')
        takes = int(vvod())
        tr = 0 
        while takes <= 0 and tr < 5 :
            vivod('You cant take candies <= 0, try again.')
            vivod('Candies: ')
            takes = int(vvod())
            tr += 1
        if tr >= 5:
            vivod('Too many tries, ' + players[hod] + ' lose.')
            vivod('The winner is ' + players[(hod+1)%2])
            vivod('Congratulations ' + players[(hod+1)%2]+'!!!')
            break
        if takes > 28:
            vivod('You are cheating! '+ players[hod] + ' lose.')
            vivod('The winner is ' + players[(hod+1)%2])
            vivod('Congratulations ' + players[(hod+1)%2]+'!!!')
            break
        candies -= takes
        if candies <= 0:
            vivod('The winner is ' + players[hod])
            vivod('Congratulations ' + players[hod]+'!!!')
        hod = (hod+1)%2

else:
    vivod('Your name: ')
    players ={}
    players[1] = vvod()
    if mode == 2:
        players[0] = 'Bot'
        f = lambda left: random.randint(1, 28)
    if mode == 3:
        players[0] = 'Smart Bot'
        f = lambda left: left%29 if left%29 !=0 else random.randint(1, 28)
    
    hod = random.randint(0, 1)
    vivod('The order of the move is determined randomly.')
    vivod('The first one will be ' + players[hod] + '.')
    while candies > 0:
        vivod('Candies left ' + str(candies))
        if hod == 0:
            takes = f(candies)
            vivod(players[0] + ' takes candies ' + str(takes))
        else:
            vivod(players[hod] + ' takes candies: ')
            takes = int(vvod())
        tr = 0
        while takes <= 0 and tr < 5 :
            vivod('You cant take candies <= 0, try again.')
            vivod('Candies: ')
            takes = int(vvod())
            tr += 1
        if tr >= 5:
            vivod('Too many tries, ' + players[1] + ' lose.')
            vivod('The winner is ' + players[0])
            break
        if takes > 28:
            vivod('You are cheating! '+ players[1] + ' lose.')
            vivod('The winner is ' + players[0])
            break
        candies -= takes
        if candies <= 0:
            vivod('The winner is ' + players[hod])
            if hod == 1:
                vivod('Congratulations ' + players[hod]+'!!!')
        hod = (hod+1)%2
