from telebot import types
from time import sleep
from config import bot, conn
from plugins.get import urls_citata
import requests
from bs4 import BeautifulSoup
import random #
from telebot import apihelper
from plugins.log_error import logfile
import os
import datetime
#_________________________________________________________
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
#________________________________________________________________________________________________________________
#Самые главные кнопки, где книги и прочее
#________________________________________________________________________________________________________________
        if call.data == "book":
            bot.send_chat_action(call.message.chat.id, 'typing')
            keyb = types.InlineKeyboardMarkup()
            books = types.InlineKeyboardButton(text="Книги📚", callback_data="books")
            video = types.InlineKeyboardButton(text="Видеокурсы📹", callback_data="video")
            vkus = types.InlineKeyboardButton(text="Вкусняшки😋", callback_data="vkus")
            service = types.InlineKeyboardButton(text="Сервисы😧", callback_data="servise")
            slovar = types.InlineKeyboardButton(text="Словари брут📖", callback_data="slovar")
            audio = types.InlineKeyboardButton(text="Аудиокниги🔊", callback_data="audio")
            back = types.InlineKeyboardButton(text="🔙", callback_data="glav")
            delete = types.InlineKeyboardButton(text="❌", callback_data="delete")
            keyb.add(books, video, vkus,
                     service, slovar, audio)
            keyb.add(back, delete)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="*Какой пункт выберешь?*", reply_markup=keyb, parse_mode= "Markdown")
        elif call.data == "infa":
            bot.send_chat_action(call.message.chat.id, 'typing')
            key = types.InlineKeyboardMarkup()
            arch = types.InlineKeyboardButton(text="Arch Linux", callback_data="arch linux")
            ubuntu = types.InlineKeyboardButton(text="Ubuntu Linux", callback_data="ubuntu linux")
            debian = types.InlineKeyboardButton(text="Debian Linux", callback_data="debian linux")
            gentoo = types.InlineKeyboardButton(text="Gentoo Linux", callback_data="gentoo linux")
            lfs = types.InlineKeyboardButton(text="LFS", callback_data="lfs linux")
            kali = types.InlineKeyboardButton(text="Kali Linux", callback_data="kali linux")
            back = types.InlineKeyboardButton(text="🔙", callback_data="glav")
            delete = types.InlineKeyboardButton(text="❌", callback_data="delete")
            key.add(arch, ubuntu, debian, gentoo, lfs, kali)
            key.add(back, delete)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="*Какой дистрибутив желаешь?*" , reply_markup=key, parse_mode= "Markdown")
        elif call.data == "glav":
            bot.send_chat_action(call.message.chat.id, 'typing')
            keyboard = types.InlineKeyboardMarkup()
            book = types.InlineKeyboardButton(text="Обучаться📚", callback_data="book")
            infa = types.InlineKeyboardButton(text="Wiki Linux", callback_data="infa")
            citata = types.InlineKeyboardButton(text="Цитата🤤", callback_data="citata")
            commands_help = types.InlineKeyboardButton(text="Помощь по командам📄", callback_data = "helpmenu")

            delete = types.InlineKeyboardButton(text="❌", callback_data="delete")
            keyboard.add(book, infa, citata, commands_help)
            keyboard.add(delete)

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="*Что желаешь?*", reply_markup=keyboard, parse_mode= "Markdown")
        elif call.data == "books":
            markup = types.InlineKeyboardMarkup()
            btn_site= types.InlineKeyboardButton(text='🔜', url='https://clck.ru/N3e6i')
            back = types.InlineKeyboardButton(text="🔙", callback_data="book")
            delete = types.InlineKeyboardButton(text="❌", callback_data="delete")
            markup.add(btn_site)
            markup.add(back, delete)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="*Книги, читаем и развиваемся*📚", reply_markup = markup, parse_mode= "Markdown")
        elif call.data == "video":
            markup = types.InlineKeyboardMarkup()
            btn_site= types.InlineKeyboardButton(text='🔜', url='https://clck.ru/N3eBX')
            back = types.InlineKeyboardButton(text="🔙", callback_data="book")
            delete = types.InlineKeyboardButton(text="❌", callback_data="delete")
            markup.add(btn_site)
            markup.add(back, delete)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="*Видеокурсы*📹", reply_markup = markup, parse_mode= "Markdown")
        elif call.data == "vkus":
            markup = types.InlineKeyboardMarkup()
            btn_site= types.InlineKeyboardButton(text='🔜', url='https://clck.ru/MoUC7')
            back = types.InlineKeyboardButton(text="🔙", callback_data="book")
            delete = types.InlineKeyboardButton(text="❌", callback_data="delete")
            markup.add(btn_site)
            markup.add(back, delete)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="*Вкусняшки*😋", reply_markup = markup, parse_mode= "Markdown")
        elif call.data == "servise":
            markup = types.InlineKeyboardMarkup()
            btn_site= types.InlineKeyboardButton(text='🔜', url='https://clck.ru/NBvQt')
            back = types.InlineKeyboardButton(text="🔙", callback_data="book")
            delete = types.InlineKeyboardButton(text="❌", callback_data="delete")
            markup.add(btn_site)
            markup.add(back, delete)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="*Сервисы*😧", reply_markup = markup, parse_mode= "Markdown")
        elif call.data == "slovar":
            markup = types.InlineKeyboardMarkup()
            btn_site= types.InlineKeyboardButton(text='🔜', url='https://clck.ru/NPLf6')
            back = types.InlineKeyboardButton(text="🔙", callback_data="book")
            delete = types.InlineKeyboardButton(text="❌", callback_data="delete")
            markup.add(btn_site)
            markup.add(back, delete)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="*Словари для брутфорса*📖", reply_markup = markup, parse_mode= "Markdown")
        elif call.data == "audio":
            markup = types.InlineKeyboardMarkup()
            btn_my_site= types.InlineKeyboardButton(text='🔜', url='https://clck.ru/MpokB')
            back = types.InlineKeyboardButton(text="🔙", callback_data="book")
            delete = types.InlineKeyboardButton(text="❌", callback_data="delete")
            markup.add(btn_my_site)
            markup.add(back, delete)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="*Аудиокурсы*🔊", reply_markup = markup, parse_mode= "Markdown")
