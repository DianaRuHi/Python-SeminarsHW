from ast import dump
import json

def pos_selection():
    print('Напишите должность сотрудников, список которых хотите увидеть. ')
    position = input('Position: ')

    with open('HW8/workers(json).txt') as f:
        data = json.load(f)
        count = 0
        for d in data:
            if d == 'ID' or data[d][4] == position:
                count += 1
                print (d + ' '*(5 - len(d)) + data[d][0] + ' '*(15-len(data[d][0])) + data[d][1] + ' '*(15-len(data[d][1])) + data[d][2] + ' '*(15-len(data[d][2])) + data[d][3] + ' '*(15-len(data[d][3])) + data[d][4] + ' '*(15-len(data[d][4]))  + data[d][5] + ' '*(15-len(data[d][5])))
        if count == 1:
            print('Таких сотрудников нет.')
