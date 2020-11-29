from config import bot, chat_id
from telebot import types
from plugins.error import Error
from plugins.error import in_chat
#________________________________________________________________________________________________________________
#Команда /start выводим меню вкусняшек
#________________________________________________________________________________________________________________
@in_chat()
def start(m):
    bot.delete_message(m.chat.id, m.message_id)
    bot.send_chat_action(m.chat.id, 'typing') #тайпинг бота
    keyboard = types.InlineKeyboardMarkup() #Добавляем кнопки
    book = types.InlineKeyboardButton(text="Обучаться📚", callback_data="book")
    infa = types.InlineKeyboardButton(text="Wiki Linux", callback_data="infa")
    citata = types.InlineKeyboardButton(text="Цитата🤤", callback_data="citata")
    commands_help = types.InlineKeyboardButton(text="Помощь по командам📄", callback_data = "helpmenu")

    delete = types.InlineKeyboardButton(text="❌", callback_data="delete")
    keyboard.add(book, infa, citata, commands_help)
    keyboard.add(delete)
    bot.send_message(m.chat.id,"*Что желаешь?*", reply_markup=keyboard, parse_mode= "Markdown") #Выводим кнопки и сообщение
#________________________________________________________________________________________________________________
#Команда /help помощь по боту
#________________________________________________________________________________________________________________
@in_chat()
def helps(m):
    bot.delete_message(m.chat.id, m.message_id)
    bot.send_chat_action(m.chat.id, 'typing') #Тайпинг бота
    keyboard = types.InlineKeyboardMarkup() #Добавляем кнопки
    commands_user = types.InlineKeyboardButton(text="Пользователь🤵", callback_data="user")
    commands_admin = types.InlineKeyboardButton(text="Админ🤴", callback_data="admins")
    back = types.InlineKeyboardButton(text="🔙", callback_data="glav")
    delete = types.InlineKeyboardButton(text="❌", callback_data="delete")
    keyboard.add(commands_user, commands_admin) #Добавляем кнопки для вывода
    keyboard.add(back, delete)
    bot.send_message(m.chat.id,"*Кто ты?*", reply_markup=keyboard, parse_mode= "Markdown") #Выводим кнопки и сообщение
