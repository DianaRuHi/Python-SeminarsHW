from ast import dump
import json

def find():
    print('Что вы знаете о сотруднике, которого хотите найти? (если не знаете пишите DK): ')
    id = input('ID: ')
    info = []
    info.append(input('Surname: '))
    info.append(input('Name: '))
    info.append(input('Patronymic: '))
    info.append(input('Phone Number: '))
    info.append(input('Position: '))
    info.append(input('Salary: '))
    

    with open('HW8/workers(json).txt') as f:
        data = json.load(f)
        flag = 0
        for d in data:
            iter = 0
            if (id == 'DK' or id == d) and id != 'ID':
                for i in range(len(data[d])):
                    if data[d][i] == info[i] or info[i] == 'DK':
                        iter += 1
            if iter == len(data[d]):
                flag += 1
                print('Сотрудник отвечающий критериям поиска №', flag, ' :')
                print('ID: ' + d + '\nSurname: ' + data[d][0] + '\nName: ' + data[d][1] + '\nPatronymic: ' + data[d][2])
                print('Phone Number: ' + data[d][3] + '\nPosition: ' + data[d][4] + '\nSalary: ' + data[d][5])
        if flag == 0:
            print('Такого сотрудника нет.')
  