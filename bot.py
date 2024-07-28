from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os

TOKEN = os.getenv('7240803057:AAHg-vv5-OYhosfjdRwsIuF93D6wtPUAlBo')

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello!')

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
