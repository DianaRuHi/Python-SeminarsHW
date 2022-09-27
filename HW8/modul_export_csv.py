from ast import dump
import json
import csv

def in_csv():
    with open('HW8/workers(json).txt') as f:
        data = json.load(f)
    data_csv =[]
    for d in data:
        line_csv =[d]
        for i in data[d]:
            line_csv.append(i)
        data_csv.append(line_csv)
    with open('HW8/workers.csv', 'w',  newline='') as f:
        csv.writer(f, delimiter=';', quoting=csv.QUOTE_NONE).writerows(data_csv)
    print('Данные экспортированны в формат csv.')
