from config import bot, chat_id
from time import sleep
from plugins.error import Error
from plugins.error import in_chat, check_reply, check_private, check_admin, check_exist_user
from telebot.apihelper import ApiTelegramException

@in_chat()         # Новая версия
@check_private()
@check_admin()
@check_reply()
@check_exist_user()

def kick(m):
    bot.delete_message(m.chat.id, m.message_id)
    bool_ = Error(m,bot).check_reply_admin_()
    if m.reply_to_message.from_user.id == 905933085:
        bot.send_message(m.chat.id, f"*{m.from_user.first_name}*, по голове постучи себе!", parse_mode = "Markdown")
    elif bool_ == True:
        bot.kick_chat_member(m.chat.id, m.reply_to_message.from_user.id) #Удаляем пользователя по пересланному сообщению
    elif bool_ == False:
        Error(m, bot).message_admin()

"""  # Прошлая версия
from config import bot, chat_id
from time import sleep
from plugins.error import error_permission, message_admin, private_bot

def kick(m):
    bot.delete_message(m.chat.id, m.message_id) #Удалить сообщение, содержащее команду
    status = ['creator', 'administrator', 'member']
    for chri in status:
        if chri == bot.get_chat_member(chat_id, user_id=m.from_user.id).status: #Проверить, находится ли пользователь в чате
            if m.chat.type == "private":
                private_bot(m)
            else:
                if bot.get_chat_member(m.chat.id, m.from_user.id).status in ["administrator", "creator"]: #Проверить на наличие админ прав
                    if m.reply_to_message:
                        if bot.get_chat_member(m.chat.id, m.reply_to_message.from_user.id).status not in ["administrator", "creator"]:
                            bot.kick_chat_member(m.chat.id, m.reply_to_message.from_user.id) #Удаляем пользователя по пересланному сообщению
                        else: #Если сообщение принадлежит админу
                            message_admin(m)
                    else:
                        try:
                            if bot.get_chat_member(m.chat.id, m.text[6:]).status not in ["administrator", "creator"]:
                                bot.kick_chat_member(m.chat.id, m.text[6:])
                            else: #Если сообщение принадлежит админу
                                message_admin(m)
                        except:
                            sent=bot.send_message(m.chat.id, "Ошибка выполнения команды, проверьте правильность написания команды или напишите администратору\n"
                                        "\n/kick user_id или перешлите сообщение")
                            sleep(10)
                            bot.delete_message(m.chat.id, sent.message_id)
                else:#если команду вызвал не админ
                    error_permission(m)
"""