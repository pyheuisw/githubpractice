from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException  # 흔히 만나는 예외(에러) 종류
from selenium.webdriver.remote.webdriver import WebDriver  # 타입 힌트(이 변수가 WebDriver라는 뜻)용 임포트
from selenium.webdriver.support import expected_conditions as EC  # "보인다", "클릭 가능하다" 같은 대기 조건 모음
from selenium.webdriver.support.ui import WebDriverWait  # 지정한 시간만큼 조건이 만족될 때까지 기다려주는 클래스


class BasePage:                   # 다른 Page 클래스들이 상속받을 기본 클래스
    BASE_URL = "https://automationexercise.com"  # 사이트 기본 주소 상수

    def __init__(self, driver: WebDriver, timeout: int = 10):  # Page 객체 생성 시 실행되는 초기화 메서드(최대 대기 10초)
        self.driver = driver      # 전달받은 브라우저 드라이버를 이 인스턴스의 속성으로 저장
        self.wait = WebDriverWait(driver, timeout)  # 최대 timeout초 동안 기다리는 대기 객체 생성

    def open(self, path: str = "/") -> None:  # 특정 경로(기본값 "/")를 여는 메서드; -> None은 반환값이 없음을 의미
        self.driver.get(f"{self.BASE_URL}{path}")  # 기본 URL과 경로를 합쳐 페이지 이동

    def wait_visible(self, locator):          # locator(예: (By.CSS_SELECTOR, "...")) 요소가 화면에 보일 때까지 대기
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_clickable(self, locator):        # 요소가 보이고 활성화되어 클릭 가능한 상태가 될 때까지 대기
        return self.wait.until(EC.element_to_be_clickable(locator))

    def scroll_to_element(self, element) -> None:  # 브라우저 화면을 움직여 해당 요소가 보이게 스크롤
        self.driver.execute_script(           # 파이썬에서 브라우저 안의 JavaScript를 직접 실행
            "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",  # 요소를 화면 중앙 근처로 맞춤
            element,                          # 위 JS 코드의 arguments[0] 자리에 element가 들어감
        )

    def click(self, locator) -> None:         # 요소를 찾고 스크롤한 뒤 클릭하는 메서드
        el = self.wait_clickable(locator)     # 클릭 가능할 때까지 기다린 뒤 웹 요소(el)를 받음
        self.scroll_to_element(el)            # 클릭하기 편하도록 화면 중앙으로 스크롤
        try:
            el.click()                        # 일반적인 Selenium 클릭 시도
        except ElementClickInterceptedException:  # 다른 배너나 고정 헤더가 클릭을 가로막았을 때 발생하는 예외
            # 일반 클릭이 막힐 경우 JS로 직접 클릭 이벤트를 발생시키는 실무용 우회(폴백) 처리
            self.driver.execute_script("arguments[0].click();", el)

    def type_text(self, locator, text: str) -> None:  # 입력칸에 기존 값을 지우고 새 텍스트를 입력
        el = self.wait_visible(locator)       # 입력칸이 보일 때까지 대기
        self.scroll_to_element(el)            # 입력칸으로 스크롤
        el.clear()                            # 기존에 들어있을 수 있는 글자 삭제
        el.send_keys(text)                    # 키보드로 타이핑하듯 text 입력

    def get_text(self, locator) -> str:       # 요소의 화면 텍스트를 읽어 앞뒤 공백을 제거해 반환
        return self.wait_visible(locator).text.strip()

    def is_visible(self, locator, timeout: int = 3) -> bool:  # 짧은 시간(기본 3초) 안에 보이는지 True/False로 확인
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True                       # 제한 시간 안에 보이면 True
        except TimeoutException:              # 제한 시간 안에 안 보이면 TimeoutException 발생
            return False                      # 에러로 테스트를 멈추지 않고 False 반환