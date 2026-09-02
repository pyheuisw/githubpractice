import pickle
import time
from selenium import webdriver

driver = webdriver.Chrome()

# ⚠️ 중요: 쿠키를 추가하려면 먼저 해당 사이트의 도메인에 접속해 있어야 합니다.
driver.get("https://www-ecp-stgrenew.amoremall.com/")

# 저장해둔 쿠키 파일 불러오기
try:
    with open("cookies.pkl", "rb") as f:
        cookies = pickle.load(f)
        for cookie in cookies:
            # expiry 값 관련 에러 방지를 위해 수수료 정수 처리
            if 'expiry' in cookie:
                cookie['expiry'] = int(cookie['expiry'])
            driver.add_cookie(cookie)
            
    # 쿠키 적용을 위해 페이지 새로고침
    driver.refresh()
    print("쿠키 적용 성공! 로그인 상태 유지됨")
except FileNotFoundError:
    print("쿠키 파일이 없습니다. 먼저 쿠키 저장 코드를 실행해주세요.")

# 이제 로그인된 상태로 목적지 페이지로 이동
driver.get("https://www-ecp-stgrenew.amoremall.com/kr/ko/product/detail?onlineProdSn=12438&onlineProdCode=111610000002")

time.sleep(10)