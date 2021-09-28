import requests
from bs4 import BeautifulSoup

raw = requests.get("https://news.ycombinator.com")
html = BeautifulSoup(raw.text, 'html.parser')

page = 1
for page in range(1, 4):
    raw = requests.get("https://news.ycombinator.com/news?p="+str(page),
                       headers = {"User - Agent": "Mozilla /5.0"})

# 컨테이너: tr.athing
# 순위: span.rank
# 제목: a.storylink
# 출처: span.sitebit

#1. 컨테이너 수집하기
articles = html.select("tr.athing")

#2. 기사 데이터 수집하기
for ar in articles:
    rank = ar.select_one("span.rank").text
    title = ar.select_one("a.storylink").text

    print(rank, title)
    print("=" * 50)