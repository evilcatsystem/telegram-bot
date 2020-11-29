import requests
from bs4 import BeautifulSoup
from config import bot, chat_id
import telebot.types as types
from plugins.error import Error
from plugins.error import in_chat

@in_chat()
def news(m):
    bot.delete_message(m.chat.id, m.message_id)
    try:
        keyboard = types.InlineKeyboardMarkup()
        keyboard_delete = types.InlineKeyboardButton(text = "❌", callback_data = "delete")
        keyboard.add(keyboard_delete)

        user_agent = {
                    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
                    }
        url = requests.get('https://www.opennet.ru/#', headers=user_agent)
        soup = BeautifulSoup(url.text, features="lxml")

        tags = soup.find_all('td', class_="tnews")
        results_news = []
        for b in tags:
            url = b.find('a').get('href')
            title = b.find('a').text
            results = f'<a href="https://www.opennet.ru{url}">{title}</a>'
            results_news.append(results)
            results_lists_news = "\n".join(results_news)
        bot.send_message(m.chat.id, "\n🆕 Новости 🆕\n" + results_lists_news, reply_markup = keyboard, disable_web_page_preview = True, parse_mode="HTML")
    except:
        Error(m, bot).error()