# -*- coding: utf-8 -
import telebot
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

TOKEN = '1262410895:AAGF4lqKGSzp6-73cPG9d2eijkiNF-tFKS8'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет')

bot.polling(none_stop=True)
