from ast import dump
import json

def redate():
    print('Введите ID и новые данные сотрудника.')
    id = input('ID: ')
    with open('HW8/workers(json).txt') as f:
        data = json.load(f)
    if id in list(data.keys()) and id != 'ID':
        info = []
        info.append(input('Surname: '))
        info.append(input('Name: '))
        info.append(input('Patronymic: '))
        info.append(input('Phone Number: '))
        info.append(input('Position: '))
        info.append(input('Salary: '))
        data[id] = info
        with open('HW8/workers(json).txt', 'w') as f:
            json.dump(data, f)
        print ('Данные сотрудника обновлены.')
    else:
        print('Такого сотрудника нет.')
