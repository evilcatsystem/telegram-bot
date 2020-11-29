from config import bot, chat_id
from telebot import types
import requests
from bs4 import BeautifulSoup
from plugins.error import in_chat

@in_chat()
def cats(m):
    bot.delete_message(m.chat.id, m.message_id)
    keyboard = types.InlineKeyboardMarkup() #Добавляем кнопки
    cats = types.InlineKeyboardButton(text="Еще хочу котейку", callback_data="cats")
    keyboard.add(cats) #Добавляем кнопки для вывода
    user_agent = {
                    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
                }

    search = "https://theoldreader.com/kittens/1366/768/js" #Запрашиваем у юзера, что он хочет найти
    url = requests.get(search, headers=user_agent) #Делаем запрос
    soup = BeautifulSoup(url.text, features="lxml") #Получаем запрос
    result = soup.find("img").get("src") #Ищем тег <img src="ссылка.png"
    result = "https://theoldreader.com" + result
    bot.send_photo(m.chat.id,photo=result, reply_markup=keyboard, parse_mode= "Markdown")
