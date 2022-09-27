from ast import dump
import json

def delete_worker():
    print('Введите ID сотрудника, которого хотите удалить.')
    id = input('ID: ')
    with open('HW8/workers(json).txt') as f:
        data = json.load(f)
    if id in list(data.keys()) and id != 'ID':
        
        data_new = {}
        for d in data:
            if d == 'ID':
                data_new[d] = data[d]
            elif int(d) < int(id):
                data_new[d] = data[d]
            elif int(d) > int(id):
                data_new[str(int(d)-1)] = data[d]
        with open('HW8/workers(json).txt', 'w') as f:
            json.dump(data_new, f)
        print ('Сотрудник удален.')
    else:
        print('Такого сотрудника нет.')
