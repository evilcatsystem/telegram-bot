from config import bot, chat_id
from time import sleep
from plugins.error import Error
from plugins.error import in_chat, check_reply, check_admin, check_reply_admin, check_private
#________________________________________________________________________________________________________________
#Команда /pin закрепить сообщение
#________________________________________________________________________________________________________________

@in_chat()
@check_admin()
@check_private()
@check_reply()
def pin(m):
    bot.delete_message(m.chat.id, m.message_id)
    bot.pin_chat_message(m.chat.id, m.reply_to_message.message_id)
    sent=bot.send_message(m.chat.id, "Сообщение успешно закреплено!")
    sleep(10)
    bot.delete_message(m.chat.id,sent.message_id)
#________________________________________________________________________________________________________________
#Команда /unpin открепить сообщение
#________________________________________________________________________________________________________________

@check_admin()
@in_chat()
@check_private()

def unpin(m):
    bot.delete_message(m.chat.id, m.message_id)
    try:
        bot.unpin_chat_message(m.chat.id)
        sent=bot.send_message(m.chat.id, "Сообщение успешно откреплено!")
        sleep(10)
        bot.delete_message(m.chat.id,sent.message_id)
    except:
        delete=bot.send_message(m.chat.id, "Нечего откреплять!")
        sleep(5)
        bot.delete_message(m.chat.id, delete.message_id)
