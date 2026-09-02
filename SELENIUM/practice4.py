import requests
from bs4 import BeautifulSoup

base_url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query="
keyword = input("검색어를 입력하시오 : ")
url = base_url + keyword


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

items = soup.select(".sds-comps-vertical-layout.sds-comps-full-layout.vlFp8ERAn58mSKma")
print(len(items))


for e,item in enumerate(items,1):
    element = item.select_one(".sds-comps-text-type-headline1").text
    print(f"{e}번째 뉴스 : {element}")


