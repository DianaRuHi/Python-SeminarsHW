from modul_txt import out_txt, in_txt
from modul_json import out_json, in_json
from modul_csv import out_csv, in_csv

def run():
    action = int(input('Что вы хотите сделать? \n1 - Увидеть содержимое справочника \n2 - Записать новую информацию в справочник \n: '))
    type = input('Какой формат файла вам нужен? (json, csv, txt)\n: ')
    if action == 1:
        if type == 'txt':
            out_txt()
        if type == 'json':
            out_json()  
        if type == 'csv':
            out_csv()

    if action == 2 and (type == 'txt' or type == 'json' or type == 'csv'):
        fio = input('Введите ФИО человека: ')
        number = input('Введите номер человека: ')
        description = input('Введите описание: ')
        if type == 'txt':
            in_txt(fio, number, description)
        if type == 'json':
            in_json(fio, number, description)
        if type == 'csv':
            in_csv(fio, number, description)
