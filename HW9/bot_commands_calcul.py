from asyncore import write
from ctypes.wintypes import HACCEL
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from random import randint
from spy import log 
from fractions import Fraction
from ast import dump


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

