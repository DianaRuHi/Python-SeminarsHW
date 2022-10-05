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

def help(update, context):
    log(update,context)
    context.bot.send_message(update.effective_chat.id, "Cписок команд: ")
    context.bot.send_message(update.effective_chat.id, "/start - приветствие")
    context.bot.send_message(update.effective_chat.id, "/wiki + текст - ищет определение в википедии")
    context.bot.send_message(update.effective_chat.id, "/abv_del + текст - удаляет из следующего после текста все слова содержащие 'aбв' ")
    context.bot.send_message(update.effective_chat.id, "/candy_game - игра про конфетки :)")
    context.bot.send_message(update.effective_chat.id, "/calc - небольшой калькулятор для рациональных и комплексных чисел")
    context.bot.send_message(update.effective_chat.id, "/tel_directory - телефонный справочник с возможностью выгрузить файл")
    context.bot.send_message(update.effective_chat.id, "/x_o_game - крестики нолики")
    

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
                    return ConversationHandler.END 
                else:
                    context.bot.send_message(update.effective_chat.id, f'Я взял {bot_move} конфет, осталось {candy_new_bot} конфет на столе.\nТвой ход.')
                    with open('candy.txt', 'w+') as f:
                        f.write(str(candy_new_bot))
                    return B
    except:
        context.bot.send_message(update.effective_chat.id, "Что-то не так, попробуй ввести количество конфет еще раз.")
        return B

def cancel(update, context):
    log(update,context)
    context.bot.send_message(update.effective_chat.id, 'Игра закончена!')


C = 2
D = 3
E = 4

def calc(update, context):
    log(update,context)
    context.bot.send_message(update.effective_chat.id, 'C какими числами вы хотите работать?\n1 - рациональные числа\n2 - комплексные числа')
    return C

def nums_calc(update, context):
    log(update,context)
    if '1' == update.message.text or '2' == update.message.text:
        with open('calc.txt', 'w+') as f:
            f.write(update.message.text)
        context.bot.send_message(update.effective_chat.id, 'Какую операцию вы хотите применить к числам?\n1 - сложение\n2 - вычитание\n3 - умножение\n4 - деление')
        return D
    else:
        context.bot.send_message(update.effective_chat.id, 'Неверный ввод, попробуйте выбрать тип чисел еще раз.')
        return C

def operation_calc(update, context):
    log(update, context)
    if '1' == update.message.text or '2' == update.message.text or '3' == update.message.text or '4' == update.message.text:
        with open('calc.txt', 'a') as f:
            f.write(update.message.text)
        context.bot.send_message(update.effective_chat.id, 'Введите числа через пробел.')
        return E
    else:
        context.bot.send_message(update.effective_chat.id, 'Неверный ввод, попробуйте выбрать операцию еще раз.')
        return D

def calc_calc(update, context):
    log(update, context)
    with open('calc.txt', 'r') as f:
        text = f.read()
    try:
        nums = [i for i in update.message.text.split()]
        if text[0] == '1':
            num1 = Fraction(nums[0])
            num2 = Fraction(nums[1])
        else:
            num1 = complex(nums[0])
            num2 = complex(nums[1])
    except:
        context.bot.send_message(update.effective_chat.id, 'Неверный ввод, попробуйте ввести числа еще раз.')
        return E
    if text[1] == '1':
        context.bot.send_message(update.effective_chat.id, f'{num1} + {num2} = {num1+num2}')
    elif text[1] == '2':
        context.bot.send_message(update.effective_chat.id, f'{num1} - {num2} = {num1-num2}')
    elif text[1] == '3':
        context.bot.send_message(update.effective_chat.id, f'{num1} * {num2} = {num1*num2}') 
    else:
        context.bot.send_message(update.effective_chat.id, f'{num1} / {num2} = {num1/num2}') 
    return ConversationHandler.END   

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

wikipedia.set_lang('ru')

def wiki(update, context):
    log(update, context)
    text = ' '.join(context.args)
    try:
        result = wikipedia.summary(text, sentences=2)
        context.bot.send_message(update.effective_chat.id, result)
    except:
        context.bot.send_message(update.effective_chat.id, 'Не найдено!')


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
                return ConversationHandler.END 
            flag = 0
            for i in pole:
                if i == '-':
                    flag = 1
            if flag == 0:
                context.bot.send_message(update.effective_chat.id, 'Ничья!')
                return ConversationHandler.END
            
            context.bot.send_message(update.effective_chat.id, 'Мой ход.')
            bot_move = randint(0,8)
            while pole[bot_move] != '-':
                bot_move = randint(0,8)
            pole[bot_move] = 'O'
            context.bot.send_message(update.effective_chat.id, f'{pole[0]} {pole[1]} {pole[2]}\n{pole[3]} {pole[4]} {pole[5]}\n{pole[6]} {pole[7]} {pole[8]}') 
            if pole[0] == pole[1] == pole[2] == 'O' or pole[3] == pole[4] == pole[5] == 'O' or pole[6] == pole[7] == pole[8] == 'O' or pole[0] == pole[3] == pole[6] == 'O' or pole[1] == pole[4] == pole[7] == 'O' or pole[2] == pole[5] == pole[8] == 'O' or pole[0] == pole[4] == pole[8] == 'O' or pole[2] == pole[4] == pole[6] == 'O':
                context.bot.send_message(update.effective_chat.id, 'Я победил!')
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


