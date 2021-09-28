#1. 네이버 로그인하기
from selenium import webdriver
import time

# 크롬창(웹드라이버) 열기
driver = webdriver.Chrome("./chromedriver")

# 네이버 로그인 페이지 접속
driver.get("https://www.facebook.com")

# 페이지 접속 후 시간 지연
time.sleep(0.5)

# 입력창에 검색어 입력
id_box = driver.find_element_by_css_selector("input#email")
id_box.send_keys("01089351693")
password_box = driver.find_element_by_css_selector("input#pass")
password_box.send_keys("ocean2nd")

# 로그인 버튼 클릭
login_button = driver.find_element_by_css_selector("input#u_0_e")
login_button.click()