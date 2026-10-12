# 과제1 

# def print_star():
#     print("*" * 24)


# def print_plus():
#     print("+" * 26)


# def print_hash():
#     print("#" * 24)


# print_hash()
# print_star()
# print_plus()
# print_plus()
# print_star()
# print_hash()



# 과제2

# def print_hash(n):
#     for i in range(n):
#         print(i, "#" * 20)


# print_hash(6)


# 과제3

# def print_sub(a, b):
#     result = a - b
#     print(f"{a}과 {b}의 차는 {result}입니다.")


# print_sub(10, 20)


# 과제4

# def print_area(width, height):
#     area = width * height / 2
#     print(f"밑변 {width}, 높이 {height}인 삼각형의 면적은 : {area:g}")


# print_area(10, 20)




# 과제5
# def circle_area_circum(radius):
#     pi = 3.14
#     area = pi * radius ** 2
#     circum = 2 * pi * radius

#     return area, circum


# radius = 10
# area, circum = circle_area_circum(radius)

# print(f"반지름 {radius}인 원의 면적은 {area:.1f}, 원의 둘레는 {circum:.1f}")



# 과제6

# def muliples(n, m):
#     result = []

#     for i in range(1, m + 1):
#         result.append(n * i)

#     return tuple(result)


# r1, r2, r3, r4 = muliples(3, 4)
# print(r1, r2, r3, r4)

# r1, r2, r3, r4, r5 = muliples(2, 5)
# print(r1, r2, r3, r4, r5)


# 과제7

# def sum_nums(*args):
#     print(f"{len(args)} 개의 인자 {args}")

#     total = sum(args)
#     average = total / len(args)

#     print(f"합계 : {total} , 평균 : {average:.1f}")


# sum_nums(10, 20, 30)
# sum_nums(10, 20, 30, 40, 50)



def cal_area(width, height):
    area = width * height / 2
    return area


width = float(input("밑변을 입력하시오: "))
height = float(input("높이를 입력하시오: "))

result = cal_area(width, height)

print(f"삼각형의 면적 : {result}")