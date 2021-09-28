from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.instagram.com/explore/tags/ootd/")
time.sleep(1)

login_button = driver.find_element_by_css_selector('button.sqdOP.L3NKy.y3zKF')
login_button.click()

time.sleep(3)
driver.find_element_by_name('username').send_keys('-')
driver.find_element_by_name('password').send_keys('-')


driver.find_element_by_css_selector('button.sqdOP.L3NKy.y3zKF').click()
time.sleep(10)


post = driver.find_elements_by_css_selector("div.eLAPa")
post = post[:12]
for p in post:
    p.click()
    time.sleep(1)
    feeds = driver.find_element_by_css_selector("div.C7I1f.X7jCj div.C4VMK>span")
    print(feeds)
    close_button = driver.find_element_by_css_selector("div.Igw0E button.wpO6b")
    close_button.click()
    time.sleep(1)