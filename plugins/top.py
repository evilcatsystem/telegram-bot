from config import bot, conn, user_id, chat_id
import psycopg2
from telebot import types
import matplotlib.pyplot as plt 
import warnings 
import os
from psycopg2.errors import InFailedSqlTransaction
import datetime
from plugins.error import Error
from plugins.error import in_chat
import sys
from psycopg2.errors import InFailedSqlTransaction
from psycopg2.errors import UndefinedColumn

sys.setrecursionlimit(5000) 
def deletedb(m):
    if int(m.from_user.id) == int(user_id):
        cursor = conn.cursor()
        bot.send_message(m.chat.id, "Удачный вход в базу данных")
        try:
            cursor.execute("DROP TABLE top_users;")
            conn.commit()
            bot.send_message(m.chat.id, "Таблица успешно удалена")
        except:
            bot.send_message(m.chat.id, "Таблицы не найдено")
    else:
        bot.send_message(m.chat.id, "Вас нет в списке!")

def createdb(m):
    if int(m.from_user.id) == int(user_id):
        cursor = conn.cursor()
        bot.send_message(m.chat.id, "Удачный вход в базу данных") 
        try:
            cursor.execute('''CREATE TABLE top_users
                    (user_id INT PRIMARY KEY,
                    name text,
                    message text);''')
            conn.commit()
            bot.send_message(m.chat.id, "Таблица успешна создана")
        except:
            bot.send_message(m.chat.id, "Таблица уже создана")
    else:
        bot.send_message(m.chat.id, "Вас нет в списке!")

@in_chat()
def top(m):
    bot.delete_message(m.chat.id, m.message_id)
    cursor = conn.cursor()
    cursor.execute("SELECT row_number() OVER(ORDER BY message::int DESC), user_id, name, message, new, date_add FROM top_users;")
    rows = cursor.fetchall()
    result_list = []

    beginner = ""
    for row in rows[:10]:
        date = row[5]
        if row[4] == True:
            date = row[5].split()
            year = int (date[0])     # Год
            month = int (date[1])    # Месяц
            day = int (date[2])     # День

            date_new = datetime.date(year, month, day)
            date_last = datetime.datetime.now().day - date_new.day
            if date_last >= 5:
                cursor.execute(f"""UPDATE top_users SET new = FALSE WHERE user_id = {row[1]};""") 
                cursor.execute(f"UPDATE top_users SET date_add = '' WHERE user_id = {row[1]};")
                conn.commit()
            else:
                beginner = "[Новичок]"

        number = row[0]
        user_id = row[1]
        last_name = row[2]
        message = row[3]
        result = f'{number} ✅ {last_name} ✉ = {message}     {beginner}\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖'
        result_list.append(result)
        results_lists_last = "\n".join(result_list)
        #______________________________________________________________
    try:
        markup = types.InlineKeyboardMarkup() #Отвечаем, если выхов был из супер чата
        dalee_top = types.InlineKeyboardButton(text='🔜', callback_data="dalee_top") #Отвечаем, если выхов был из супер чата
        delete = types.InlineKeyboardButton(text="❌", callback_data="delete_2")
        markup.add(dalee_top, delete) #Отвечаем, если выхов был из супер чата

        info = rows
        messages_list = []   # Создаем списки
        names_list = []

        for line in info[:-10]:               # Берем имена и сообщения, кроме последних 10.  
            if line[2] == "과일 🍊":
               names_list.append("Фрукт")         # Стираем нахой фрукта, потому что ломает все систему
               messages_list.append(line[3])      # своими иероглифами

            if line[2] == "🅨🅤🅡🅨<🐧>":
               names_list.append("@poruncov")         # Стираем нахой фрукта, потому что ломает все систему
               messages_list.append(line[3])
            else:
                names_list.append(line[2])       # Если их не убрать то надписи будут налазить
                messages_list.append(line[3])    # друг на друга

        end_messages = []

        for line in info[-10:]:                    # Берем последние 10 имен
            end_messages.append (int(line[3]))    # Добовляем сообщения в список
        end_messages = sum(end_messages)          # Суммируем их


        labels = names_list
        sizes = messages_list

        labels.append("Другие")      
        sizes.append(end_messages)

        with warnings.catch_warnings():
            warnings.simplefilter('ignore')  # Не даем показаться варнингy
            fig1, ax1 = plt.subplots()
            #plt.style.use(['dark_background'])  # Темный фон, ломает цвета
            ax1.pie(sizes, labels=labels, autopct='%1.1f%%',labeldistance = 1.08, startangle = 30, wedgeprops = {'linewidth': 18},
                    shadow=False)

            ax1.axis('equal')
            fig1.savefig('foo.png', bbox_inches='tight')
        bot.send_photo(m.chat.id, open('foo.png', 'rb'));
            #______________________________________________________________
        bot.send_message(m.chat.id, f"📎Активность пользователей в чате📎\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n{results_lists_last}", reply_markup = markup)
    except InFailedSqlTransaction:
        bot.send_message(m.chat.id, "Таблица пустая, нечего выводить")

def writes(m):           # Добавление юзера в таблицу
    if int(m.chat.id) == int(chat_id):
        cursor = conn.cursor()

        userid = str(m.from_user.id)
        last_name = m.from_user.first_name
        try:
            cursor.execute(f"""INSERT INTO top_users (user_id, name, message, new, root, send_message) VALUES ('{userid}', '{last_name}', 1, TRUE, FALSE, TRUE);""")     # Кто-то не знает про функцию zip)

            conn.commit()                                                                                                         
        except:
            conn.rollback()
            write(m)

def write(m):              # Изменение значение в таблице
    if not m.reply_to_message:
        cursor = conn.cursor()

        name = m.from_user.first_name
        userid = str(m.from_user.id)
        try:
            cursor.execute(f"SELECT message from top_users where user_id= {userid};")
            rows = cursor.fetchall()
            result=None
            for row in rows:
                mes = int(row[0]) + int(1)
                result = mes
            cursor.execute(f"UPDATE top_users set message = {str(result)}, name = '{name}' where user_id = {str(userid)};")
        except (UndefinedColumn, InFailedSqlTransaction):
            writes(m)
        finally:
            conn.commit()
    # Одна из возможных популярных ошибок в write():
    # если бот выключен, кто-то и вошел в чат. То бот не добавляет в базу
    # человека, и при изменение таблицы пользователя всё ломается