import telebot

# Replace 'YOUR_API_TOKEN' with your bot's API token
API_TOKEN = '7240803057:AAG7xMLwBKljEiRpjN7EYEVfANX9BGthUCI'

bot = telebot.TeleBot(API_TOKEN)

# Handle the /start and /help commands
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Здравствуйте! Я ваш помощник бот. Чем могу помочь?")

# Handle all other messages
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Вы сказали: " + message.text)

# Start the bot
bot.polling()