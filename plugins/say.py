from config import bot, chat_id
from time import sleep
from telebot import types
from plugins.error import Error
from plugins.message import shout
import random
from plugins.error import in_chat, check_private

@in_chat()
def say(m):
    bot.delete_message(m.chat.id, m.message_id)
    try:
        if m.chat.type != "private":
            markup = types.InlineKeyboardMarkup() #Отвечаем, если выхов был из супер чата
            link_bot= types.InlineKeyboardButton(text='Перейти в лс', url='t.me/cat_glav_bot') #Отвечаем, если выхов был из супер чата
            markup.add(link_bot) #Отвечаем, если выхов был из супер чата
            sent=bot.send_message(m.chat.id, "Команда /say работает только в лс бота", reply_markup = markup) #Отвечаем, если выхов был из супер чата
            sleep(10)
            bot.delete_message(m.chat.id,sent.message_id)

        if m.reply_to_message:
            sticker_id = bot.get_file(m.reply_to_message.sticker.file_id)
            bot.send_sticker(chat_id, sticker_id.file_id)
            sent=bot.send_message(m.chat.id, "Стикер успешно отправлен!")#Отвечаем, если команда пришла не из супер чата
            sleep(10)
            bot.delete_message(m.chat.id,sent.message_id)
        else:
            bot.send_message(chat_id,  f"_{random.choice(shout)}:_ *'{m.text[5:]}'* 😱 ", parse_mode="Markdown") #Обработать команду и отправить то, что находится с 5 символа и до...
            sent=bot.send_message(m.chat.id, "Сообщение успешно отправлено!")#Отвечаем, если команда пришла не из супер чата
            sleep(10)
            bot.delete_message(m.chat.id,sent.message_id)
    except Exception:
        Error(m, bot).error()
