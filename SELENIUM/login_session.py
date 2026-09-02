from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("user-data-dir=/somewhere")
# 브라우저 자동종료 방지
options.add_experimental_option("detach", True)
# 브라우저 실행중 로깅을 비활성화
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get("https://www.amoremall.com/kr/ko/product/detail?onlineProdSn=63063&onlineProdCode=111970001785")

