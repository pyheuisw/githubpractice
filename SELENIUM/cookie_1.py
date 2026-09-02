import pickle
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www-ecp-stgrenew.amoremall.com/")

# 수동 또는 자동 로그인을 진행합니다.
# 로그인에 필요한 충분한 시간을 줍니다.
time.sleep(20) 

# 로그인 완료 후 쿠키 추출 및 pickle 파일 저장
cookies = driver.get_cookies()
with open("cookies.pkl", "wb") as f:
    pickle.dump(cookies, f)

print("쿠키 저장 완료!")
driver.quit()