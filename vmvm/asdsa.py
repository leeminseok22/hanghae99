from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

import time


def crawl_wth():

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('https://weather.naver.com/today/06110565', headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    weathers = soup.select(
        '#content > div > div.section_center > div.card.card_today > div.today_weather > div.weather_area')
    for weath in weathers:
        a = weath.select_one('div.weather_now > div > strong')
        if a is not None:
            temper_receive = a.text.partition('도')[2]
            print("온도는: ", temper_receive)
    return temper_receive


from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.mpsb1.mongodb.net/Cluster0?retryWrites=true&w=majority',
                     tlsCAFile=ca)
db_list = client.list_databases()
# for i in db_list:
#     print("db_list: ", i)

db = client.sparta.weather
# print("db name: ", db)

kpb_db = client.get_database("sparta")

collection_list = sparta_db.list_collections()
print("coll_list: ", collection_list)

for i in collection_list:
    print(i)


@app.route('/')
def home():
    return render_template('adfdsf.html')


@app.route("/weather", methods=["GET"])
def weather_post():

    temper_receive = crawl_wth()
    print("온도?: ", temper_receive)

    wea = {
        'data': 0,
        'tem': temper_receive
    }

    if len(list(db.weather.find())) == 0:
        db.weather.insert_one(wea)
        return "inserted"
    else:
        query = {"data": 0}
        new_data = {"$set": {"tem": temper_receive}}
        db.weather.update_one(query, new_data)
        return "업데이트."


@app.route("/check", methods=['GET'])
def check_db():
    wth = db.weather.find_one()

    if wth is None:
        data = "없음."
    else:
        data = wth['tem']
        print("check wth : ", wth)

    # return render_template("adfdsf.html", check_data=data)
    return jsonify(weathers=data)

@app.route("/del_all", methods=['GET'])
def del_all_data():
    db.weather.delete_many({})
    return "다 지움 ㅅㄱ"


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)