from config import bot, chat_id
from translate import Translator
from plugins.error import Error
from plugins.error import in_chat
#________________________________________________________________________________________________________________
#перевод на русский
#________________________________________________________________________________________________________________
@in_chat()
def ru(m):
    bot.delete_message(m.chat.id, m.message_id)
    try:
        translator= Translator(to_lang="ru", from_lang="en")
        translation = translator.translate(m.text[4:])
        bot.send_message(m.chat.id,"Перевод: " + translation)
    except:
        Error(m, bot).error()
#________________________________________________________________________________________________________________
#перевод на английский
#________________________________________________________________________________________________________________
@in_chat()
def en(m):
    bot.delete_message(m.chat.id, m.message_id)
    try:
        translator= Translator(to_lang="en", from_lang="ru")
        translation = translator.translate(m.text[4:])
        bot.send_message(m.chat.id, "Перевод: " + translation)
    except:
        Error(m, bot).error()