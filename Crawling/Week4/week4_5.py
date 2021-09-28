import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(["제목", "채널명", "재생수", "좋아요수"])

raw = requests.get("https://tv.naver.com/r/")
# print(raw.text)
html = BeautifulSoup(raw.text, 'html.parser')
print(html)

# 1-3위 컨테이너: div.inner
# 제목: dt.title
# 채널명: dd.chn
# 재생수: span.hit
# 좋아요 수: span.like

#1. 컨테이너 수집하기
container = html.select("div.inner")
# print(container[0])

#2. 영상 데이터 수집하기
for cont in container:
    title = cont.select_one("dt.title").text.strip()
    chn = cont.select_one("dd.chn").text.strip()
    hit = cont.select_one("span.hit").text.strip()
    like = cont.select_one("span.like").text.strip()

    hit = hit.replace("재생 수", "")
    like = like.replace("좋아요 수", "")

    sheet.append([title, chn, hit, like])

#    print(title.text.strip())
#   print(chn.text.strip())
#    print(hit.text.strip())
#    print(like.text.strip())
#    print("=" * 50)

wb.save("navertv.xlsx")