#________________________________________________________________________________________________________________
#Рандомные цитатики
#________________________________________________________________________________________________________________
        elif call.data == "citata":
            try:
                markup = types.InlineKeyboardMarkup()
                duble = types.InlineKeyboardButton(text="Еще цитату😋", callback_data="citata")
                back = types.InlineKeyboardButton(text="🔙", callback_data="glav")
                delete = types.InlineKeyboardButton(text="❌", callback_data="delete")
                markup.add(duble)
                markup.add(back, delete)
                url = urls_citata()

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                text=url, reply_markup = markup)
            except apihelper.ApiTelegramException as e:
                logfile(call, "Злоупотребление кнопками").time()
#________________________________________________________________________________________________________________
#Кнопки для wiki and download linux
#________________________________________________________________________________________________________________
        elif call.data == "arch linux":
            markup = types.InlineKeyboardMarkup()
            downloads = types.InlineKeyboardButton(text='Загрузить', url='archlinux.org/download')
            wiki = types.InlineKeyboardButton(text='Вики', url='wiki.archlinux.org')
            install = types.InlineKeyboardButton(text='Инструкция', url='https://clck.ru/N5eWx')
            back = types.InlineKeyboardButton(text="🔙", callback_data="infa")
            delete = types.InlineKeyboardButton(text="❌", callback_data="delete")
            markup.add(downloads, wiki, install)
            markup.add(back, delete)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="*[Arch Linux]   Для самых привередливых*", reply_markup = markup, parse_mode= "Markdown")
        elif call.data == "ubuntu linux":
            markup = types.InlineKeyboardMarkup()
            downloads = types.InlineKeyboardButton(text='Загрузить', url='releases.ubuntu.com')
            wiki = types.InlineKeyboardButton(text='Вики', url='help.ubuntu.ru/wiki/главная')
            back = types.InlineKeyboardButton(text="🔙", callback_data="infa")
            delete = types.InlineKeyboardButton(text="❌", callback_data="delete")
            markup.add(downloads, wiki)
            markup.add(back, delete)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="*[Ubuntu Linux]   Для самых маленьких котят*", reply_markup = markup, parse_mode= "Markdown")
        elif call.data == "debian linux":
            markup = types.InlineKeyboardMarkup()
            downloads = types.InlineKeyboardButton(text='Загрузить', url='debian.org/CD/')
            wiki = types.InlineKeyboardButton(text='Вики', url='wiki.debian.org/ru/DebianRussian')
            back = types.InlineKeyboardButton(text="🔙", callback_data="infa")
            delete = types.InlineKeyboardButton(text="❌", callback_data="delete")
            markup.add(downloads,wiki)
            markup.add(back, delete)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="*[Debian Linux]   Для любителей серверов*", reply_markup = markup, parse_mode= "Markdown")
        elif call.data == "gentoo linux":
            markup = types.InlineKeyboardMarkup()
            downloads = types.InlineKeyboardButton(text='Загрузить', url='gentoo.org/downloads')
            wiki = types.InlineKeyboardButton(text='Handbook', url='wiki.gentoo.org/wiki/Handbook:Main_Pagecg/ru')
            back = types.InlineKeyboardButton(text="🔙", callback_data="infa")
            delete = types.InlineKeyboardButton(text="❌", callback_data="delete")
            markup.add(downloads,wiki)
            markup.add(back, delete)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="*[Gentoo Linux]   Для вегетарианцев*", reply_markup = markup, parse_mode= "Markdown")
        elif call.data == "lfs linux":
            markup = types.InlineKeyboardMarkup()
            downloads = types.InlineKeyboardButton(text='Загрузить', url='linuxfromscratch.org')
            wiki = types.InlineKeyboardButton(text='Russian book', url='book.linuxfromscratch.ru')
            back = types.InlineKeyboardButton(text="🔙", callback_data="infa")
            delete = types.InlineKeyboardButton(text="❌", callback_data="delete")
            markup.add(downloads,wiki)
            markup.add(back, delete)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="*[LFS Linux]   Тут даже нечего сказать*", reply_markup = markup, parse_mode= "Markdown")
        elif call.data == "kali linux":
            markup = types.InlineKeyboardMarkup()
            btn_site= types.InlineKeyboardButton(text='Взломать', url='https://clck.ru/JwL3')
            back = types.InlineKeyboardButton(text="🔙", callback_data="infa")
            delete = types.InlineKeyboardButton(text="❌", callback_data="delete")
            markup.add(btn_site)
            markup.add(back, delete)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="*[Kall Linux]   Наше время пришло, мой друг*", reply_markup = markup, parse_mode= "Markdown")
