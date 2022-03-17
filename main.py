from telegram.bot import Bot
from telegram.user import User
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram.update import Update
from settings import setting

updater = Updater(token=setting.TELEGRAM_TOKEN)

bot = Bot(token="2063139219:AAFCI6h2_AQM8-aX4DvHp8iNWBB--_Xejuw")
user: User = bot.get_me()
bot.send_message(chat_id=setting.CHAT_ID, text='hello motto')
#

# print(user.link)
# print(bot.get_me())
# updates = bot.get_updates()
# print(updates[0])

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Salom!')
    context.bot.send_message(chat_id=update.message.chat_id, text="Salom yana bir bor!")
    print(update)


dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()
