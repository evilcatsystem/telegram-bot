from config import bot, chat_id, group_id
from time import sleep
from plugins.error import Error
from plugins.error import in_chat, check_reply, check_admin
#________________________________________________________________________________________________________________
#Получить айди чата, если не знаете айди, то закомментируйте строки связанные с проверкой пользователя на наличие его в чате
#________________________________________________________________________________________________________________
@in_chat()
def id_chat(m):
    bot.delete_message(m.chat.id, m.message_id)
    bot.send_message(m.chat.id, "Айди чата " + m.chat.title + ": " + str(m.chat.id))

#________________________________________________________________________________________________________________
#Меняем описание чата
#________________________________________________________________________________________________________________
@in_chat()
@check_admin()
def description(m):
    bot.delete_message(m.chat.id, m.message_id)
    try:
        bot.set_chat_description(chat_id, m.text[5:])
        sent=bot.send_message(m.chat.id, "Описание чата изменено на: " + m.text[5:])
        sleep(10)
        bot.delete_message(m.chat.id,sent.message_id)
    except Exception:
        Error(m, bot).error()
#________________________________________________________________________________________________________________
#Получаем ссылку на приглашение в чат
#________________________________________________________________________________________________________________
@in_chat()
@check_admin()
def link(m):
    bot.delete_message(m.chat.id, m.message_id)
    try:
        count = bot.export_chat_invite_link(chat_id)
        bot.send_message(m.from_user.id, count)
    except:
        bot.send_message(chat_id, "К нам постучался заблокированный юзер " + m.from_user.last_name)

#________________________________________________________________________________________________________________
#Команда /invite отправляем пользователя за ссылкой приглашения в чат
#________________________________________________________________________________________________________________
@in_chat()
@bot.message_handler(commands=['invite']) #Команда /ivnite
def invite(m):
    bot.delete_message(m.chat.id, m.message_id)
    try:
        sent=bot.send_message(m.chat.id, "Чтобы получить ссылку на приглашение в чат, свяжитесь с администрацией \n@evil_cat_it \n@hh8oShjvjj89og995gui\n@frutitutitut\n@I_LOVE_ARCH")
        sleep(10)
        bot.delete_message(m.chat.id,sent.message_id)
    except Exception:
        Error(m, bot).error()
#________________________________________________________________________________________________________________
#Удалить пересланное сообщение, не знаю зачем, но мне в кайф
#________________________________________________________________________________________________________________
@in_chat()
@check_reply()
def delete(m):
    bot.delete_message(m.chat.id, m.message_id)
    try:
        bot.delete_message(m.chat.id, m.reply_to_message.message_id)
    except Exception:
        Error(m, bot).error()

#________________________________________________________________________________________________________________
#Запостить текст на канал
#________________________________________________________________________________________________________________
@in_chat()
def post(m):
    bot.delete_message(m.chat.id, m.message_id)
    try:
        bot.send_message(group_id, m.text[6:])
        bot.send_message(m.chat.id, "Сообщение \n" + m.text[6:] + " \nОтправлено на канал " + group_id)
    except Exception:
        Error(m, bot).error()
