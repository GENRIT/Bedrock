import telebot
import os

# Убедитесь, что вы получаете токен из переменных окружения или замените его своим токеном
TOKEN = os.getenv( 
'7240803057:AAG7xMLwBKljEiRpjN7EYEVfANX9BGthUCI')

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello!')

def main():
    bot.polling()

if name == 'main':
    main()