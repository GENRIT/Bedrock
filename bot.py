import telebot
from telebot import types
import os

API_TOKEN = '7240803057:AAG7xMLwBKljEiRpjN7EYEVfANX9BGthUCI'
OWNER_CHAT_ID = 1420106372

bot = telebot.TeleBot(API_TOKEN)

# Handle the /start and /help commands
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Здравствуйте! Я ваш помощник бот. Чем могу помочь?")

# Handle registration data
@bot.message_handler(content_types=['document'])
def handle_docs(message):
    if message.chat.id == OWNER_CHAT_ID:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        file_extension = os.path.splitext(message.document.file_name)[1]

        if file_extension == '.mcpack':
            mcpack_filename = f"{os.path.splitext(message.document.file_name)[0]}.mcpack"
            with open(mcpack_filename, 'wb') as new_file:
                new_file.write(downloaded_file)
            bot.reply_to(message, f"Файл .mcpack сохранен как {mcpack_filename}")
        elif file_extension == '.png' and message.caption:
            caption_parts = message.caption.split('\n')
            if len(caption_parts) == 2 and ': ' in caption_parts[0] and ': ' in caption_parts[1]:
                nickname = caption_parts[0].split(': ')[1]
                email = caption_parts[1].split(': ')[1]
                skin_filename = f"{nickname}_skin.png"
                with open(skin_filename, 'wb') as new_file:
                    new_file.write(downloaded_file)
                confirmation_message = f"Получены данные регистрации:\nНик: {nickname}\nПочта: {email}\nСкин сохранен как {skin_filename}"
                bot.reply_to(message, confirmation_message)
            else:
                bot.reply_to(message, "Подпись должна содержать ник и почту в формате:\nНик: <ваш ник>\nПочта: <ваша почта>")
        else:
            bot.reply_to(message, "Файл не является .mcpack или .png с правильной подписью.")
    else:
        bot.reply_to(message, "Вы не являетесь владельцем этого бота или данные регистрации не были отправлены корректно.")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.chat.id == OWNER_CHAT_ID:
        bot.reply_to(message, "Получены регистрационные данные: " + message.text)
    else:
        bot.reply_to(message, "Вы не являетесь владельцем этого бота.")

# Start the bot
bot.polling()
