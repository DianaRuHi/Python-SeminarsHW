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


A = 0
B = 1

def candy_game(update, context):
    log(update,context)
    context.bot.send_message(update.effective_chat.id, "Суть игры:\nНа столе лежат 2022 конфетки. Каждый из нас по очереди берет от 1 до 28 конфет, кто будет первым определяется случайно. Победит тот, кто заберет последюю конфетку. \nCыграем? (да/нет)")
    return A

def choice_game(update, context):
    log(update,context)
    text = update.message.text
    if 'да' in text.lower():
        if randint(1, 2) == 1:
            context.bot.send_message(update.effective_chat.id, "Твой ход, напиши количество конфеток, которые хочешь взять.")
            with open('candy.txt', 'w+') as f:
                f.write('2022')
            return B
        else:
            context.bot.send_message(update.effective_chat.id, f"Мой ход.\nЯ беру {2022%29} конфет, осталось {2022-2022%29} конфет на столе.\nТвой ход, напиши количество конфеток, которые хочешь взять.")
            with open('candy.txt', 'w+') as f:
                f.write(str(2022-2022%29))
            return B
    else:
        context.bot.send_message(update.effective_chat.id, "Очень жаль, а мне так хотелось поиграть с тобой :(")
        return ConversationHandler.END 

def plaer_move_game(update, context):
    log(update,context)
    try:
        move = int(update.message.text)
        if move > 28 or move < 1:
            context.bot.send_message(update.effective_chat.id, "Количество конфет должно быть строго от 1 до 28, выбери количество конфет исходя из условия.")
            return B
        else:
            with open('candy.txt', 'r') as f:
                candy = int(f.read())
            candy_new = candy - move    
            if candy_new < 0:
                context.bot.send_message(update.effective_chat.id, 'Ты не можешь взять конфет больше, чем их осталось на столе, попробуй сделать выбор еще раз.')
                return B
            elif candy_new == 0:
                context.bot.send_message(update.effective_chat.id, 'Конфет на столе не осталось, поздравляю, ты победил!')
                
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
            else:
                context.bot.send_message(update.effective_chat.id, f'Ты взял {move} конфет, осталось {candy_new} конфет на столе.\nМой ход.')
                if candy_new%29 == 0:
                    bot_move = randint(1, 28)
                else:
                    bot_move = candy_new%29 
                candy_new_bot = candy_new - bot_move
                if candy_new_bot == 0:
                    context.bot.send_message(update.effective_chat.id, f'Я взял {bot_move} конфет, конфет на столе не осталось, я победил!\nНе расстраивайся, ты обязательно победишь в следующий раз!')
                    
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
                else:
                    context.bot.send_message(update.effective_chat.id, f'Я взял {bot_move} конфет, осталось {candy_new_bot} конфет на столе.\nТвой ход.')
                    with open('candy.txt', 'w+') as f:
                        f.write(str(candy_new_bot))
                    return B
    except:
        context.bot.send_message(update.effective_chat.id, "Что-то не так, попробуй ввести количество конфет еще раз.")
        return B
