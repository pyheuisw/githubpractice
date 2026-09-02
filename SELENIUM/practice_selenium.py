
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()

URL = 'https://www.amoremall.com/kr/ko/product/detail?onlineProdSn=63063&onlineProdCode=111970001785'
driver.get(URL)
driver.maximize_window()

time.sleep(3)

driver.find_element(By.XPATH, '//*[@id="__next"]/section/section[1]/section/div/div/div[1]/div[1]/div[2]/div[3]/div/button[3]').click()

time.sleep(3)

elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//button[@class="thumbProdCard"]')))
driver.execute_script("arguments[0].click();", elements[1])


time.sleep(3)


driver.find_element(By.XPATH, '//*[@id="__next"]/section/section[1]/section/div/div/div[1]/div[1]/div[2]/div[3]/div/section[2]/div[2]/div/div/div[4]/button[2]').click()


time.sleep(3)

driver.find_element(By.XPATH, '//*[@id="__next"]/section/section[2]/div[2]/div/div/div[1]/div[1]/div[1]/a').click()

time.sleep(3)

driver.find_element(By.XPATH, '//*[@id="loginid"]').send_keys("pyheuisw")
driver.find_element(By.XPATH, '//*[@id="loginpassword"]').send_keys("qwer12344")

driver.find_element(By.XPATH, '//*[@id="dologin"]').click()



time.sleep(10)
driver.quit()

