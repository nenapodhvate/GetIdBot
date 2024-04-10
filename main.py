import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from config import TOKEN 

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)

def sticker_handler(update: Update, context: CallbackContext) -> None:
    sticker_id = update.message.sticker.file_id
    update.message.reply_text(f"Sticker ID: {sticker_id}")

def chatid_handler(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    update.message.reply_text(f"Chat ID: {chat_id}")

def add_command_handlers(dispatcher):
    dispatcher.add_handler(CommandHandler("chatid", chatid_handler))

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Hi, I'm a bot that will help you get sticker or chat IDs.\n"
        "Just send me a sticker to find out his ID,"
        "or use the /chatid command to get the ID of the current chat."
    )

def unknown_content_handler(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Sorry, I can only handle text messages, stickers and commands.")

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(MessageHandler(Filters.sticker, sticker_handler))

    add_command_handlers(dp)

    dp.add_handler(MessageHandler(Filters.all, unknown_content_handler))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
