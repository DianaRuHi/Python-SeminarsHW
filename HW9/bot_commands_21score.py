from csv import list_dialects
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from random import choice as ch, randint
from spy import log 
import ast


O = 13
P = 14
Q = 16

def score21(update, context):
    log(update, context)

    coloda = {6: 4, 7: 4, 8: 4, 9: 4, 10: 4, 2: 4, 3: 4, 4: 4, 11: 4}
    count_points_user = [0]
    count_points_bot = [0]
    with open('score21.txt', 'w+') as f:
        f.write(str(coloda)+'\n')
        f.write(str(count_points_user)+'\n')
        f.write(str(count_points_bot))
    context.bot.send_message(update.effective_chat.id, "Сыграем в игру 21 очко? Цель набрать очков больше меня, но не больше 21. Всего есть 9 карт со следующими возможными очками: 2, 3, 4, 6, 7, 8, 9, 10, 11 - каждой из этих карт в колоде 4 штуки. В первом ходе ты случайным образом получаешь две карточки, далее можно взять дополнительную карточку или завершить набор карт и начать подсчет очков. Так что, хочешь сыграть? (да/нет)")
    return O

def choice21 (update, context):
    log(update, context)
    text = update.message.text

    if 'да' in text.lower():
        with open('score21.txt', 'r') as f:
            data = f.readlines()
        coloda = ast.literal_eval(data[0])
        count_points_user = ast.literal_eval(data[1])
        count_points_bot = ast.literal_eval(data[2])
        for i in range(2):
            card = ch(list(coloda.keys()))
            count_points_user.append(card)
            coloda[card] -= 1
            card = ch(list(coloda.keys()))
            count_points_bot.append(card)
            coloda[card] -= 1
        context.bot.send_message(update.effective_chat.id, f"Твои текущие карты: {count_points_user[1]}, {count_points_user[2]}\nВозьмешь еще карту? (да/нет)")
        with open('score21.txt', 'w+') as f:
            f.write(str(coloda)+'\n')
            f.write(str(count_points_user)+'\n')
            f.write(str(count_points_bot))
        return P
    else:
        context.bot.send_message(update.effective_chat.id, "Очень жаль, а мне так хотелось поиграть с тобой :(")
        return ConversationHandler.END 

def get21(update, context):
    log(update, context)
    text = update.message.text

    if 'да' in text.lower():
        with open('score21.txt', 'r') as f:
            data = f.readlines()
        coloda = ast.literal_eval(data[0])
        count_points_user = ast.literal_eval(data[1])
        count_points_bot = ast.literal_eval(data[2])

        card = ch(list(coloda.keys()))
        while coloda[card] == 0:
            card = ch(list(coloda.keys()))
        count_points_user.append(card)
        coloda[card] -= 1

        with open('score21.txt', 'w+') as f:
            f.write(str(coloda)+'\n')
            f.write(str(count_points_user)+'\n')
            f.write(str(count_points_bot))

        user_cards = ''
        for i in range(1, len(count_points_user)):
            user_cards += str(count_points_user[i]) + ', '
        context.bot.send_message(update.effective_chat.id, "Твои текущие карты: " + user_cards +"\nВозьмешь еще карту? (да/нет) (если нет, то отправь два сообщения)")
        return P
    else:
        context.bot.send_message(update.effective_chat.id, "...")
        return Q

def count21(update, context):
    log(update, context)
    with open('score21.txt', 'r') as f:
        data = f.readlines()
    coloda = ast.literal_eval(data[0])
    count_points_user = ast.literal_eval(data[1])
    count_points_bot = ast.literal_eval(data[2])    

    user_cards = ''
    for i in range(1, len(count_points_user)):
        user_cards += str(count_points_user[i]) + ', '
    context.bot.send_message(update.effective_chat.id, "Твои карты: " + user_cards)

    while sum(list(map(lambda x: int(x), count_points_bot))) < 16 or sum(list(map(lambda x: int(x), count_points_bot))) < 18 and randint(0,2) < 2:
        card = ch(list(coloda.keys()))
        while coloda[card] == 0:
            card = ch(list(coloda.keys()))
        count_points_bot.append(card)
        coloda[card] -= 1

    bot_cards = ''
    for i in range(1, len(count_points_bot)):
        bot_cards += str(count_points_bot[i]) + ', '
    context.bot.send_message(update.effective_chat.id, "Мои карты: " + bot_cards)

    sum_user = sum(list(map(lambda x: int(x), count_points_user)))
    sum_bot = sum(list(map(lambda x: int(x), count_points_bot)))

    if sum_user > 21 and sum_bot < 22 or sum_user < sum_bot and sum_user <= 21 and sum_bot <= 21: 
        winner ='Я победил.'

        with open('crore_of_all_games.txt', 'r') as f:
            data = f.readlines()
        score = ast.literal_eval(data[0])
        id = update.effective_user.id
        if id not in list(score.keys()):
            score[id] = [0, 0, 0]
        score[id][1] += 1
        with open('crore_of_all_games.txt', 'w+') as f:
            f.write(str(score))
        
    elif sum_bot > 21 and sum_user < 22 or sum_user > sum_bot and sum_user <= 21 and sum_bot <= 21:
        winner = 'Tы победил.'

        with open('crore_of_all_games.txt', 'r') as f:
            data = f.readlines()
        score = ast.literal_eval(data[0])
        id = update.effective_user.id
        if id not in list(score.keys()):
            score[id] = [0, 0, 0]
        score[id][0] += 1
        with open('crore_of_all_games.txt', 'w+') as f:
            f.write(str(score))
        
    elif sum_user > 21 and sum_bot > 21:
        winner = 'Ничья.'

        with open('crore_of_all_games.txt', 'r') as f:
            data = f.readlines()
        score = ast.literal_eval(data[0])
        id = update.effective_user.id
        if id not in list(score.keys()):
            score[id] = [0, 0, 0]
        score[id][2] += 1
        with open('crore_of_all_games.txt', 'w+') as f:
            f.write(str(score))
        
    context.bot.send_message(update.effective_chat.id, f"Ну что ж, подсчитаем очки и определим победителя.\nТы набрал {sum_user} очков.\nЯ набрал {sum_bot} очков.\n" + winner)
    return ConversationHandler.END 






# with open('crore_of_all_games.txt', 'r') as f:
#     data = f.readlines()
# score = ast.literal_eval(data[0])
# id = update.effective_user.id
# if id not in list(score.keys()):
#     score[id] = [0, 0, 0]
# score[id][0] += 1
# with open('crore_of_all_games.txt', 'w+') as f:
#     f.write(score)