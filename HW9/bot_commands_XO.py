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

K = 10
L = 11
N = 12

def x_o_game(update, context):
    log(update, context)
    context.bot.send_message(update.effective_chat.id, 'Поиграем в крестики нолики!\nЧем ты хочешь играть? (x/o)')
    with open('x_o.txt', 'w+') as f:
        f.write('- - - - - - - - -')
    return K

def choice_x_o(update, context):
    log(update, context)
    text = update.message.text
    if text in 'xXхХ':
        context.bot.send_message(update.effective_chat.id, 'Ты ходишь первым.\nНапиши через пробел номер строки и номер столбца, куда хочешь поставить Х.')
        with open('x_o.txt', 'r') as f:
            pole = [i for i in f.read().split()]
        context.bot.send_message(update.effective_chat.id, f'{pole[0]} {pole[1]} {pole[2]}\n{pole[3]} {pole[4]} {pole[5]}\n{pole[6]} {pole[7]} {pole[8]}')
        return L
    elif text in 'oOоО0':
        context.bot.send_message(update.effective_chat.id, 'Тогда первым хожу я.')
        move = randint(0,8)
        with open('x_o.txt', 'r') as f:
            pole = [i for i in f.read().split()]
        pole[move] = 'X'
        context.bot.send_message(update.effective_chat.id, f'{pole[0]} {pole[1]} {pole[2]}\n{pole[3]} {pole[4]} {pole[5]}\n{pole[6]} {pole[7]} {pole[8]}')
        context.bot.send_message(update.effective_chat.id, 'Твой ход.\nНапиши через пробел номер строки и номер столбца, куда хочешь поставить О.')
        with open('x_o.txt', 'w') as f:
            f.write(' '.join(pole))
        return N
    else:
        context.bot.send_message(update.effective_chat.id, 'Неверный ввод, попробуй выбрать х или о еще раз.')
        return K

def x_game(update, context):
    log(update, context)
    text = [i for i in update.message.text.split()]
    try:
        if int(text[0])%2 == 0:
            move = int(text[0]) + int(text[1])
        else:
            move = int(text[0]) * (int(text[0]) - 1) + int(text[1]) - 1
    except:
        context.bot.send_message(update.effective_chat.id, 'Неверный ввод, попробуй написать номера еще раз.')
        return L
    if move > 8 or move < 0:
        context.bot.send_message(update.effective_chat.id, 'Неверный ввод номеров, попробуй написать еще раз.')
        return L
    else:
        with open('x_o.txt', 'r') as f:
            pole = [i for i in f.read().split()]
        if pole[move] != '-':
            context.bot.send_message(update.effective_chat.id, 'Клетка уже занята, выбери другую клетку.')
            return L
        else:
            pole[move] = 'X'
            context.bot.send_message(update.effective_chat.id, f'{pole[0]} {pole[1]} {pole[2]}\n{pole[3]} {pole[4]} {pole[5]}\n{pole[6]} {pole[7]} {pole[8]}') 
            if pole[0] == pole[1] == pole[2] == 'X' or pole[3] == pole[4] == pole[5] == 'X' or pole[6] == pole[7] == pole[8] == 'X' or pole[0] == pole[3] == pole[6] == 'X' or pole[1] == pole[4] == pole[7] == 'X' or pole[2] == pole[5] == pole[8] == 'X' or pole[0] == pole[4] == pole[8] == 'X' or pole[2] == pole[4] == pole[6] == 'X':
                context.bot.send_message(update.effective_chat.id, 'Ты победил!')

                with open('crore_of_all_games.txt', 'r') as f:
                    data = f.readlines()
                score = ast.literal_eval(data[0])
                id = update.effective_user.id
                if id not in list(score.keys()):
                    score[id] = [0, 0, 0]
                score[id][0] += 1
                with open('crore_of_all_games.txt', 'w+') as f:
                    f.write(str(score))
                return ConversationHandler.END 
            flag = 0
            for i in pole:
                if i == '-':
                    flag = 1
            if flag == 0:
                context.bot.send_message(update.effective_chat.id, 'Ничья!')

                with open('crore_of_all_games.txt', 'r') as f:
                    data = f.readlines()
                score = ast.literal_eval(data[0])
                id = update.effective_user.id
                if id not in list(score.keys()):
                    score[id] = [0, 0, 0]
                score[id][2] += 1
                with open('crore_of_all_games.txt', 'w+') as f:
                    f.write(str(score))
                return ConversationHandler.END
            
            context.bot.send_message(update.effective_chat.id, 'Мой ход.')
            bot_move = randint(0,8)
            while pole[bot_move] != '-':
                bot_move = randint(0,8)
            pole[bot_move] = 'O'
            context.bot.send_message(update.effective_chat.id, f'{pole[0]} {pole[1]} {pole[2]}\n{pole[3]} {pole[4]} {pole[5]}\n{pole[6]} {pole[7]} {pole[8]}') 
            if pole[0] == pole[1] == pole[2] == 'O' or pole[3] == pole[4] == pole[5] == 'O' or pole[6] == pole[7] == pole[8] == 'O' or pole[0] == pole[3] == pole[6] == 'O' or pole[1] == pole[4] == pole[7] == 'O' or pole[2] == pole[5] == pole[8] == 'O' or pole[0] == pole[4] == pole[8] == 'O' or pole[2] == pole[4] == pole[6] == 'O':
                context.bot.send_message(update.effective_chat.id, 'Я победил!')

                with open('crore_of_all_games.txt', 'r') as f:
                    data = f.readlines()
                score = ast.literal_eval(data[0])
                id = update.effective_user.id
                if id not in list(score.keys()):
                    score[id] = [0, 0, 0]
                score[id][1] += 1
                with open('crore_of_all_games.txt', 'w+') as f:
                    f.write(str(score))
                return ConversationHandler.END
            context.bot.send_message(update.effective_chat.id, 'Твой ход.')
        with open('x_o.txt', 'w') as f:
                f.write(' '.join(pole))
        return L


