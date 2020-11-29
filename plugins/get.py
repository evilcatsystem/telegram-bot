import re #pip install regex
import requests #pip install requests
#________________________________________________________________________________________________________________
#Рандомные цитаты с http://fucking-great-advice.ru
#________________________________________________________________________________________________________________
def urls_citata():
    contents = requests.get('http://fucking-great-advice.ru/api/random').json() #Берем котеек
    url = contents['text']
    return url
