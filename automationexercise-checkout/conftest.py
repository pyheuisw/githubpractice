from pathlib import Path          # 파일/폴더 경로를 OS 차이 없이 다루기 위한 표준 모듈
import allure                     # Allure 리포트에 스텝/첨부파일을 기록하는 라이브러리
import pytest                     # 테스트 실행 프레임워크
from selenium import webdriver    # 실제 브라우저(Chrome 등)를 조종하는 Selenium 도구
from selenium.webdriver.chrome.options import Options  # 크롬 실행 옵션 설정 클래스


@pytest.fixture                   # 아래 함수를 pytest의 '공용 준비물(fixture)'로 등록
def driver(request):              # 테스트 함수가 driver를 인자로 받으면 이 함수가 먼저 실행됨; request는 현재 테스트 정보 객체
    options = Options()           # 빈 크롬 설정 객체 생성
    # options.add_argument("--headless=new")  # 창을 띄우지 않고 백그라운드에서 실행할 때 쓰는 옵션(현재는 주석 처리)
    options.add_argument("--window-size=1440,900")  # 화면 크기를 고정해 버튼이 가려지거나 레이아웃이 깨지는 변수 방지
    options.add_argument("--disable-gpu")     # 그래픽 가속 비활성화(가상환경/CI 안정성 목적)
    options.add_argument("--no-sandbox")      # 리눅스 컨테이너 환경에서 크롬 실행 권한 오류 방지

    drv = webdriver.Chrome(options=options)   # 위 옵션으로 실제 크롬 브라우저 실행 및 제어 객체(drv) 생성
    drv.implicitly_wait(0)        # 암묵적 대기를 0으로 꺼둠(명시적 대기 WebDriverWait만 써서 대기 시간 예측 가능하게 함)
    yield drv                     # 여기서 잠시 멈추고 drv를 테스트 함수에 넘김; 테스트가 끝나면 아래 줄이 이어서 실행됨

    # 테스트 본문(call)이 실행된 결과(rep_call)가 존재하고, 그 결과가 '실패(failed)'였는지 확인
    if getattr(request.node, "rep_call", None) and request.node.rep_call.failed:
        screenshots_dir = Path("screenshots")        # screenshots 폴더 경로 객체 생성
        screenshots_dir.mkdir(exist_ok=True)         # 폴더가 없으면 만들고, 이미 있어도 에러를 내지 않음
        screenshot_path = screenshots_dir / f"{request.node.name}.png"  # f-string으로 '테스트이름.png' 경로 조합
        drv.save_screenshot(str(screenshot_path))    # 로컬 파일로도 스크린샷 저장

        allure.attach(                               # Allure 리포트에 실패 당시 화면 이미지 첨부
            drv.get_screenshot_as_png(),             # 현재 화면을 PNG 바이트 데이터로 캡처
            name="Failure Screenshot",               # 리포트에 보일 첨부파일 이름
            attachment_type=allure.attachment_type.PNG,  # 파일 형식이 PNG임을 지정
        )
        allure.attach(                               # 실패 당시 어느 URL에 있었는지 텍스트로 첨부
            drv.current_url,                         # 브라우저 주소창의 현재 URL 문자열
            name="Current URL on Failure",
            attachment_type=allure.attachment_type.TEXT,
        )
        allure.attach(                               # 실패 당시 HTML 구조(DOM) 전체를 첨부해 원인 분석에 활용
            drv.page_source,
            name="Page Source on Failure",
            attachment_type=allure.attachment_type.HTML,
        )

    drv.quit()                    # 테스트 성공/실패와 무관하게 마지막에 브라우저 창과 드라이버 프로세스 종료