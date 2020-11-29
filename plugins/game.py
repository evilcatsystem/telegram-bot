from config import bot, chat_id
from telebot import types
from plugins.error import in_chat
@in_chat()
def game(m):
    bot.delete_message(m.chat.id, m.message_id)
    keyboard = types.InlineKeyboardMarkup() #Добавляем кнопки
    kamen = types.InlineKeyboardButton(text="Камень", callback_data="kamen")
    noj = types.InlineKeyboardButton(text="Ножницы", callback_data="noj")
    bumaga = types.InlineKeyboardButton(text="Бумага", callback_data="bumaga")
    keyboard.add(kamen, noj, bumaga) #Добавляем кнопки для вывода
    bot.send_message(m.chat.id,"*Поиграем?*", reply_markup=keyboard, parse_mode= "Markdown") #Выводим кнопки и сообщение


