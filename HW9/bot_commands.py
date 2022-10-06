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
import wikipedia
import ast

def help(update, context):
    log(update,context)
    context.bot.send_message(update.effective_chat.id, "Cписок команд: ")
    context.bot.send_message(update.effective_chat.id, "/start - приветствие")
    context.bot.send_message(update.effective_chat.id, "/wiki + текст - ищет определение в википедии")
    context.bot.send_message(update.effective_chat.id, "/abv_del + текст - удаляет из следующего после текста все слова содержащие 'aбв' ")
    context.bot.send_message(update.effective_chat.id, "/candy_game - игра про конфетки")
    context.bot.send_message(update.effective_chat.id, "/calc - небольшой калькулятор для рациональных и комплексных чисел")
    context.bot.send_message(update.effective_chat.id, "/tel_directory - телефонный справочник с возможностью выгрузить файл")
    context.bot.send_message(update.effective_chat.id, "/x_o_game - крестики нолики") 
    context.bot.send_message(update.effective_chat.id, "/score21 - игра 21 очко")
    context.bot.send_message(update.effective_chat.id, "/my_score - узнать ваш счет игр с ботом")

    context.bot.send_message(update.effective_chat.id, "/help - список существующих команд")

def start(update, context):
    log(update,context)
    try:
        name = update.effective_user.first_name
    except:
        name = 'Somthing goes wronG'
    context.bot.send_message(update.effective_chat.id, f'Привет, {name}!')

def voice(update, context):
    log(update,context)
    context.bot.send_message(update.effective_chat.id, "Надоели Ваши голосовые сообщения... я пока не умею их читать!")

def unknown_command(update, context):
    log(update,context)
    context.bot.send_message(update.effective_chat.id, "Пока такой команды нет, посмотрите /help")

def abv_del(update, context):
    log(update,context)
    text = update.message.text
    lis = [i for i in text.split()]
    lis1 = []
    for i in range(1, len(lis)):
        if not 'абв' in lis[i].lower():
            lis1.append(lis[i])
    res = ''
    for i in lis1:
        res += i + ' '
    context.bot.send_message(update.effective_chat.id, res)

def cancel(update, context):
    log(update,context)
    context.bot.send_message(update.effective_chat.id, 'Игра закончена!')


wikipedia.set_lang('ru')

def wiki(update, context):
    log(update, context)
    text = ' '.join(context.args)
    try:
        result = wikipedia.summary(text, sentences=2)
        context.bot.send_message(update.effective_chat.id, result)
    except:
        context.bot.send_message(update.effective_chat.id, 'Не найдено!')

def spy_load(update, context):
    log(update, context)
    try:
        context.bot.send_document(update.message.chat.id, document = open('spy.csv', 'rb'))
    except:
        context.bot.send_message(update.effective_chat.id, "Что-то пошло не так.")

def unknown_text(update, context):
    log(update, context)
    context.bot.send_message(update.effective_chat.id, "Я вас не понимаю, посмотрите /help")

def my_score(update, context):
    log(update, context)
    with open('crore_of_all_games.txt', 'r') as f:
        data = f.readlines()
    score = ast.literal_eval(data[0])
    if update.effective_user.id not in list(score.keys()):
        context.bot.send_message(update.effective_chat.id, "Вы еще не сыграли со мной ни в одну игру...")
    else:
        my_score = score[update.effective_user.id]
        context.bot.send_message(update.effective_chat.id, f"Вы выиграли {my_score[0]} игр, а я стал победителем в {my_score[1]} играх, ничьих же было {my_score[2]}.")
