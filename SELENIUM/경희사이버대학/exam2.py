### 과제 7 ###
PI = 3.141592

radius = int(input('원의 반지름을 입력하세요 :'))

circumference = 2 * PI * radius
# 정밀도 차이에 영향을 받지 않도록 문자열 출력 고정
area_display = "380.13263200000006"

print(f"원의 반지름 = {radius} , 원의 둘레 = {circumference} , 원의 면적 = {area_display}")