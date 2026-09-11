import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




def makeorder():

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    
    
    #### 상품상세 ####


    try :
        URL1 = 'https://www-ecp-stgrenew.amoremall.com/kr/ko/product/detail?onlineProdSn=12438&onlineProdCode=111610000002'

        driver.get(URL1)
        driver.maximize_window()

        button1_1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/section/section[1]/section/div/div/div[1]/div[1]/div[2]/div[3]/div/button[3]')))
        button1_1.click()

        button1_2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/section/section[1]/section/div/div/div[1]/div[1]/div[2]/div[3]/div/section[2]/div[2]/div/div/div[1]/div[1]/div/ul/li[2]/button')))
        button1_2.click()

        button1_3 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "장바구니")]')))
        button1_3.click()


        time.sleep(3)


        URL2 = 'https://www-ecp-stgrenew.amoremall.com/kr/ko/product/detail?onlineProdSn=19690&onlineProdCode=999981000030'
        driver.get(URL2)

        button2_1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/section/section[1]/section/div/div/div[1]/div[1]/div[2]/div[2]/div/button[2]')))
        button2_1.click()

        button2_2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/section/section[1]/section/div/div/div[1]/div[1]/div[2]/div[2]/div/section[2]/div[2]/div/div/div[1]/div[1]/div/ul/li[2]/button')))
        button2_2.click()

        button2_3 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "장바구니")]')))
        button2_3.click()


        cart_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/section/header/div/div[2]/a[2]/i')))
        cart_button.click()



        #### 장바구니 ####



        cart_order_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/section/section/div/div[2]/button')))
        cart_order_button.click()


        loginpopup_login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/section[2]/div[2]/div/div/div[2]/div[1]/div[1]/a[1]')))
        loginpopup_login_button.click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="loginid"]').send_keys("test1991")
        driver.find_element(By.XPATH, '//*[@id="loginpassword"]').send_keys("qwer1234")

        loginpage_login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="dologin"]')))
        loginpage_login_button.click()



        #### 주문서 ####



        orderpage_pay_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/section/section/section/section[2]/div[2]/div[3]/div[2]/button')))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", orderpage_pay_button)
        time.sleep(2)
        orderpage_pay_button.click()


        orderpage_agree_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="personalInfoAgreement"]')))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", orderpage_agree_button )
        time.sleep(2)
        orderpage_agree_button.click()


        orderpage_order_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/section/section/div/div[2]/button')))
        orderpage_order_button.click()


    finally :
        time.sleep(5)
        driver.quit()



if __name__ == "__main__":
    for i in range(1, 6):
        print(f"\n===== [ {i}번째 주문 시도 시작 ] =====")
        try:
            makeorder()
            print(f"===== [ {i}번째 주문 완료 ] =====")

        except Exception as e:
            print(f"❌ {i}번째 시도 중 에러 발생: {e}")
        
        # 각 작업 사이의 여유 대기 시간 (필요 시 조절)
        time.sleep(3)