from ast import dump
import json

def view_all():
    with open('HW8/workers(json).txt') as f:
        data = json.load(f)
        for d in data:
                print (d + ' '*(5 - len(d)) + data[d][0] + ' '*(15-len(data[d][0])) + data[d][1] + ' '*(15-len(data[d][1])) + data[d][2] + ' '*(15-len(data[d][2])) + data[d][3] + ' '*(15-len(data[d][3])) + data[d][4] + ' '*(15-len(data[d][4]))  + data[d][5] + ' '*(15-len(data[d][5])))
