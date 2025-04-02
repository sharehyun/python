# 두 수를 입력받아 사칙연산(+,-,*,/) 출력하시오.
def cal(x,y):
    print("더하기 :",x+y)
    print("빼기 : ",x-y)
    print("곱하기 : ",x*y)
    print("나누기 : ",x/y)
    return x+y

num1 = int(input("첫번째 숫자를 입력하세요.>> "))
num2 = int(input("두번째 숫자를 입력하세요.>> "))
result1 = cal(num1,num2) # 함수호출

num3 = int(input("첫번째 숫자를 입력하세요.>> "))
num4 = int(input("두번째 숫자를 입력하세요.>> "))
result2 = cal(num3,num4)

num5 = int(input("첫번째 숫자를 입력하세요.>> "))
num6 = int(input("두번째 숫자를 입력하세요.>> "))
result3 = cal(num5,num6)

# 결과중에 합계를 모두 더해서 총 합계를 구하시오.
print("총합계 :",result1+result2+result3)


# def add(x,y):
#     print("x =",x)
#     print("y =",y)
#     print("x + y =",x+y)

# # 특정값
# a = 10
# b = 20
# c = 30
# d = 40

# add(a,b)
#     # print("x =",x)
#     # print("y =",y)
#     # print("x + y =",x+y)
# add(a,c)
#     # print("x =",x)
#     # print("y =",y)
#     # print("x + y =",x+y)
# add(a,d)
#     # print("x =",x)
#     # print("y =",y)
#     # print("x + y =",x+y)
# add(c,d)
#     # print("x =",x)
#     # print("y =",y)
#     # print("x + y =",x+y)



# 함수선언 - 변수는 명사, 함수는 동사를 많이 씀
# def add():
#     print("안녕하세요.")
#     print("안녕하세요.")
#     print("안녕하세요.")

# print("누군가 오고 있어요.")
# print("인사")
# add() # 함수호출

# # print()  # 변수뒤에 ()가 있으면 함수
# # 함수선언
# def cal(x,y):   # 함수 정의
#     result = x+y
#     print(result)
#     result2 = x-y
#     print(result2)
#     result3 = x*y
#     print(result3)
#     result4 = x/y
#     print(result4)

# a,b = 10,20
# cal(a,b) # 함수호출

# c,d = 100,200
# cal(c,d)

# e,f = 50,100
# cal(e,f)