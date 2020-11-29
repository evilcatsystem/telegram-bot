from config import bot, chat_id, user_id, conn
import datetime
from plugins.top import writes
#________________________________________________________________________________________________________________
#Встречаем нового пользователя в чате
#________________________________________________________________________________________________________________
def handler_new_member(m):
    bot.delete_message(m.chat.id, m.message_id) #Удалить сообщение, содержащее команду
    id = m.json
    id = id['new_chat_members']
    for a in id:
        id = a['id']
        name = a['first_name']
    last = f'<a href="tg://user?id={id}">{name}</a>'
    bot.send_sticker(m.chat.id, 'CAACAgIAAxkBAAJFW16Tj7HCIcjx9fPTf3WYtEXLG4EJAAIDAAOF-3IqNguusCQT_gEYBA') #Отправить стикер
    bot.send_message(m.chat.id, "Добро пожаловать, " + last + "\nНапиши /help, чтобы мной воспользоваться", parse_mode="HTML")
    bot.export_chat_invite_link(chat_id)

    #######################################################
    writes(m)
    cursor = conn.cursor()
    date = (datetime.datetime.now()).strftime("%Y %m %d")
    id_ = m.from_user.id
    cursor.execute(f"UPDATE top_users SET date_add = '{date}' WHERE user_id = {m.from_user.id};")
    conn.commit()
    ########################################################
#________________________________________________________________________________________________________________
#Провожаем вышедшего пользователя
#________________________________________________________________________________________________________________
def left_chat_member(m):
    try:
        bot.delete_message(m.chat.id, m.message_id) #Удалить сообщение о том что пользователь вышел
        bot.export_chat_invite_link(chat_id)
        first = f'<a href="tg://user?id={m.from_user.id}">{m.from_user.first_name}</a>'
        last = f'<a href="tg://user?id={m.left_chat_member.id}">{m.left_chat_member.first_name}</a>'
        if m.from_user.id != m.left_chat_member.id:
            bot.send_sticker(m.chat.id, 'CAACAgIAAxkBAAJMe1-lM12m7DQqSelOfsAs3qzBZbY7AAKPEQACPLPFBzLcyrxNSGysHgQ') #Отправить стикер
            result = first + " кикнул(a) " + last
            bot.send_message(m.chat.id, result, parse_mode=('HTML'))
        else:
            bot.send_sticker(m.chat.id, 'CAACAgIAAxkBAAJMe1-lM12m7DQqSelOfsAs3qzBZbY7AAKPEQACPLPFBzLcyrxNSGysHgQ') #Отправить стикер
            bot.send_message(m.chat.id, last + ' покинул(a) нас', parse_mode=("HTML")) #Уведомляем, что пользователь вышел
        cursor = conn.cursor()
        userid = m.left_chat_member.id
        cursor.execute("DELETE FROM top_users WHERE user_id = " + str(userid) + ";")
        conn.commit()
    except:
        bot.send_message(user_id, "Я - псих. И устал от вас, прощайте.")
