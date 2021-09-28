import requests
from bs4 import BeautifulSoup

raw = requests.get("https://tv.naver.com/r/")
html = BeautifulSoup(raw.text, 'html.parser')
print(html)

# 1-3위
container = html.select("div.inner")

for cont in container:
    title = cont.select_one("dt.title")
    chn = cont.select_one("dd.chn")
    hit = cont.select_one("span.hit")
    like = cont.select_one("span.like")

    print(title.text.strip())
    print(chn.text.strip())
    print(hit.text.strip())
    print(like.text.strip())
    print("=" * 50)

# 4-100위 컨테이너: div.cds
# 제목: dt.title
# 채널명: dd.chn
# 재생수: span.hit
# 좋아요 수: span.like

#1. 컨테이너 수집
container = html.select("div.cds")

#2. 영상 데이터 수집
for cont in container:
    title = cont.select_one("dt.title")
    chn = cont.select_one("dd.chn")
    hit = cont.select_one("span.hit")
    like = cont.select_one("span.like")

    print(title.text.strip())
    print(chn.text.strip())
    print(hit.text.strip())
    print(like.text.strip())
    print("=" * 50)

#3. 반복하기