#________________________________________________________________________________________________________________
#Кнопки для команды /help
#________________________________________________________________________________________________________________
        elif call.data == "helpmenu":
            keyboard = types.InlineKeyboardMarkup() #Добавляем кнопки
            commands_user = types.InlineKeyboardButton(text="Пользователь🤵", callback_data="user")
            commands_admin = types.InlineKeyboardButton(text="Админ🤴", callback_data="admins")
            back = types.InlineKeyboardButton(text="🔙", callback_data="glav")
            delete = types.InlineKeyboardButton(text="❌", callback_data="delete")
            keyboard.add(commands_user, commands_admin) #Добавляем кнопки для вывода
            keyboard.add(back, delete)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="*Кто ты?*", reply_markup=keyboard, parse_mode= "Markdown") #Выводим кнопки и сообщение
        elif call.data == "user":
            markup = types.InlineKeyboardMarkup()
            back=types.InlineKeyboardButton(text="🔙", callback_data="helpmenu")
            delete = types.InlineKeyboardButton(text="❌", callback_data="delete")
            markup.add(back, delete) ###
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="📎*Команды для пользователя*📎"
                                    "\n`/start` - _запустить бота_"
                                    "\n`/id` - _Узнать свой Telegram ID_"
                                    "\n`/github` - _Репозиторий кота_"
                                    "\n`/say` *text* - _крик из толпы_"
                                    "\n`/invite` - _Получить пригласительную ссылку_"
                                    "\n`/cats` - _Получить рандомных котеек_"
                                    "\n`/encode` *text* - _Закодировать в base64_"
                                    "\n`/decode` *text* - _Декодировать base64_"
                                    "\n`/url` *Ссылка на сайт* - _Скриншот сайта_"
                                    "\n`/wiki` *text* - _Поиск информации в вики_"
                                    "\n`/ru` *text* - _Перевести на русский_"
                                    "\n`/en` *text* - _Перевести на английский_"
                                    "\n`/post` *text* - _Запостить шутку на канал_"
                                    "\n`/game` - _Игра камень, ножницы, бумага_"
                                    "\n`/search` *text* - _Поиск в гугле_"
                                    "\n`/sy` *text* - _Поиск в ютубе_"
                                    "\n`/proxy` - _Получить свежий список прокси_"
                                    "\n`/top` - _Показать активных пользователей_"
                                    "\n`/arch_news` - _Показать новости Арча_"
                                    "\n`/news` - _Новости_"
                                    "\n`/whois` *IP* - _Узнать информацию об IP_"
                                    "\n`/kernel` - _Показать последние версии ядер_", reply_markup=markup, parse_mode= "Markdown") #Выводим кнопки и сообщение parse_mode= "Markdown"
        elif call.data == "admins":
            markup = types.InlineKeyboardMarkup()
            back=types.InlineKeyboardButton(text="🔙", callback_data="helpmenu")
            delete = types.InlineKeyboardButton(text="❌", callback_data="delete")
            markup.add(back, delete)

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="📎*Команды для админов*📎"
                                  "\n`/kick` - _Кикнуть пользователя_"
                                  "\n`/pin` - _Закрепить пересланное сообщение_"
                                  "\n`/unpin` - _Открепить сообщение_"
                                  "\n`/mute` - _Дать мут на 10 минут_"
                                  "\n`/unmute` - _Снять мут_"
                                  "\n`/link` - _Получить пригласительную ссылку, после каждого запроса ссылка меняется_"
                                  "\n`/des`  - _Изменить описание чата, если пустая команда, то описание стирается_ "
                                  "\n`/logs` - _Просмотр журнала ошибок_"
                                  "\n`/unban` *ID* или *Пересланное сообщение* - _Убрать пользователя из черного списка_"
                                  "\n`/restart` - _Перезапустить основного бота_", reply_markup=markup, parse_mode= "Markdown")
