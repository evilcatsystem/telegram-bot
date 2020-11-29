from config import bot, chat_id
from time import sleep
from plugins.error import Error
from plugins.error import in_chat
#________________________________________________________________________________________________________________
#Команда /id Показатель id пользователя
#________________________________________________________________________________________________________________
@in_chat()
def command_id(m):
    bot.delete_message(m.chat.id, m.message_id)
    try:
        bot.send_chat_action(m.chat.id, 'typing') #тайпинг бота
        sent=bot.send_message(m.chat.id, u"@" + str(m.from_user.username)+ ", " + "ваш Telegram ID: " + str(m.from_user.id))
        sleep(10)
        bot.delete_message(m.chat.id,sent.message_id)
    except Exception:
        Error(m, bot).error()