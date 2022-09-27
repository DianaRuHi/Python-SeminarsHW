from ast import dump
import json

def add_new():
    print('Введите информацию о сотруднике, которого хотите добавить.')
    info = []
    info.append(input('Surname: '))
    info.append(input('Name: '))
    info.append(input('Patronymic: '))
    info.append(input('Phone Number: '))
    info.append(input('Position: '))
    info.append(input('Salary: '))

    with open('HW8/workers(json).txt') as f:
        data = json.load(f)
        id = str(len(data))
        data[id] = info
    with open('HW8/workers(json).txt', 'w') as f:
        json.dump(data, f)
    print ('Сотрудник добавлен.')
