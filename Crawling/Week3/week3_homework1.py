import requests
from bs4 import BeautifulSoup

for page in range(1, 6):
    raw = requests.get("hhttps://series.naver.com/ebook/top100List.nhn?page="+str(page),
                       headers = {"User-Agent": "Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')

# 컨테이너: div.1st_thum_wrap li
# 제목: a strong
# 작가: span.writer

#1. 컨테이너 수집하기
books = html.select("div.1st_thum_wrap li")

#2. 데이터 수집하기
for b in books:
    title = b.select_one("a strong").text
    writer = b.select_one("span.writer").text

    print(title, writer)