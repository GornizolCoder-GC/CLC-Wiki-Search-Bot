from telegram.bot import Bot
from telegram.user import User
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler
from telegram.update import Update
from settings import setting
from telegram.ext.filters import Filters
import requests

import pprint as pp

updater = Updater(token=setting.TELEGRAM_TOKEN)

# bot = Bot(token="2063139219:AAFCI6h2_AQM8-aX4DvHp8iNWBB--_Xejuw")
# user: User = bot.get_me()
# bot.send_message(chat_id=setting.CHAT_ID, text='hello motto')
# #

# print(user.link)
# print(bot.get_me())
# updates = bot.get_updates()
# print(updates[0])

def start(update: Update, context: CallbackContext):

    update.message.\
        reply_text('assalomu alaykum. Vikipedia botga xush kelibsiz! '
                   'Sizga qiziq bo‘lgan mavzuda maʼlumot olmoq uchun '
                   '/search komandasidan foydalaning. Misol uchun /search Vikipedia')
    # context.bot.send_message(chat_id=update.message.chat_id, text="Salom yana bir bor!")
    print(update)

def search(update: Update, context: CallbackContext):

    URL = "https://en.wikipedia.org/w/api.php"
    args = context.args

    if len(args) == 0:
        update.message.reply_text("Izlayotgan narsa qolib ketgan! Misol uchun quyidagicha kiriting:  \n/search Amir Temur")
    else:
        search_tag = " ".join(args)

        PARAMS = {
            'action':'opensearch',
            'format':'json',
            'search':search_tag
        }

        response = requests.get(url=URL, params=PARAMS)
        link = response.json()[3]
        test = response.json()
        text = ""
        if len(link):
            # pp.pprint(link)
            pp.pprint(test)
            text = link[0]
        else:
            # print("none")
            text = 'Afsuski bunday havola mavjud emas!'
        update.message.reply_text("Sizning so'rovingiz bo'yicha havola: \n"+ text)


dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('search', search))
dispatcher.add_handler(MessageHandler(Filters.all, start))

updater.start_polling()
updater.idle()
