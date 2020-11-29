from bs4 import BeautifulSoup
import requests
from config import bot, chat_id
import telebot.types as types
from plugins.error import Error
from plugins.error import in_chat

@in_chat()
def proxy(m):
    bot.delete_message(m.chat.id, m.message_id)
    try:
        keyboard = types.InlineKeyboardMarkup()
        keyboard_delete = types.InlineKeyboardButton(text = "❌", callback_data = "delete")
        keyboard.add(keyboard_delete)

        url = requests.get('https://us-proxy.org/')
        soup = BeautifulSoup(url.text, features="lxml")
        text = soup.find('textarea', class_='form-control')

        FILE = open ("/app/plugins/proxy_list", "r+")
        print (text, file = FILE)
        FILE.close()

        FILE = open ("/app/plugins/proxy_list", "r+")
        bot.send_document(m.chat.id, FILE, reply_markup = keyboard)
    except:
        Error(m, bot).error()