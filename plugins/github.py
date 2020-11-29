from config import bot, chat_id
from time import sleep
from plugins.error import Error
from plugins.error import in_chat
#________________________________________________________________________________________________________________
#Команда /github моя ветка на гитхабе
#________________________________________________________________________________________________________________
@in_chat()
def github(m):
    try:
        bot.delete_message(m.chat.id, m.message_id)
        delete=bot.send_message(m.chat.id, "_Репозиторий кота_ [Тык](https://github.com/evilcatsystem)", parse_mode= "Markdown") #Отправляем сообщение
        sleep(10)
        bot.delete_message(m.chat.id, delete.message_id)
    except Exception:
        Error(m, bot).error()