#________________________________________________________________________________________________________________
#Рандомные котейки
#________________________________________________________________________________________________________________
        elif call.data == "cats":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            keyboard = types.InlineKeyboardMarkup()
            cats = types.InlineKeyboardButton(text="Еще хочу котейку", callback_data="cats")
            delete = types.InlineKeyboardButton(text="❌", callback_data="delete")
            keyboard.add(cats, delete)
            user_agent = {
                            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
                        }

            search = "https://theoldreader.com/kittens/1366/768/js" #Запрашиваем у юзера, что он хочет найти
            url = requests.get(search, headers=user_agent) #Делаем запрос
            soup = BeautifulSoup(url.text, features="lxml") #Получаем запрос
            result = soup.find("img").get("src") #Ищем тег <img src="ссылка.png"
            result = "https://theoldreader.com" + result
            bot.send_photo(chat_id=call.message.chat.id, photo=result, reply_markup=keyboard)
#________________________________________________________________________________________________________________
#Игра камень ножницы бумага
#________________________________________________________________________________________________________________
        elif call.data == "kamen":
            a = ['Камень', 'Ножницы', 'Бумага']
            comp_number = random.choice(a)
            enter_all = "Вы выбрали 'Камень'" + ", а мой выбор '" + comp_number + "'"
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ожидаем результата! (5 секунд)")
            sleep(5)
            if comp_number == "Камень": # Условие для ничьей
                delete = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=enter_all + "\nНичья")
                sleep(5)
                bot.delete_message(call.message.chat.id, delete.message_id)
            else: # Условие для выигрыша или проигрыша
                if comp_number == "Ножницы":
                    delete = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=enter_all + "\nТы победил, камень поломал ножницы!")
                    sleep(5)
                    bot.delete_message(call.message.chat.id, delete.message_id)
                elif comp_number == "Бумага":
                    delete = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=enter_all + "\nЯ победил, бумага закатала камень!")
                    sleep(5)
                    bot.delete_message(call.message.chat.id, delete.message_id)
        elif call.data == "noj":
            a = ['Камень', 'Ножницы', 'Бумага']
            comp_number = random.choice(a)
            enter_all = "Вы выбрали 'Ножницы'" + ", а мой выбор '" + comp_number + "'"
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ожидаем результата! (5 секунд)")
            sleep(5)
            if comp_number == "Ножницы": # Условие для ничьей
                delete = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=enter_all + "\nНичья")
                sleep(5)
                bot.delete_message(call.message.chat.id, delete.message_id)
            else: # Условие для выигрыша или проигрыша
                if comp_number == "Камень":
                    delete = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=enter_all + "\nЯ победил, так как вы выбрали ножницы. Камень поломал ножницы!")
                    sleep(5)
                    bot.delete_message(call.message.chat.id, delete.message_id)
                elif comp_number == "Бумага":
                    delete = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=enter_all + "\nТы победил, ножницы разрезали бумагу!")
                    sleep(5)
                    bot.delete_message(call.message.chat.id, delete.message_id)
        elif call.data == "bumaga":
            a = ['Камень', 'Ножницы', 'Бумага']
            comp_number = random.choice(a)
            enter_all = "Вы выбрали 'Бумага'" + ", а мой выбор '" + comp_number + "'"
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ожидаем результата! (5 секунд)")
            sleep(5)
            if comp_number == "Бумага": # Условие для ничьей
                delete = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=enter_all + "\nНичья")
                sleep(5)
                bot.delete_message(call.message.chat.id, delete.message_id)
            else: # Условие для выигрыша или проигрыша
                if comp_number == "Камень":
                    delete = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=enter_all + "\nТы победил, бумага закатала камень!")
                    sleep(5)
                    bot.delete_message(call.message.chat.id, delete.message_id)
                elif comp_number == "Ножницы":
                    delete = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=enter_all + "\nЯ победил, ножницы разрезали бумагу!")
                    sleep(5)
                    bot.delete_message(call.message.chat.id, delete.message_id)
        elif call.data == "delete":
            bot.delete_message(call.message.chat.id, call.message.message_id)
        elif call.data == "delete_2":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
        elif call.data == "dalee_top":
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT row_number() OVER(ORDER BY message::int DESC), user_id, name, message, new, date_add FROM top_users;")
                rows = cursor.fetchall()
                result_list = []
                del rows[:10]
                
                for row in rows[:10]:
                    beginner = ""
                    if row[4] == True:
                        beginner = "[Новичок]"
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

                    number = row[0]
                    user_id = row[1]
                    last_name = row[2]
                    message = row[3]
                    result = f'{number} ✅ {last_name} ✉ = {message}     {beginner}\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖'
                    result_list.append(result)
                results_lists_last = "\n".join(result_list)
                markup = types.InlineKeyboardMarkup() #Отвечаем, если выхов был из супер чата
                back_top = types.InlineKeyboardButton(text='🔙', callback_data="back_top") #Отвечаем, если выхов был из супер чата
                dalee_top_one = types.InlineKeyboardButton(text='🔜', callback_data="dalee_top_one")
                delete = types.InlineKeyboardButton(text="❌", callback_data="delete_2")
                markup.add(back_top, dalee_top_one)
                markup.add(delete) #Отвечаем, если выхов был из супер чата
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = f"📎Активность пользователей в чате📎\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n{results_lists_last}", reply_markup = markup)
            except Exception as e:
                print (e)
                markup = types.InlineKeyboardMarkup()
                dalee_top = types.InlineKeyboardButton(text='🔙', callback_data="dalee_top")
                delete = types.InlineKeyboardButton(text="❌", callback_data="delete_2")
                markup.add(dalee_top, delete)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Таблица пустая, нечего выводить", reply_markup = markup)
        elif call.data == "back_top":
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT row_number() OVER(ORDER BY message::int DESC), user_id, name, message, new, date_add FROM top_users;")
                rows = cursor.fetchall()
                result_list =[]

                for row in rows[:10]:
                    beginner = ""
                    if row[4] == True:
                        beginner = "[Новичок]"
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

                    number = row[0]
                    user_id = row[1]
                    last_name = row[2]
                    message = row[3]
                    result = f'{number} ✅ {last_name} ✉ = {message}     {beginner}\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖'
                    result_list.append(result)

                results_lists_last = "\n".join(result_list)
                markup = types.InlineKeyboardMarkup() #Отвечаем, если выхов был из супер чата
                dalee_top = types.InlineKeyboardButton(text='🔜', callback_data="dalee_top") #Отвечаем, если выхов был из супер чат
                delete = types.InlineKeyboardButton(text="❌", callback_data="delete_2")
                markup.add(dalee_top, delete) #Отвечаем, если выхов был из супер чата
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = f"📎Активность пользователей в чате📎\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n{results_lists_last}", reply_markup = markup)
            except Exception as e:
                print (e)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Таблица пустая, нечего выводить")
        elif call.data == "dalee_top_one":
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT row_number() OVER(ORDER BY message::int DESC), user_id, name, message, new, date_add FROM top_users;")
                rows = cursor.fetchall()
                result_list =[]

                beginner = ""
                for row in rows[20:30]:
                    if row[4] == True:
                        beginner = "[Новичок]"
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
                    number = row[0]
                    user_id = row[1]
                    last_name = row[2]
                    message = row[3]
                    result = f'{number} ✅ {last_name} ✉ = {message}    {beginner}\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖'
                    result_list.append(result)
                results_lists_last = "\n".join(result_list)

                markup = types.InlineKeyboardMarkup() #Отвечаем, если выхов был из супер чата
                dalee_top = types.InlineKeyboardButton(text='🔙', callback_data="dalee_top") #Отвечаем, если выхов был из супер чата
                delete = types.InlineKeyboardButton(text="❌", callback_data="delete_2")
                markup.add(dalee_top, delete) #Отвечаем, если выхов был из супер чата
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = f"📎Активность пользователей в чате📎\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n{results_lists_last}", reply_markup = markup)
            except Exception as e:
                print (e)
                markup = types.InlineKeyboardMarkup()
                dalee_top = types.InlineKeyboardButton(text='🔙', callback_data="dalee_top")
                delete = types.InlineKeyboardButton(text="❌", callback_data="delete_2")
                markup.add(dalee_top, delete)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Таблица пустая, нечего выводить", reply_markup = markup)
