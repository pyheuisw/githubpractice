import time
from appium import webdriver
from appium.options.android import UiAutomator2Options

options = UiAutomator2Options()

# 1. 가상장치(에뮬레이터) 정보 설정
options.platform_name = "Android"
options.automation_name = "UiAutomator2"
options.device_name = "Pixel 7"
options.udid = "emulator-5554"

# 2. 확인된 정확한 패키지명 및 Activity 경로 설정
options.app_package = "com.amorepacific.amorepacificmall"
options.app_activity = ".MainActivity"

# 대기 조건 및 리셋 옵션
options.app_wait_activity = "*"
options.no_reset = True  # 로그인 정보 등 기존 앱 데이터 유지

# 3. Appium 드라이버 연결 (연결과 동시에 앱 자동 실행)
driver = webdriver.Remote(command_executor="http://127.0.0.1:4723", options=options)

print("앱 자동 실행 성공!")

time.sleep(5)