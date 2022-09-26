import csv
import os

def in_csv(fio, number, description):
    with open('HW7/csv.csv', newline='') as f:
        if os.path.getsize('HW7/csv.csv') > 0:
            data = list(csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE))
            data.append([fio,number,description])
        else:
            data = [['FIO','Number','Description'],[fio,number,description]]
    with open('HW7/csv.csv', 'w+',  newline='') as f:
        csv.writer(f, delimiter=';', quoting=csv.QUOTE_NONE).writerows(data)

def out_csv():
    with open('HW7/csv.csv', newline='') as f:
        data = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
        for raw in data:
            print(raw[0] + ' '*(20 - len(raw[0])) + raw[1] + ' '*(15 - len(raw[1])) + raw[2])
