#!/usr/bin/python

from config import bot, chat_id
import requests
from bs4 import BeautifulSoup
from telebot import types
from time import sleep
from lxml import html
from plugins.error import Error
from plugins.error import in_chat
from selenium import webdriver
import os

@in_chat()
def search(m):
    bot.delete_message(m.chat.id, m.message_id)
    try:
        keyboard = types.InlineKeyboardMarkup()
        keyboard_delete = types.InlineKeyboardButton(text = "❌", callback_data = "delete")
        keyboard.add(keyboard_delete)

        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument ("--headless")
        #chrome_options.add_argument ("--disable-dev-shm-usage")
        chrome_options.add_argument ("--no-sandbox")
        prefs = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2, 'javascript': 1, 
                            'plugins': 2, 'popups': 2, 'geolocation': 2, 
                            'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2, 
                            'mouselock': 2, 'mixed_script': 2, 'media_stream': 2, 
                            'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2, 
                            'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2, 
                            'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2, 
                            'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2, 
                            'durable_storage': 2}}
        chrome_options.add_experimental_option('prefs', prefs)
        chrome_options.add_argument("start-maximized")
        chrome_options.add_argument("disable-infobars")
        chrome_options.add_argument("--disable-extensions")

        driver = webdriver.Chrome(executable_path = os.environ.get("CHROMEDRIVER_PATH"), chrome_options = chrome_options)
        text = m.text[8:]
        info_user = text.replace(" ", "+")
        driver.get(f"https://duckduckgo.com/?q={info_user}+russian&ia=web")                     # Запрос
        SEARCH_DROP = slice(5)

        finds = driver.find_elements_by_xpath("//a[@class='result__a']")[SEARCH_DROP]
        finds_links = driver.find_elements_by_xpath("//a[@class='result__a']")[SEARCH_DROP]

        ############################################################
        info = [line.text for line in finds]
        links = [line.get_attribute('href') for line in finds_links]      # Обработка текста/ссылок
        ############################################################
        full = [f"[{line}]({line2})" for line, line2 in zip(info, links)]
        full_numbers = [f"{idx}. {val}" for idx, val in enumerate(full, 1)]
        full_numbers.insert(0, f"_Результат по запросу:_ *{text}*")
        bot.send_message(m.chat.id, "\n\n".join(full_numbers), parse_mode = "Markdown", reply_markup = keyboard)
    except Exception as e:
        print ("search.py " + str(e))
        bot.send_message(m.chat.id, "*Результаты были не найдены!*", parse_mode = "Markdown", reply_markup = keyboard)
    finally:
        driver.close()

@in_chat()
def search_youtube(m):
    bot.delete_message(m.chat.id, m.message_id)
    try:
        keyboard = types.InlineKeyboardMarkup()
        keyboard_delete = types.InlineKeyboardButton(text = "❌", callback_data = "delete")
        keyboard.add(keyboard_delete)

#######################################
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument ("--headless")
        #chrome_options.add_argument ("--disable-dev-shm-usage")
        chrome_options.add_argument ("--no-sandbox")
        prefs = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2, 'javascript': 1, 
                            'plugins': 2, 'popups': 2, 'geolocation': 2, 
                            'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2, 
                            'mouselock': 2, 'mixed_script': 2, 'media_stream': 2, 
                            'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2, 
                            'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2, 
                            'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2, 
                            'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2, 
                            'durable_storage': 2}}
        chrome_options.add_experimental_option('prefs', prefs)
        chrome_options.add_argument("start-maximized")
        chrome_options.add_argument("disable-infobars")
        chrome_options.add_argument("--disable-extensions")

        driver = webdriver.Chrome(executable_path = os.environ.get("CHROMEDRIVER_PATH"), chrome_options = chrome_options)
#######################################
        
        text = m.text[4:]
        info_user = text.replace(" ", "+")
        driver.get(f"https://www.youtube.com/results?search_query={info_user}")
        find = driver.find_elements_by_xpath("//a[@id='video-title']")

        find_links = []
        find_labels = []

        for line in find:
            if line.get_attribute('aria-label') == None:
                pass
            else:
                find_labels.append(line.get_attribute('aria-label'))

        for line in find:
            if line.get_attribute('href') == None:
                pass
            else:
                find_links.append(line.get_attribute('href'))


        find_labels = find_labels[:5]
        find_links = find_links[:5]

        index_list = [] #
        for line in find_labels:
            find_index = line.find("by")
            AVTOR = slice(find_index - 1)
            index_list.append(line[AVTOR])

        full = [f"[{line}]({line2})"for line, line2 in zip(index_list, find_links)]
        full = [f"{val}. {line}" for val, line in enumerate(full, 1)]
        full.insert(0, f"_Результат по запросу в Youtube:_ *{text}*")
        bot.send_message(m.chat.id, "\n\n".join(full), parse_mode = "Markdown", reply_markup = keyboard)

    except Exception as e:
        print ("search.py " + e)
    finally:
        driver.close()
