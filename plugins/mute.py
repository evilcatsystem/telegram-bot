from config import bot, chat_id
import time
from plugins.error import Error
import datetime
from plugins.error import in_chat, check_admin, check_private, check_reply, check_exist_user
#________________________________________________________________________________________________________________
#Команда /mute
#________________________________________________________________________________________________________________
@in_chat()
@check_admin()
@check_private()
@check_reply()
@check_exist_user()
def mute(m):
    bot.delete_message(m.chat.id, m.message_id)

    check_admin = Error(m, bot).check_reply_admin_()

    if m.reply_to_message.from_user.id == 905933085:
        bot.send_message(m.chat.id, text = "*Не трошь её!*", parse_mode = "Markdown")
        time.sleep(2)
        bot.delete_message(m.chat.id, m.message_id + 1)
        bot.send_sticker(m.chat.id, "CAACAgIAAxkBAAIalF94SmIocEzaL6j2Yaz4IAM_ueoMAAIBAQACnxUvEo9CUplzfDv9GwQ")
        time.sleep(5)
        bot.delete_message(m.chat.id, m.message_id + 2)
##########################################################################
    else:                                      # Если человек не
        if check_admin == False:    
            Error(m, bot).message_admin()
        if check_admin == True:
            bot.restrict_chat_member(m.chat.id, m.reply_to_message.from_user.id, can_send_messages=False)
            bot.send_message(m.chat.id, text = "*" + m.reply_to_message.from_user.first_name + "* _замолк на 10 минут!_", parse_mode = "Markdown")


    # m.from_user.id - айди человека, который хочет замутить
    # m.reply_to_message - проверить, переслано ли сообщение
    # m.reply_to_message.from_user.id - айди человека, которого мутят
#________________________________________________________________________________________________________________
#Команда /unmute
#________________________________________________________________________________________________________________
@in_chat()
@check_private()
@check_reply()
@check_admin()
@check_exist_user()

def unmute(m):
    bot.delete_message(m.chat.id, m.message_id)
    check_admin = Error(m, bot).check_reply_admin_()

    if check_admin == True:

        umute = "_Вам разрешено отправлять сюда сообщения._ *Будь хорошим мальчиком!*"
        if m.reply_to_message.from_user.id:
            bot.restrict_chat_member(m.chat.id, m.reply_to_message.from_user.id,
                                       can_send_messages=True,
                                       can_send_media_messages=True,
                                       can_send_other_messages=True,
                                       can_add_web_page_previews=True)
            bot.send_message(m.chat.id, umute,
                            reply_to_message_id=m.reply_to_message.message_id, parse_mode = "Markdown")
        else:
            bot.restrict_chat_member(m.chat.id, m.reply_to_message.from_user.username,
                                       can_send_messages=True,
                                       can_send_media_messages=True,
                                       can_send_other_messages=True,
                                       can_add_web_page_previews=True)
            bot.send_message(m.chat.id, umute,
                            reply_to_message_id=m.reply_to_message.message_id)
    else:
        delete = bot.send_message(m.chat.id, "Пользователь и так может свободно общаться в чате")
        time.sleep(5)
        bot.delete_message(m.chat.id, delete.message_id)


