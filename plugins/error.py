from config import bot
from time import sleep
import random
from config import chat_id
from config import token

class Error:
    def __init__(self, m, bot):

        permission = ['У вас нет прав на использование этой команды', 'Недостаточно прав', 'Ну куда ты лезишь, команда не для тебя',
        'Не делай так больше', 'Вот ты псих :D', "А ну брысь отсюда", "Ну и что ты хочешь от меня?", "Ты действительно думаешь что я выполню твою просьбу?",
        "Кышь, твои полномочия всё", "Нет, я этого не сделаю", "Все надоели, я в отпуске"]

        reply = ['Перешлите сообщение', 'По-моему где-то сообщение потерялось и до меня не дошло', 'А сообщение где?',
        'Я бы пошутил про UDP, но боюсь, что не дайдет, как и ваше пересланное сообщение', "А пересылать сообщение кто будет?"]

        admin = ['Я не имею прав трогать админов', 'Мои чары на администрацию не распространяется', 'А может не будем трогать админов?',
        'Не надо раздражать админов', 'Ну это пиздец, зачем мы админов тронули, ну все, пойду вешаться', "На что ты меня подписываешь? Не трошь админов",
        "Не надо расстраивать администрацию"]

        errors = ['Ошибка', 'Ой, я ошибку поймал', "Я поймал KERNEL PANIC", "Что-то мне сегодня не хорошо",
        "Произошла ошибка, но я все равно буду работать"]

        private = ['Команда не работает в лс бота', 'Команда работает только в чате', 'Ну и зачем ты это делаешь? Эта команда не для лс']

        shout = ['Крик из толпы', 'Я слышал, как кто-то крикнул', "Хакеры пришли и написали"]

        self.permission = permission
        self.reply = reply
        self.admin = admin
        self.errors = errors
        self.private = private
        self.shout = shout
        self.m = m
        self.bot = bot

    def error_reply_message(self):
    #Функция для вывода ошибки, если нет пересланного сообщения
        try:
            delete = self.bot.send_message(self.m.chat.id, "❗⛔️ " + random.choice(self.reply) + " ⛔️❗")
            sleep(5)
            self.bot.delete_message(self.m.chat.id, self.m.message_id + 1)
        except:
            pass

    def error_permission(self):
        #Функция для вывода ошибки, если ошибка при выполнение команды
        try:
            delete=self.bot.send_message(self.m.chat.id, "❗⛔️ " + random.choice(self.permission) + " ⛔️❗️")
            sleep(10)
            self.bot.delete_message(self.m.chat.id, self.m.message_id + 1)
        except:
            pass
    def message_admin(self):
        #Функция для вывода ошибки, если сообщение принадлежит админу
        try:
            delete=self.bot.send_message(self.m.chat.id, "❗⛔️ " + random.choice(self.admin) + " ⛔️❗️")
            sleep(10)
            self.bot.delete_message(self.m.chat.id, self.m.message_id + 1)
        except:
            pass
    def error(self):
        # В случае ошибки
        try:
            delete=self.bot.send_message(self.m.chat.id, "❗⛔️ " + random.choice(self.errors) + " ⛔️❗️")
            sleep(10)
            self.bot.delete_message(self.m.chat.id, self.m.message_id + 1)
        except:
            pass
    def private_bot(self):
        try:
            #Функция для вывода ошибки, если команда не предназначена для лс бота
            delete=self.bot.send_message(self.m.chat.id, "❗⛔️ " + random.choice(self.private) + " ⛔️❗️")
            sleep(5)
            self.bot.delete_message(self.m.chat.id, self.m.message_id + 1)
        except:
            pass
#######################################################

    # Проверка пересылается ли сообщение админу
    def check_reply_admin_(self):
        if self.m.reply_to_message:
            if self.bot.get_chat_member(chat_id, self.m.reply_to_message.from_user.id).status not in ['administrator', 'creator'] and not self.m.reply_to_message.from_user.id == 905933085:
                return True
            else:
                return False
        else:
            return None
    # True - пересылающий не админ
    # False - админ
    # None - сообщение не пересылалось

########################################################

def in_chat():            # Проверка, присутствует ли человек в чате
    def wrap1(func):
        def wrap2(m, *args):
            status = ['creator', 'administrator', 'member', "restricted"]
            if bot.get_chat_member(chat_id, user_id=m.from_user.id).status in status or m.from_user.id == 905933085:
                func(m, *args)
            else:
                bot.delete_message(m.chat.id, m.message_id)
                Error(m, bot).error()
        return wrap2
    return wrap1
 
def check_admin():        # Проверка, является ли человек администратором
    def wrap1(func):
        def wrap2(m, *args):
            if bot.get_chat_member(chat_id, m.from_user.id).status in ['administrator', 'creator'] or m.from_user.id == 905933085:
                func(m, *args)
            else:
                bot.delete_message(m.chat.id, m.message_id)
                Error(m, bot).error_permission()
        return wrap2
    return wrap1

def check_reply_admin():    # Проверка, чьё сообщение переслали
    def wrap1(func):        
        def wrap2(m, *args):
            if m.reply_to_message:
                if bot.get_chat_member(chat_id, m.reply_to_message.from_user.id).status not in ['administrator', 'creator'] and not m.from_user.id == 905933085:
                    func(m, *args)
                else:
                    bot.delete_message(m.chat.id, m.message_id)
                    Error(m, bot).message_admin()

        return wrap2
    return wrap1

def check_reply():    # Проверка, чьё сообщение переслали
    def wrap1(func):
        def wrap2(m, *args):
            if m.reply_to_message:
                func(m, *args)
            else:
                bot.delete_message(m.chat.id, m.message_id)
                Error(m, bot).error_reply_message()
        return wrap2
    return wrap1

def check_private():   # Проверка, активен ли бот в личке
    def wrap1(func):
        def wrap2(m, *args):
            if m.chat.type != "private":
                func(m, *args)
            else:
                bot.delete_message(m.chat.id, m.message_id)
                Error(m, bot).private_bot()
        return wrap2
    return wrap1

def check_exist_user():   # Проверка, существует ли пользователь (пересылающий)
    def wrap1(func):
        def wrap2(m, *args):
            if m.reply_to_message:
                import requests
                id_ = m.reply_to_message.from_user.id

                url = f'https://api.telegram.org/bot{token}/getChatMember'
                payload = {
                    
                    "chat_id":"-1001293845658",
                    "user_id": id_
                }

                res = requests.post(url, data=payload)
                response = dict(res.json())
                response = response['result']
                status = response['status']
                try:
                    if status == 'left' or response['is_member'] == False: 
                        bot.delete_message(m.chat.id, m.message_id)
                        Error(m, bot).error()
                    else:
                        func(m, *args)
                except:
                    func(m, *args)
        return wrap2
    return wrap1