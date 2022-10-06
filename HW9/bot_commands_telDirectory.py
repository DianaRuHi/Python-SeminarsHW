from asyncore import write
from ctypes.wintypes import HACCEL
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from random import randint
from spy import log 
from fractions import Fraction
from ast import dump
import json
import os
import csv


F = 5
G = 6
H = 7
I = 8
J = 9

def tel_directory(update, context):
    log(update, context)
    context.bot.send_message(update.effective_chat.id, "Что вы хотите сделать с телефонным справочником?\n1 - добавить новый контакт\n2 - выгрузить данные")
    return F

def action_tel(update, context):
    log(update, context)
    if update.message.text == '1':
        context.bot.send_message(update.effective_chat.id, 'Напишите ФИО нового контакта (предпочтительнее на английском).')
        return G
    elif update.message.text == '2':
        context.bot.send_message(update.effective_chat.id, 'В каком формате вы хотите выгрузить данные?\n1 - txt\n2 - json(txt)\n3 - csv')
        return J
    else:
        context.bot.send_message(update.effective_chat.id, 'Неверный ввод, попробуйте выбрать действие еще раз.')
        return F

def fio_tel(update, context):
    log(update, context)
    with open('tel_temp.txt', 'w+') as f:
        f.write(update.message.text)
    context.bot.send_message(update.effective_chat.id, 'Напишите телефон нового контакта.')
    return H

def tel_tel(update, context):
    log(update, context)
    with open('tel_temp.txt', 'a+') as f:
        f.write('///' + update.message.text)
    context.bot.send_message(update.effective_chat.id, 'Напишите описание к новому контакту (предпочтительнее на английском).')
    return I

def info_tel(update, context):
    log(update, context)
    with open('tel_temp.txt', 'a+') as f:
        f.write('///' + update.message.text)
    with open('tel_temp.txt', 'r') as f:
        contact = [i for i in f.read().split('///')]

    with open('tel.txt', 'a+') as f:
        f.write(contact[0] + ' - ' + contact[1] + ' - ' + contact[2] + '\n')

    with open('tel.csv', newline='') as f:
        if os.path.getsize('tel.csv') > 0:
            data = list(csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE))
            data.append([contact[0],contact[1],contact[2]])
        else:
            data = [['FIO','Number','Description'],[contact[0],contact[1],contact[2]]]
    with open('tel.csv', 'w+',  newline='') as f:
        csv.writer(f, delimiter=';', quoting=csv.QUOTE_NONE).writerows(data)
   
    with open('tel(json).txt') as f:
        if os.path.getsize('tel(json).txt') > 0:
            data = json.load(f)
            ind = len(data) + 1
        else:
            data = {}
            ind = 1
    data[ind] = [{'FIO':contact[0], 'NUMBER': contact[1],'DESCRIPTION':contact[2]}]
    with open('tel(json).txt', 'w') as f:
        json.dump(data, f)

    context.bot.send_message(update.effective_chat.id, 'Контакт сохранен.')
    return ConversationHandler.END 

def load_tel(update, context):
    log(update, context)
    if update.message.text == '1':
        context.bot.send_document(update.message.chat.id, document = open('tel.txt', 'rb'))
        return ConversationHandler.END 
    elif update.message.text == '2':
        context.bot.send_document(update.message.chat.id, document = open('tel(json).txt', 'rb'))
        return ConversationHandler.END 
    elif update.message.text == '3':
        context.bot.send_document(update.message.chat.id, document = open('tel.csv', 'rb'))
        return ConversationHandler.END 
    else:
        context.bot.send_message(update.effective_chat.id, 'Неверный ввод, попробуйте выбрать формат еще раз.')
        return J


