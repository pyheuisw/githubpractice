# 과제1
# for i in range(5):
#     print(i)


# 과제2
# numbers = list(range(1, 101))
# print(numbers)



# 과제3
# # 1) 1 이상 100 이하의 짝수 리스트
# even_list = list(range(2, 101, 2))
# print(even_list)

# # 2) 1 이상 100 이하의 홀수 리스트
# odd_list = list(range(1, 101, 2))
# print(odd_list)

# # 3) -100보다 크고 0보다 작은 음수 리스트 (-99부터 -1까지)
# negative_list = list(range(-99, 0))
# print(negative_list)


# 과제4
# # 1) 1에서 100까지 정수의 합
# total = 0
# for i in range(1, 101):
#     total += i
# print("1에서 100까지 정수의 합:", total)

# # 2) 1에서 100까지 짝수의 합
# even_total = 0
# for i in range(0, 101, 2):
#     even_total += i
# print("1에서 100까지 짝수의 합:", even_total)

# # 3) 1에서 100까지 홀수의 합
# odd_total = 0
# for i in range(1, 101, 2):
#     odd_total += i
# print("1에서 100까지 홀수의 합:", odd_total)







n = 7

for i in range(n):
    # 1) 공백 출력용 안쪽 루프 (n - 1 - i 개)
    for j in range(n - 1 - i):
        print(" ", end="")
    
    # 2) '#' 출력용 안쪽 루프 (1개)
    for k in range(1):
        print("#", end="")
        
    print()  # 줄바꿈
















# 과제6
# i = 1
# while i <= 5:
#     print(i)
#     i += 1


# 과제7
# total = 0
# i = 1
# while i <= 10:
#     total += i
#     i += 1
# print("합계:", total)


# 과제8
# while True:
#     num = int(input("숫자를 입력하세요: "))
#     if num == 0:
#         print("프로그램을 종료합니다.")
#         break
#     print("입력한 숫자:", num)