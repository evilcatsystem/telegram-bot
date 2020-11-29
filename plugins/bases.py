#!/usr/bin/python
from config import bot, conn, user_id, chat_id
import psycopg2
from telebot import types

# Это написано для взаимодействия с бд

def set_(m):
	bot.delete_message(m.chat.id, m.message_id)
	if m.from_user.id == 905933085:
		info = m.text[4:].split()
		cursor = conn.cursor()
        cursor.execute("UPDATE top_users set message = " + info[1] + " where user_id = " + str(info[0]))
