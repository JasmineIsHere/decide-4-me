import os
from dotenv import load_dotenv
import random
import telebot

load_dotenv()
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello!')

@bot.message_handler(commands=['spin'])
def spin(message):
    bot.send_message(message.chat.id, 'You should...')
    print(message)
    list_of_items = message.text[6:].split(' ')
    print(list_of_items)
    if len(list_of_items) == 1 and list_of_items[0] == '':
        bot.send_message(message.chat.id, '...enter some choices for me to spin')
    else:
        bot.send_message(message.chat.id, "..." + random.choice(list_of_items) + "!")
bot.infinity_polling()