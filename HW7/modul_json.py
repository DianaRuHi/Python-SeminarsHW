from ast import dump
import json
import os

def in_json(fio, number, description):
    with open('HW7/json.txt') as f:
        if os.path.getsize('HW7/json.txt') > 0:
            data = json.load(f)
            ind = len(data) + 1
        else:
            data = {}
            ind = 1
    data[ind] = [{'FIO':fio, 'NUMBER':number,'DESCRIPTION':description}]
    with open('HW7/json.txt', 'w') as f:
        json.dump(data, f)

def out_json():
    with open('HW7/json.txt') as f:
        data = json.load(f)
        for d in data:
            for id in data[d]:
                print('ФИО: ' + id['FIO'] + ' '*(25 - len('ФИО: ' + id['FIO'])) + 'Телефон: ' + id['NUMBER'] + ' '*(25 - len('Телефон: ' + id['NUMBER'])) + 'Описанрие: ' + id['DESCRIPTION'])
