from config import bot, chat_id
from plugins.error import Error
import requests
from bs4 import BeautifulSoup
import time
from telebot import types
from plugins.error import in_chat

#________________________________________________________________________________________________________________
#Скриншот сайтов
#________________________________________________________________________________________________________________
@bot.message_handler(commands=['url'])
@in_chat()
def screen(m):
    bot.delete_message(m.chat.id, m.message_id)
    HEADERS = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"}
    keyboard = types.InlineKeyboardMarkup()
    keyboard_delete = types.InlineKeyboardButton(text = "❌", callback_data = "delete")
    keyboard.add(keyboard_delete)

    try:
        res = requests.get(m.text[5:], headers = HEADERS) # Защита от спермотоксикозников
        bool_ = ("Порн" in res.text or "Porn" in res.text or "porn" in res.text or "порн" in res.text)
        if bool_ == 1:  
            bot.send_sticker(m.chat.id, "CAACAgQAAxkBAAIaSF93cwIsw1oPRGtOdZHTF8_UsBTDAAJYAAO6erwZr3-jVb-xFsgbBA")
            time.sleep (15.5)
            bot.delete_message(m.chat.id, m.message_id + 1)
        else:
            bot.send_photo(m.chat.id, photo="https://mini.s-shot.ru/1366x768/JPEG/1366/Z100/?" + m.text[5:], reply_markup = keyboard)
    except Exception as e:
        print ("❌ ОШИБКА ❌")
        print ("screenshot.py  " + e)
        Error(m, bot).error()