import time  # 현재 시각(유닉스 타임스탬프)을 구해 매번 겹치지 않는 테스트 계정 이름을 만들 때 쓰는 표준 모듈
import allure  # Allure 리포트에 분류 라벨(@allure.epic 등)과 검증 구간(with allure.step)을 남기기 위한 모듈
from pages.home_page import HomePage  # 방금 만든 pages/home_page.py 파일에서 HomePage 클래스를 불러옴


# 아래 4줄은 Allure 리포트에서 이 테스트를 어떤 메뉴/분류/중요도로 묶어 보여줄지 지정하는 데코레이터
@allure.epic("E-Commerce Storefront")  # 리포트 최상위 대분류(에픽): 전자상거래 스토어프런트
@allure.feature("Cart & Checkout")  # 중분류(기능): 장바구니 및 결제
@allure.story("첫 번째 상품 장바구니 담기 및 결제 완료")  # 소분류(사용자 스토리): 구체적인 시나리오 이름
@allure.severity(allure.severity_level.CRITICAL)  # 중요도 설정: 핵심 기능이므로 CRITICAL(치명적/중요)로 표시
def test_first_product_add_to_cart_and_checkout(driver):  # pytest가 'test_'로 시작하는 이름과 'driver' fixture를 인식해 실행하는 테스트 함수
    page = HomePage(driver)  # 브라우저 조종기(driver)를 넘겨 HomePage 객체(인스턴스)를 생성하고 page 변수에 담음

    unique_suffix = int(time.time())  # time.time()이 돌려주는 소수점 시각을 정수(int)로 바꿔 매번 달라지는 숫자 꼬리표 생성
    test_email = f"qa_{unique_suffix}@example.com"  # f-string으로 숫자를 끼워 넣어 중복 가입 에러를 피할 고유 이메일 주소 제작

    # --- 1단계: 회원가입으로 로그인 상태 만들기 ---
    page.load()  # 메인 페이지 접속 및 로딩 대기
    page.go_to_login()  # 상단 메뉴에서 회원가입/로그인 페이지로 이동
    page.register_quick_user(  # 임시 테스트 계정 가입 메서드 호출
        name=f"qa_user_{unique_suffix}",  # 매번 다른 사용자 이름 전달
        email=test_email,  # 위에서 만든 고유 이메일 전달(password는 기본값 "TestPass123!" 사용)
    )

    # --- 2단계: 메인 화면에서 첫 번째 상품 장바구니 담기 및 이동 ---
    page.load()  # 회원가입 완료 후 다시 메인 페이지로 돌아옴
    first_product_name = page.get_first_product_name()  # 메인 화면 첫 번째 상품 이름을 읽어 변수에 저장(나중에 장바구니와 비교하려고 보관)
    page.add_first_product_to_cart()  # 첫 번째 상품 카드에 마우스를 올리고 'Add to cart' 버튼 클릭
    page.go_to_cart_from_modal()  # 장바구니 담기 모달의 'View Cart'를 눌러 장바구니 화면으로 이동

    # --- 3단계: 장바구니 상품 담김 여부 검증 ---
    with allure.step("장바구니에 선택한 첫 번째 상품이 담겼는지 검증"):  # 이 블록 안의 실행/검증 결과를 Allure 리포트의 한 스텝으로 묶어 표시
        cart_items = page.get_cart_item_names()  # 현재 장바구니 화면에 보이는 상품명 목록(리스트)을 가져옴
        assert first_product_name in cart_items, (  # 아까 기억해 둔 상품명이 장바구니 목록 안에 있는지 검사; False면 테스트 실패 처리
            f"Expected '{first_product_name}' in cart, but got {cart_items}"  # 실패 시 원인 파악에 도움이 되도록 출력할 에러 메시지
        )

    # --- 4단계: Checkout 진행 및 카드 결제 ---
    page.proceed_to_checkout()  # 장바구니에서 'Proceed To Checkout' 버튼을 눌러 주문서 확인 화면으로 이동
    page.place_order()  # 주문 코멘트를 입력하고 'Place Order'를 눌러 결제 화면으로 이동
    page.pay_with_card(  # 테스트용 더미 카드 정보를 채워 넣고 결제를 확정
        name="QA Tester",  # 카드 명의자 이름
        card_number="4100000000001234",  # 테스트용 가상 카드 번호
        cvc="123",  # 테스트용 CVC 번호
        month="12",  # 만료 월
        year="2028",  # 만료 연도
    )

    # --- 5단계: 결제 완료 화면 검증 ---
    with allure.step("주문 완료 문구('ORDER PLACED!') 노출 여부 검증"):  # 최종 검증 단계를 Allure 리포트 스텝으로 기록
        confirmation_text = page.get_order_confirmation_text().upper()  # 결제 완료 문구를 가져와 .upper()로 모두 대문자로 변환
        assert "ORDER PLACED!" in confirmation_text  # 대문자로 바꾼 문구 안에 "ORDER PLACED!"가 포함되어 있으면 테스트 최종 통과