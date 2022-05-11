# 크롤링 패키지
import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# DB패키지
from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.mpsb1.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.sparta.mini

# def crawl_movie():




# print(current_movies) #데이터 뽑히는 지 확인

# 메인화면에서 해당 영화 페이지를 클릭하면 link 값을 sub화면에 전달해줌 -> 안해도됨 걍 각자 쓰면될듯
# sub화면으로 페이지 변경
def crawl_movie():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('https://movie.naver.com/movie/running/current.naver?view=list&tab=normal&order=likeCount',
                        headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    current_movies = soup.select('#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li')
    for movie in current_movies:
        a = movie.select_one('dl > dt > a').text
        if a is not None:
            # 타이틀
            title_receive = a
            # 링크 - 상세 페이지 링크혹시몰라서 넣음(안 필요할듯^^)
            link_receive = movie.select_one('dl > dt > a')['href']
            # 이미지
            img_receive = movie.select_one('div > a > img')['src']
            # 평점(데이터 값이 숫자가 아니라서 변수명에 str표시함)
            # 평점이 0.00이면 평점없음으로 변경
            star_receive = movie.select_one('dl > dd.star > dl.info_star > dd > div > a > span.num').text
            if star_receive == '0.00':
                star_receive = '평점없음'


                return star_receive, img_receive, title_receive, link_receive

db_list = client.list_databases()
# for i in db_list:
#     print("db_list: ", i)

db = client.sparta.mini
# print("db name: ", db)

sparta_db = client.get_database("sparta")

collection_list = sparta_db.list_collections()
print("coll_list: ", collection_list)


@app.route('/')
def home():
    return render_template('main.html')

@app.route("/weather", methods=["GET"])
def movie_post():

    crawl_movie()
    print("온도?: ", crawl_movie())

    doc = {
        'data': 0,
        'title': title_receive,
        'link': link_receive,
        'img': img_receive,
        'star': star_receive
    }
    db.sparta.mini.insert_many(doc)



    if len(list(db.mini.find())) == 0:
        db.mini.insert_one(doc)
        return "inserted"
    else:
        query = {"data": 0}
        new_data = {"$set": {"title": title_receive}}
        db.mini.update_one(query, new_data)
        return "업데이트."
