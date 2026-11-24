import allure  # Allure 테스트 리포트에 단계(@allure.step)나 첨부파일(allure.attach)을 남기기 위해 불러옴
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException  # 클릭이 방해받거나 대기 시간이 초과될 때 나는 에러(예외) 종류
from selenium.webdriver.common.action_chains import ActionChains  # 마우스 이동·호버 등 복합 마우스 동작을 묶어서 실행할 때 쓰는 도구
from selenium.webdriver.common.by import By  # 웹페이지 요소를 어떤 기준(CSS 선택자, ID 등)으로 찾을지 지정할 때 쓰는 상수 모음
from selenium.webdriver.remote.webdriver import WebDriver  # 타입 힌트용: 이 변수가 브라우저 조종 객체(WebDriver)임을 표시
from selenium.webdriver.support import expected_conditions as EC  # "화면에 보인다", "클릭 가능하다" 같은 대기 조건들을 EC라는 짧은 이름으로 불러옴
from selenium.webdriver.support.ui import Select, WebDriverWait  # Select: <select> 드롭다운 메뉴 선택용 / WebDriverWait: 조건이 될 때까지 기다려주는 도구


class HomePage:  # 웹페이지의 요소(로케이터)와 화면 조작 기능을 하나로 묶어 둔 설계도(클래스)
    BASE_URL = "https://automationexercise.com"  # 클래스 안에서 공통으로 쓸 기본 웹사이트 주소(상수처럼 대문자로 작성)

    # --- 메인 화면 로케이터 ---
    # 아래 로케이터들은 (찾는_방법, 찾는_값) 형태의 '튜플(tuple, 소괄호로 묶은 수정 불가 데이터)'로 미리 정리해 둠
    FIRST_PRODUCT_CARD = (By.CSS_SELECTOR, ".features_items .product-image-wrapper:first-of-type")  # 상품 목록(.features_items) 안의 첫 번째 상품 카드 전체 영역
    FIRST_PRODUCT_ADD_BTN = (  # 긴 문자열을 읽기 쉽게 괄호 안에서 여러 줄로 나눈 것
        By.CSS_SELECTOR,  # CSS 선택자 방식으로 찾겠다는 뜻
        ".features_items .product-image-wrapper:first-of-type .productinfo .add-to-cart",  # 첫 번째 상품 카드 안 기본 영역(.productinfo)의 'Add to cart' 버튼
    )
    FIRST_PRODUCT_OVERLAY_ADD_BTN = (
        By.CSS_SELECTOR,
        ".features_items .product-image-wrapper:first-of-type .product-overlay .add-to-cart",  # 마우스를 올렸을 때 겹쳐 뜨는 영역(.product-overlay)의 'Add to cart' 버튼
    )
    FIRST_PRODUCT_NAME = (
        By.CSS_SELECTOR,
        ".features_items .product-image-wrapper:first-of-type .productinfo p",  # 첫 번째 상품의 이름이 들어 있는 <p> 태그
    )
    MODAL_VIEW_CART_LINK = (By.CSS_SELECTOR, "#cartModal a[href='/view_cart']")  # 장바구니 담기 팝업(#cartModal) 안의 'View Cart' 이동 링크
    HEADER_SIGNUP_LOGIN = (By.CSS_SELECTOR, "header a[href='/login']")  # 상단 메뉴(header)의 회원가입/로그인(/login) 링크

    # --- 회원가입/로그인 로케이터 ---
    SIGNUP_NAME = (By.CSS_SELECTOR, "[data-qa='signup-name']")  # data-qa 속성이 'signup-name'인 이름 입력칸
    SIGNUP_EMAIL = (By.CSS_SELECTOR, "[data-qa='signup-email']")  # data-qa 속성이 'signup-email'인 이메일 입력칸
    SIGNUP_BTN = (By.CSS_SELECTOR, "[data-qa='signup-button']")  # 회원가입 시작('Signup') 버튼
    PASSWORD = (By.ID, "password")  # HTML id가 'password'인 비밀번호 입력칸
    FIRST_NAME = (By.ID, "first_name")  # HTML id가 'first_name'인 이름(First name) 입력칸
    LAST_NAME = (By.ID, "last_name")  # HTML id가 'last_name'인 성(Last name) 입력칸
    ADDRESS = (By.ID, "address1")  # HTML id가 'address1'인 주소 입력칸
    COUNTRY = (By.ID, "country")  # HTML id가 'country'인 국가 선택 드롭다운(<select>)
    STATE = (By.ID, "state")  # HTML id가 'state'인 주/도 입력칸
    CITY = (By.ID, "city")  # HTML id가 'city'인 도시 입력칸
    ZIPCODE = (By.ID, "zipcode")  # HTML id가 'zipcode'인 우편번호 입력칸
    MOBILE = (By.ID, "mobile_number")  # HTML id가 'mobile_number'인 휴대폰 번호 입력칸
    CREATE_ACCOUNT_BTN = (By.CSS_SELECTOR, "[data-qa='create-account']")  # 'Create Account' 계정 생성 완료 버튼
    ACCOUNT_CREATED_MSG = (By.CSS_SELECTOR, "[data-qa='account-created']")  # 계정 생성 성공 시 뜨는 안내 문구 요소
    CONTINUE_BTN = (By.CSS_SELECTOR, "[data-qa='continue-button']")  # 계정 생성 후 다음 화면으로 넘어가는 'Continue' 버튼

    # --- 장바구니 로케이터 ---
    CART_ITEMS_NAME = (By.CSS_SELECTOR, "#cart_info_table tbody tr .cart_description h4 a")  # 장바구니 표(#cart_info_table) 각 행(tr)에 담긴 상품명 링크들
    PROCEED_TO_CHECKOUT = (By.CSS_SELECTOR, ".check_out")  # 장바구니에서 결제 단계로 넘어가는 'Proceed To Checkout' 버튼

    # --- 주문/결제 로케이터 ---
    COMMENT_TEXTAREA = (By.CSS_SELECTOR, "#ordermsg textarea[name='message']")  # 주문서 화면(#ordermsg)의 배송/주문 코멘트 입력란
    PLACE_ORDER_BTN = (By.CSS_SELECTOR, "a[href='/payment']")  # 결제 화면(/payment)으로 이동하는 'Place Order' 버튼
    NAME_ON_CARD = (By.CSS_SELECTOR, "[data-qa='name-on-card']")  # 카드 명의자 이름 입력칸
    CARD_NUMBER = (By.CSS_SELECTOR, "[data-qa='card-number']")  # 카드 번호 입력칸
    CVC = (By.CSS_SELECTOR, "[data-qa='cvc']")  # 카드 CVC(보안코드) 입력칸
    EXPIRY_MONTH = (By.CSS_SELECTOR, "[data-qa='expiry-month']")  # 카드 만료 월 입력칸
    EXPIRY_YEAR = (By.CSS_SELECTOR, "[data-qa='expiry-year']")  # 카드 만료 연도 입력칸
    PAY_CONFIRM_BTN = (By.CSS_SELECTOR, "[data-qa='pay-button']")  # 'Pay and Confirm Order' 최종 결제 확정 버튼
    ORDER_PLACED_MSG = (By.CSS_SELECTOR, "[data-qa='order-placed']")  # 주문이 정상 접수되었을 때 뜨는 완료 메시지 요소

    def __init__(self, driver: WebDriver, timeout: int = 10):  # HomePage(driver)로 객체를 만들 때 자동 실행되는 초기화 함수; 기본 최대 대기시간은 10초
        self.driver = driver  # 밖에서 받은 브라우저 조종기(driver)를 이 객체의 속성(self.driver)으로 저장
        self.wait = WebDriverWait(driver, timeout)  # 최대 timeout(10)초 동안 원하는 조건이 될 때까지 기다려주는 대기 객체 생성

    # --- 공통 대기/조작 헬퍼 ---
    # 메서드 이름 앞의 밑줄(_)은 "이 클래스 내부에서 쓰려고 만든 보조 함수"라는 파이썬의 약속(관례)
    def _open(self, path: str = "/") -> None:  # path를 받되 안 넘기면 기본값 "/"; -> None은 돌려주는 값(return)이 없다는 뜻
        self.driver.get(f"{self.BASE_URL}{path}")  # f-string으로 기본 주소와 path를 이어 붙여 브라우저로 해당 URL 접속

    def _wait_visible(self, locator):  # locator 요소가 화면에 보일 때까지 최대 10초 기다렸다가 그 요소를 돌려줌
        return self.wait.until(EC.visibility_of_element_located(locator))

    def _wait_clickable(self, locator):  # locator 요소가 보이고 활성화되어 클릭 가능한 상태가 될 때까지 기다렸다가 돌려줌
        return self.wait.until(EC.element_to_be_clickable(locator))

    def _scroll_to_element(self, element) -> None:  # 웹 요소를 화면 중앙 근처로 스크롤해 보이게 만드는 함수
        self.driver.execute_script(  # 파이썬에서 브라우저 안의 자바스크립트(JS) 코드를 직접 실행
            "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",  # 요소를 화면 세로 중앙(center)에 맞추는 JS 명령
            element,  # 위 JS 코드의 arguments[0] 자리에 전달할 웹 요소
        )

    def _click(self, locator) -> None:  # 기다리기 → 스크롤 → 클릭을 한 번에 처리하는 안전 클릭 함수
        el = self._wait_clickable(locator)  # 클릭 가능해질 때까지 기다린 뒤 요소(el)를 변수에 담음
        self._scroll_to_element(el)  # 요소가 화면 중앙에 오도록 스크롤
        try:  # 아래 코드를 먼저 시도해 봄
            el.click()  # 일반적인 마우스 클릭 실행
        except ElementClickInterceptedException:  # 배너나 고정 메뉴 등이 클릭을 가로막아 이 에러가 나면 아래 코드로 넘어감
            self.driver.execute_script("arguments[0].click();", el)  # 일반 클릭이 막힐 때 JS로 직접 클릭을 강제 실행(우회 처리)

    def _type_text(self, locator, text: str) -> None:  # 입력칸에 기존 값을 지우고 새 글자(text)를 입력하는 함수
        el = self._wait_visible(locator)  # 입력칸이 화면에 보일 때까지 대기
        self._scroll_to_element(el)  # 입력칸이 보이도록 스크롤
        el.clear()  # 입력칸에 이미 들어 있는 글자를 먼저 비움
        el.send_keys(text)  # 키보드로 치듯이 text 문자열을 입력

    def _select_by_text(self, locator, visible_text: str) -> None:  # <select> 드롭다운에서 보이는 글자(visible_text)로 항목을 고르는 함수
        el = self._wait_visible(locator)  # 드롭다운 요소가 보일 때까지 대기
        self._scroll_to_element(el)  # 드롭다운 위치로 스크롤
        Select(el).select_by_visible_text(visible_text)  # Select 객체로 감싼 뒤 화면에 보이는 텍스트(예: "Canada")로 선택

    def _get_text(self, locator) -> str:  # 요소 안의 글자를 읽어 앞뒤 공백(.strip())을 없앤 문자열(str)로 돌려줌
        return self._wait_visible(locator).text.strip()

    def _is_visible(self, locator, timeout: int = 3) -> bool:  # 짧은 시간(기본 3초) 안에 요소가 보이는지 True/False로만 알려주는 함수
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))  # timeout초 안에 보이면 통과
            return True  # 보이면 True 반환
        except TimeoutException:  # timeout초가 지나도 안 보여서 타임아웃 에러가 발생하면
            return False  # 테스트를 멈추지 않고 False 반환

    # --- 메인 화면 동작 ---
    @allure.step("메인 페이지 로드")  # Allure 리포트에 '메인 페이지 로드'라는 실행 단계로 기록
    def load(self) -> "HomePage":  # 따옴표로 감싼 "HomePage"는 아직 클래스 정의가 끝나기 전이라 쓰는 자기 타입 힌트
        self._open("/")  # 메인 페이지("/")로 이동
        self._wait_visible(self.FIRST_PRODUCT_CARD)  # 첫 번째 상품 카드가 보일 때까지 기다려 페이지 로딩 완료 확인
        return self  # 자기 자신(HomePage 인스턴스)을 반환

    @allure.step("메인 화면 첫 번째 상품명 조회")  # Allure 리포트에 상품명 조회 단계 기록
    def get_first_product_name(self) -> str:  # 첫 번째 상품 이름을 문자열로 돌려주는 메서드
        name = self._get_text(self.FIRST_PRODUCT_NAME)  # 첫 번째 상품명 텍스트를 가져와 name 변수에 저장
        allure.attach(name, name="First Product Name", attachment_type=allure.attachment_type.TEXT)  # 조회한 상품명을 Allure 리포트 첨부 텍스트로 남김
        return name  # 테스트 코드에서 장바구니와 비교할 수 있도록 상품명을 반환

    @allure.step("메인 화면 첫 번째 상품 장바구니 담기")  # Allure 리포트에 장바구니 담기 단계 기록
    def add_first_product_to_cart(self) -> None:  # 첫 번째 상품에 마우스를 올리고 'Add to cart'를 누르는 메서드
        card = self._wait_visible(self.FIRST_PRODUCT_CARD)  # 첫 번째 상품 카드 요소를 찾고 보일 때까지 기다림
        self._scroll_to_element(card)  # 상품 카드가 화면 중앙에 오도록 스크롤
        ActionChains(self.driver).move_to_element(card).perform()  # 카드 위로 마우스 커서를 이동(move_to_element)하고 실제 실행(.perform())

        if self._is_visible(self.FIRST_PRODUCT_OVERLAY_ADD_BTN, timeout=2):  # 마우스 오버 시 나타나는 오버레이 버튼이 2초 안에 보이면
            self._click(self.FIRST_PRODUCT_OVERLAY_ADD_BTN)  # 오버레이 'Add to cart' 버튼을 클릭
        else:  # 오버레이 버튼이 보이지 않는 상태라면
            self._click(self.FIRST_PRODUCT_ADD_BTN)  # 기본 'Add to cart' 버튼을 클릭

        self._wait_clickable(self.MODAL_VIEW_CART_LINK)  # 장바구니 담기 후 뜨는 모달의 'View Cart' 링크가 클릭 가능해질 때까지 대기

    @allure.step("장바구니 추가 모달에서 'View Cart' 클릭하여 장바구니 이동")  # Allure 리포트 단계 기록
    def go_to_cart_from_modal(self) -> None:  # 모달 팝업에서 장바구니 화면으로 이동
        self._click(self.MODAL_VIEW_CART_LINK)  # 'View Cart' 링크 클릭

    @allure.step("회원가입/로그인 페이지로 이동")  # Allure 리포트 단계 기록
    def go_to_login(self) -> None:  # 상단 메뉴에서 로그인/회원가입 페이지로 이동
        self._click(self.HEADER_SIGNUP_LOGIN)  # 'Signup / Login' 링크 클릭

    # --- 회원가입 동작 ---
    @allure.step("임시 테스트 계정 가입: {email}")  # 리포트 단계 제목에 실제 email 값이 자동으로 채워져 표시됨
    def register_quick_user(self, name: str, email: str, password: str = "TestPass123!") -> None:  # 매번 새 테스트 계정을 빠르게 가입시키는 메서드
        self._type_text(self.SIGNUP_NAME, name)  # 회원가입 시작 폼에 사용자 이름 입력
        self._type_text(self.SIGNUP_EMAIL, email)  # 회원가입 시작 폼에 이메일 입력
        self._click(self.SIGNUP_BTN)  # 'Signup' 버튼 클릭해 상세 정보 입력 화면으로 이동

        self._type_text(self.PASSWORD, password)  # 비밀번호 입력
        self._type_text(self.FIRST_NAME, "QA")  # First name 입력
        self._type_text(self.LAST_NAME, "Tester")  # Last name 입력
        self._type_text(self.ADDRESS, "123 Test Street")  # 주소 입력
        self._select_by_text(self.COUNTRY, "Canada")  # 국가 드롭다운에서 "Canada" 선택
        self._type_text(self.STATE, "Ontario")  # 주/도 입력
        self._type_text(self.CITY, "Toronto")  # 도시 입력
        self._type_text(self.ZIPCODE, "M5V2T6")  # 우편번호 입력
        self._type_text(self.MOBILE, "01012345678")  # 휴대폰 번호 입력
        self._click(self.CREATE_ACCOUNT_BTN)  # 'Create Account' 버튼 클릭

        assert "ACCOUNT CREATED!" in self._get_text(self.ACCOUNT_CREATED_MSG).upper()  # 계정 생성 완료 문구가 대문자로 변환했을 때 포함되는지 확인(아니면 실패)
        self._click(self.CONTINUE_BTN)  # 'Continue' 버튼을 눌러 로그인 완료 상태로 진입

    # --- 장바구니 및 결제 동작 ---
    @allure.step("장바구니 내 상품 목록 조회")  # Allure 리포트 단계 기록
    def get_cart_item_names(self) -> list[str]:  # 장바구니에 담긴 상품명들을 문자열 리스트(list[str])로 반환
        self._wait_visible(self.CART_ITEMS_NAME)  # 장바구니 상품명 요소가 보일 때까지 대기
        items = [el.text.strip() for el in self.driver.find_elements(*self.CART_ITEMS_NAME)]  # 모든 상품 요소를 찾아 텍스트와 공백 제거 후 리스트로 만듦(*는 튜플 풀기)
        allure.attach("\n".join(items), name="Cart Items", attachment_type=allure.attachment_type.TEXT)  # 장바구니 상품 목록을 줄바꿈(\n)으로 이어 Allure 첨부파일로 남김
        return items  # 상품명 리스트 반환

    @allure.step("장바구니에서 'Proceed To Checkout' 진행")  # Allure 리포트 단계 기록
    def proceed_to_checkout(self) -> None:  # 주문서 확인 페이지로 이동
        self._click(self.PROCEED_TO_CHECKOUT)  # 'Proceed To Checkout' 버튼 클릭

    @allure.step("주문 코멘트 입력 및 'Place Order' 클릭")  # Allure 리포트 단계 기록
    def place_order(self, comment: str = "Automated E2E order") -> None:  # 코멘트 입력 후 결제 화면으로 이동
        self._type_text(self.COMMENT_TEXTAREA, comment)  # 주문 코멘트 입력란에 안내 문구 입력
        self._click(self.PLACE_ORDER_BTN)  # 'Place Order' 버튼 클릭

    @allure.step("카드 결제 정보 입력 및 결제 확정")  # Allure 리포트 단계 기록
    def pay_with_card(  # 카드 정보를 받아 입력하고 결제를 누르는 메서드
        self,
        name: str,
        card_number: str,
        cvc: str,
        month: str,
        year: str,
    ) -> None:
        self._type_text(self.NAME_ON_CARD, name)  # 카드 명의자 이름 입력
        self._type_text(self.CARD_NUMBER, card_number)  # 카드 번호 입력
        self._type_text(self.CVC, cvc)  # CVC 코드 입력
        self._type_text(self.EXPIRY_MONTH, month)  # 만료 월 입력
        self._type_text(self.EXPIRY_YEAR, year)  # 만료 연도 입력
        self._click(self.PAY_CONFIRM_BTN)  # 'Pay and Confirm Order' 버튼 클릭해 결제 확정

    @allure.step("결제 완료 메시지 조회")  # Allure 리포트 단계 기록
    def get_order_confirmation_text(self) -> str:  # 결제 완료 화면의 안내 문구를 읽어 반환
        return self._get_text(self.ORDER_PLACED_MSG)