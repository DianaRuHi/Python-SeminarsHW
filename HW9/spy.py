from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import csv
from transliterate import translit

def log(update, context):
    try:
        msg = translit(update.message.text, reversed=True)
    except:
        try:
            msg = update.message.text
        except:
            msg = 'Something goes wronG'
            print('msg 01')
    try:
        name = translit(update.effective_user.first_name, reversed=True)
    except:
        try:
            name = update.effective_user.first_name
        except:    
            name = 'Something goes wronG'
            print('name')
    try:
        id = update.effective_user.id
    except:
        id = 'Something goes wronG'
        print('id')
    try:
        time = update.message.date
    except:
        time = 'Something goes wronG'
        print('time')
    
    data_csv = [[name, id, msg, time]]
    try:
        with open('spy.csv', 'a+', newline='') as file:
            csv.writer(file, delimiter=';', quoting=csv.QUOTE_NONE).writerows(data_csv)
    except:
        try:
            with open('spy.csv', 'a+') as file:
                file.write(str(name) + ';' + str(id) + ';' + str(msg) + ';' + str(time) + '+++\n')
        except:
            print('Something goes VERY wronG')
