from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from bot_commands import *

bot_token="token"
bot = Bot(bot_token)

updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher


dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('abv_del', abv_del))


candy_game_handler = CommandHandler('candy_game', candy_game)
choice_game_handler = MessageHandler(Filters.text, choice_game)
plaer_move_game_handler = MessageHandler(Filters.text, plaer_move_game)
cancel_handler = CommandHandler('cancel', cancel)

candy_handler = ConversationHandler(entry_points=[candy_game_handler],
                                    states={A: [choice_game_handler],
                                            B: [plaer_move_game_handler]},
                                    fallbacks=[cancel_handler])

dispatcher.add_handler(candy_handler)
dispatcher.add_handler(cancel_handler)



calc_handler = CommandHandler('calc', calc)
nums_calc_handler = MessageHandler(Filters.text, nums_calc)
operation_calc_handler = MessageHandler(Filters.text, operation_calc)
calc_calc_handler = MessageHandler(Filters.text, calc_calc)

cal_handler = ConversationHandler(entry_points=[calc_handler],
                                    states={C: [nums_calc_handler],
                                            D: [operation_calc_handler],
                                            E: [calc_calc_handler]},
                                    fallbacks=[cancel_handler])

dispatcher.add_handler(cal_handler)

tel_directory_handler = CommandHandler('tel_directory', tel_directory)
action_tel_handler = MessageHandler(Filters.text, action_tel)
fio_tel_handler = MessageHandler(Filters.text, fio_tel)
tel_tel_handler = MessageHandler(Filters.text, tel_tel)
info_tel_handler = MessageHandler(Filters.text, info_tel)
load_tel_handler = MessageHandler(Filters.text, load_tel)

tel_handler = ConversationHandler(entry_points=[tel_directory_handler],
                                    states={F: [action_tel_handler],
                                            G: [fio_tel_handler],
                                            H: [tel_tel_handler],
                                            I: [info_tel_handler],
                                            J: [load_tel_handler]},
                                    fallbacks=[cancel_handler])

dispatcher.add_handler(tel_handler)

x_o_game_handler = CommandHandler('x_o_game', x_o_game)
choice_x_o_handler = MessageHandler(Filters.text, choice_x_o)
x_game_handler = MessageHandler(Filters.text, x_game)
o_game_handler = MessageHandler(Filters.text, o_game)

x_o_handler = ConversationHandler(entry_points=[x_o_game_handler],
                                    states={K: [choice_x_o_handler],
                                            L: [x_game_handler],
                                            N: [o_game_handler]},
                                    fallbacks=[cancel_handler])

dispatcher.add_handler(x_o_handler)



wiki_handler = CommandHandler('wiki', wiki)
dispatcher.add_handler(wiki_handler)
dispatcher.add_handler(MessageHandler(Filters.voice, voice))
dispatcher.add_handler(MessageHandler(Filters.command, unknown_command))


updater.start_polling()
updater.idle() # ctrl + c + c



# import wikipedia
# wikipedia.set_lang('ru')

# def wiki(update, context):
#     text = ' '.join(context.args)
#     try:
#         result = wikipedia.summary(text, sentences=2)
#         context.bot.send_message(update.effective_chat.id, result)
#     except:
#         context.bot.send_message(update.effective_chat.id, 'Не найдено!')

# wiki_handler = CommandHandler('wiki', wiki)
# dispatcher.add_handler(wiki_handler)

