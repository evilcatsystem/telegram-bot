from config import bot, chat_id
import base64
from time import sleep
from plugins.error import Error
from plugins.log_error import logfile
from plugins.error import in_chat
#________________________________________________________________________________________________________________
#Кодируем в base64
#________________________________________________________________________________________________________________
@in_chat()
def encode(m):
    bot.delete_message(m.chat.id, m.message_id)
    a=bot.send_message(m.chat.id, "***")

    try:
        message = m.text[7:]
        encode_message = message.encode("UTF-8")
        encode = base64.b64encode(encode_message)
        bot.edit_message_text(chat_id=m.chat.id, text=encode,message_id=a.message_id)
    except (Exception, apihelper.ApiTelegramException) as e:
        logfile(m, "Злоупотребление base командами").time()
        Error(m, bot).error()
#________________________________________________________________________________________________________________
#Декодируем base64
#________________________________________________________________________________________________________________
@in_chat()
def decode(m):
    bot.delete_message(m.chat.id, m.message_id)
    a=bot.send_message(m.chat.id, "***")
    try:
        message = m.text[7:]
        encode_message = message.encode("UTF-8")
        decode = base64.b64decode(encode_message)
        bot.edit_message_text(chat_id=m.chat.id, text=decode,message_id=a.message_id)
    except (Exception, apihelper.ApiTelegramException) as e:
        logfile(m, "Злоупотребление base командами").time()
        Error(m, bot).error()