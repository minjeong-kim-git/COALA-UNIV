#1. 네이버 로그인하기
from selenium import webdriver
import time

# 크롬창(웹드라이버) 열기
driver = webdriver.Chrome("./chromedriver")

# 네이버 로그인 페이지 접속
driver.get("https://nid.naver.com")

# 페이지 접속 후 시간 지연
time.sleep(0.5)

# 입력창에 검색어 입력
id_box = driver.find_element_by_css_selector("input#id.int")
id_box.send_keys("fran0666")
password_box = driver.find_element_by_css_selector("input#pw.int")
password_box.send_keys("Field1st!")

# 로그인 버튼 클릭
login_button = driver.find_element_by_css_selector("input.btn_global")
login_button.click()