import telebot #pip install pyTelegramBotAPI
import requests #pip install requests
import psycopg2
###
token = '<token>'
bot = telebot.TeleBot(token, threaded=True)           # Если есть рекурсионные ошибки вписать: threaded=False
s = requests.session()                                # Многопоточность автоматически включена (при выключении
                                                      # бот становится медленней)
chat_id = "<chat_id>"   
user_id = "712178565"          
group_id = "@shutki_it"        

conn = psycopg2.connect(dbname='<dbname>', user='<user>',
                    password='<password>', host='<host>')


