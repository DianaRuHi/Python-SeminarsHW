from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import csv
from transliterate import translit

def log(update, context):
    try:
        msg = translit(update.message.text, reversed=True)
    except:
        msg = update.message.text
    try:
        name = update.effective_user.first_name
    except:
        name = 'Somthing goes wronG'
    data_csv = [[name, update.effective_user.id, msg, update.message.date]]
    with open('spy.csv', 'a+', newline='') as file:
        csv.writer(file, delimiter=';', quoting=csv.QUOTE_NONE).writerows(data_csv)

