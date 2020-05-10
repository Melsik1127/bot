# -*- coding: utf-8 -
import telebot
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

TOKEN = '1235450874:AAHTVDjH_qHjhh8-k0Bc2zkyvBYPOmEMObA'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет')

bot.polling(none_stop=True)