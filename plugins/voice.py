from config import bot, s
import speech_recognition as sr #pip install SpeechRecognition
import subprocess
import os
import urllib.request #pip install urllib3
import json


def voice(message):
    request2text(message.voice.file_id, message.chat.id)

def wav2text(dest_filename, id, file_name):
    r = sr.Recognizer()
    message = sr.AudioFile(dest_filename)
    with message as source:
        audio = r.record(source)
    try:
        result = r.recognize_google(audio, language="ru_RU")
        bot.send_message(id, format(result))
        os.remove(dest_filename)
        os.remove(file_name)
    except sr.UnknownValueError:
        bot.send_message(id, 'Говори четче')
        os.remove(dest_filename)
        os.remove(file_name)

def oga2wav(file_name, id):
    src_filename = file_name
    dest_filename = file_name + '.wav'
    process = subprocess.run(['ffmpeg', '-i', src_filename, dest_filename]) #Специально написана переменная, которая не используется, чтобы голосовые не сохраняла на хостинге
    wav2text(dest_filename, id, file_name)

def donwload(file_path, file_id, id):
    url = 'https://api.telegram.org/file/bot1202599286:AAFtLRh52UdFipEECkBWArwcIOCT5Uj5sqc/' + file_path
    urllib.request.urlretrieve(url, file_id + '.oga')
    file_name = file_id + '.oga'
    oga2wav(file_name, id)

def request2text(file_id, id):
    r = s.get('https://api.telegram.org/bot1202599286:AAFtLRh52UdFipEECkBWArwcIOCT5Uj5sqc/getFile?file_id=' + file_id)
    r = json.loads(r.text)
    donwload(r['result']['file_path'], r['result']['file_id'], id)