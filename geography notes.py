from telegram import *
from telegram.ext import *
from requests import *

updater = Updater(token="5720124659:AAGrCyeYC1P5hyIu0I245cx2lagTbc8zHCk")
dispatcher = updater.dispatcher

geography_content = "Geography Notes"
class6 = "Class 6"
class7 = "Class 7"
class8 = "Class 8"
class9 = "Class 9"
class10 = "Class 10"
class11 = "Class 11"
class12 = "Class 12"


def startCommand(update: Update, context: CallbackContext):
    buttons = [[KeyboardButton(geography_content)]]
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=
        "Hi, Awsome Human.\nThis Bot will assit you by providing Geography notes for your preperation.\nDo consider Subscribig Our YouTube Channel link provided below\n\nhttps://www.youtube.com/channel/UChKAauPQVYK5rzLHgl8u36g\n\nClick on the Buttons to Continue.",
        reply_markup=ReplyKeyboardMarkup(buttons))


def messageHandler(update: Update, context: CallbackContext):
    if geography_content in update.message.text:
        buttons = [[KeyboardButton(class6)], [KeyboardButton(class7)],
                   [KeyboardButton(class8)], [KeyboardButton(class9)],
                   [KeyboardButton(class10)], [KeyboardButton(class11)],
                   [KeyboardButton(class12)]]
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Select the Class of your choice.",
                                 reply_markup=ReplyKeyboardMarkup(buttons))
    if class6 in update.message.text:
      context.bot.send_document(chat_id=update.effective_chat.id, document=open('chemicalbond.pdf', 'rb'), filename="Chapter 1 - Our Earth")
      
        


dispatcher.add_handler(CommandHandler("start", startCommand))
dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))

updater.start_polling()
