import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import openpyxl
import pandas as pd


options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)


URL = 'https://datalab.naver.com/shoppingInsight/sCategory.naver'
driver.get(URL)

excelfile = openpyxl.Workbook()
sheet = excelfile.active


button1 = '식품'
button2 = '유가공룡'
button3 = '치즈'
button4 = '피자치즈'


driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div[1]/div/div/div[1]/div/div[1]/span').click()
driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div[1]/div/div/div[1]/div/div[1]/ul/li[7]/a').click()

if button1 != '':
    driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div[1]/div/div/div[1]/div/div[2]/span').click()
    driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div[1]/div/div/div[1]/div/div[2]/ul/li[7]/a').click()

if button2 != '':
    driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div[1]/div/div/div[1]/div/div[3]/span').click()
    driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div[1]/div/div/div[1]/div/div[3]/ul/li[1]/a').click()

if button3 != '':
    driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div[1]/div/div/div[1]/div/div[4]/span').click()
    driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div[1]/div/div/div[1]/div/div[4]/ul/li[2]/a').click()



driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div[1]/div/a').click()


page_info = []

for i in range(20):
    for i in range(1, 21):
        rank = driver.find_element(By.XPATH, f'//*[@id="content"]/div[2]/div/div[2]/div[2]/div/div/div[1]/ul/li[{i}]/a/span').text
        name = driver.find_element(By.XPATH, f'//*[@id="content"]/div[2]/div/div[2]/div[2]/div/div/div[1]/ul/li[{i}]/a').text
        name = name.split('\n', 1)[1]
        print(page_info)
        page_info.append([rank, name])
    

d = pd.DataFrame(page_info, columns=['순위', '상품명'])
print(d)

d.to_excel("test.xlsx", index=False)

time.sleep(3)
print("정상 작동")

