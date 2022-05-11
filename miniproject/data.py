#크롤링 패키지
import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
#DB패키지
from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.mpsb1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', tlsCAFile=ca)

db = client.dbcseven

@app.route('/')
def main():
    return render_template('main.html')

# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get('https://movie.naver.com/movie/running/current.naver?view=list&tab=normal&order=likeCount',headers=headers)
#
# soup = BeautifulSoup(data.text, 'html.parser')
#
# current_movies = soup.select('#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li')
# #print(current_movies) #데이터 뽑히는 지 확인
#
# #메인화면에서 해당 영화 페이지를 클릭하면 link 값을 sub화면에 전달해줌 -> 안해도됨 걍 각자 쓰면될듯
# #sub화면으로 페이지 변경
#
# for movie in current_movies:
#     fa = movie.select_one('dl > dt > a')
#     if fa is not None:
#         #타이틀
#         title = fa.text
#         #링크 - 상세 페이지 링크혹시몰라서 넣음(안 필요할듯^^)
#         link = movie.select_one('dl > dt > a')['href']
#         #이미지
#         img = movie.select_one('div > a > img')['src']
#         #평점(데이터 값이 숫자가 아니라서 변수명에 str표시함)
#         #평점이 0.00이면 평점없음으로 변경
#         str_grade = movie.select_one('dl > dd.star > dl.info_star > dd > div > a > span.num').text
#         # print(title, link, img, str_grade)
#
#         doc = {
#
#             'tit': title,
#             'lin': link,
#             'img': img,
#             'str': str_grade
#         }
#
#         db.minicseven.insert_one(doc)



@app.route("/titles", methods=["GET"])
def title_get():
    titles = list(db.minicseven.find({'til': 'title'}, {'_id': False}))


    return "가져왔데숭숭"



if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)