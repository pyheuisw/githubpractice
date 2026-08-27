
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()

URL = 'https://www.amoremall.com/kr/ko/display/search/main?type=search'
driver.get(URL)
driver.maximize_window()

time.sleep(3)

element = driver.find_element(By.XPATH, '//*[@id="inputSearch"]')
element.send_keys("스킨케어")

time.sleep(3)

element.send_keys(Keys.ENTER)

time.sleep(3)


last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        break

    last_height = new_height


time.sleep(3)


target = driver.find_element(By.XPATH, '//*[@id="__next"]/section/section[1]/section/section/div[1]')

# 해당 요소까지 마우스 이동 → 요소가 화면에 보이도록 스크롤
ActionChains(driver).scroll_to_element(target).perform()


time.sleep(5)
driver.close()


