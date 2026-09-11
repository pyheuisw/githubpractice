import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Appium Options 설정
options = UiAutomator2Options()
options.platform_name = "Android"
options.automation_name = "UiAutomator2"
options.device_name = "Galaxy S10"

# 앱이 있는 경우 app_package, app_activity 사용
options.app_package = "com.amorepacific.amorepacificmall"  # 실제 테스트 대상 앱 패키지명
options.app_activity = ".MainActivity"      # 실제 메인 액티비티명
options.no_reset = True

# 1. 사용 중인 Chromedriver 경로 (154 버전)
options.set_capability(
    "appium:chromedriverExecutable", 
    r"C:\Users\comes\Downloads\chromedriver-win64\chromedriver.exe"  # 실제 154버전 파일 경로
)

# 2. 🔑 [핵심] Chromedriver 프로세스 멈춤 방지 옵션 추가
options.set_capability("appium:chromedriverArgs", [
    "--no-sandbox",
    "--disable-dev-shm-usage",
    "--disable-gpu"
])

# 3. ChromeOptions 패키지 연결 명시
options.set_capability("appium:chromeOptions", {
    "androidPackage": "com.amorepacific.amorepacificmall",
    "androidUseRunningApp": True
})

# 2. Appium 서버 연결
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
time.sleep(3)

try:
    wait = WebDriverWait(driver, 15)

    # -------------------------------------------------------------
    # 🔑 [핵심] 3. NATIVE_APP에서 WEBVIEW Context로 전환하기
    # -------------------------------------------------------------
    # 앱 내부에서 해당 URL(아모레몰) 웹뷰 페이지가 화면에 켜질 때까지 대기
    time.sleep(5) 

    # 현재 연결 가능한 모든 컨텍스트 출력 (디버깅용)
    available_contexts = driver.contexts
    print("사용 가능한 Contexts:", available_contexts)

    # WEBVIEW 컨텍스트 찾아서 전환
    webview_context = None
    for context in available_contexts:
        if "WEBVIEW_com.amorepacific.amorepacificmall" in context:
            webview_context = context
            break

    if webview_context:
        driver.switch_to.context(webview_context)
        print(f"✅ Successful Context Switch: {webview_context}")
    else:
        print("⚠️ WEBVIEW Context를 찾지 못했습니다. Native 스크립트로 동작을 시도합니다.")

    # -------------------------------------------------------------
    # 4. 웹뷰로 전환된 상태에서 기존 웹 요소 조작 (Selenium 동일)
    # -------------------------------------------------------------

    # 옵션 선택 버튼 클릭
    opt_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="__next"]/section/section[1]/section/div/div/div[1]/div[1]/div[2]/div[3]/div/button[3]')
    ))
    opt_btn.click()
    time.sleep(2)

    # 상품 카드(썸네일) 목록 대기 및 클릭
    elements = wait.until(EC.presence_of_all_elements_located(
        (By.XPATH, '//button[@class="thumbProdCard"]')
    ))
    driver.execute_script("arguments[0].click();", elements[1])
    time.sleep(2)

    # 구매하기 / 장바구니 등 두 번째 동작 버튼 클릭
    action_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="__next"]/section/section[1]/section/div/div/div[1]/div[1]/div[2]/div[3]/div/section[2]/div[2]/div/div/div[4]/button[2]')
    ))
    action_btn.click()
    time.sleep(2)

    # 로그인 링크 이동
    login_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="__next"]/section/section[2]/div[2]/div/div/div[1]/div[1]/div[1]/a')
    ))
    login_link.click()
    time.sleep(2)

    # ID / PW 입력 및 로그인 버튼 클릭
    id_input = wait.until(EC.presence_of_element_at_located((By.XPATH, '//*[@id="loginid"]')))
    id_input.send_keys("pyheuisw")

    pw_input = driver.find_element(By.XPATH, '//*[@id="loginpassword"]')
    pw_input.send_keys("qwer12344")

    login_btn = driver.find_element(By.XPATH, '//*[@id="dologin"]')
    login_btn.click()

    time.sleep(5)

finally:
    # (선택) 네이티브 영역으로 다시 복귀할 때
    # driver.switch_to.context('NATIVE_APP')
    driver.quit()