def o_game(update, context):
    log(update, context)
    text = [i for i in update.message.text.split()]
    try:
        if int(text[0])%2 == 0:
            move = int(text[0]) + int(text[1])
        else:
            move = int(text[0]) * (int(text[0]) - 1) + int(text[1]) - 1
    except:
        context.bot.send_message(update.effective_chat.id, 'Неверный ввод, попробуй написать номера еще раз.')
        return N
    if move > 8 or move < 0:
        context.bot.send_message(update.effective_chat.id, 'Неверный ввод номеров, попробуй написать еще раз.')
        return N
    else:
        with open('x_o.txt', 'r') as f:
            pole = [i for i in f.read().split()]
        if pole[move] != '-':
            context.bot.send_message(update.effective_chat.id, 'Клетка уже занята, выбери другую клетку.')
            return N
        else:
            pole[move] = 'O'
            context.bot.send_message(update.effective_chat.id, f'{pole[0]} {pole[1]} {pole[2]}\n{pole[3]} {pole[4]} {pole[5]}\n{pole[6]} {pole[7]} {pole[8]}') 
            if pole[0] == pole[1] == pole[2] == 'O' or pole[3] == pole[4] == pole[5] == 'O' or pole[6] == pole[7] == pole[8] == 'O' or pole[0] == pole[3] == pole[6] == 'O' or pole[1] == pole[4] == pole[7] == 'O' or pole[2] == pole[5] == pole[8] == 'O' or pole[0] == pole[4] == pole[8] == 'O' or pole[2] == pole[4] == pole[6] == 'O':
                context.bot.send_message(update.effective_chat.id, 'Ты победил!')
                return ConversationHandler.END 
            
            context.bot.send_message(update.effective_chat.id, 'Мой ход.')
            bot_move = randint(0,8)
            while pole[bot_move] != '-':
                bot_move = randint(0,8)
            pole[bot_move] = 'X'
            context.bot.send_message(update.effective_chat.id, f'{pole[0]} {pole[1]} {pole[2]}\n{pole[3]} {pole[4]} {pole[5]}\n{pole[6]} {pole[7]} {pole[8]}') 
            if pole[0] == pole[1] == pole[2] == 'X' or pole[3] == pole[4] == pole[5] == 'X' or pole[6] == pole[7] == pole[8] == 'X' or pole[0] == pole[3] == pole[6] == 'X' or pole[1] == pole[4] == pole[7] == 'X' or pole[2] == pole[5] == pole[8] == 'X' or pole[0] == pole[4] == pole[8] == 'X' or pole[2] == pole[4] == pole[6] == 'X':
                context.bot.send_message(update.effective_chat.id, 'Я победил!')
                return ConversationHandler.END
            flag = 0
            for i in pole:
                if i == '-':
                    flag = 1
            if flag == 0:
                context.bot.send_message(update.effective_chat.id, 'Ничья!')
                return ConversationHandler.END
            context.bot.send_message(update.effective_chat.id, 'Твой ход.')
        with open('x_o.txt', 'w') as f:
                f.write(' '.join(pole))
        return N
