import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

URL = 'https://www.amoremall.com/kr/ko/beautypoint/app/receipt/app/agreePage.do'
driver.get(URL)
driver.maximize_window()


element = driver.find_element(By.XPATH, '/html/body/section/section[1]/div/p/span[1]/label/span[1]')


if element.is_selected() == False:
    print("미선택 상태입니다.")
    element.click()
else :
    print("선택 상태입니다.")


time.sleep(5)


driver.find_element(By.XPATH, '/html/body/section/section[1]/div/p/span[2]/label/span[1]').click()


time.sleep(5)
driver.close()