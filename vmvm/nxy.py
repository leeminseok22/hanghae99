import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://weather.naver.com/today/06110565',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

weathers = soup.select('#content > div > div.section_center > div.card.card_today > div.today_weather > div.weather_area')

for weath in weathers:
    a = weath.select_one('div.weather_now > div > strong')
    if a is not None:
        temper = a.text.partition('도')[2]
        print(temper)
