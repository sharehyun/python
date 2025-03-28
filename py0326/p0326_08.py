# # 1. 두 숫자를 입력받아 합과 곱을 출력하시오.
# a = input("1. 숫자를 입력하시오 : ")
# b = input("2. 숫자를 입력하시오 : ")

# a = float(a)
# b = float(b)
# print(a+b)
# print(a*b)

# #a, b라는 변수에 입력받아, a,b를 출력하고 값을 교체해서 출력하시오

# a = input("3. 숫자를 입력하시오 : ")
# b = input("4. 숫자를 입력하시오 : ")

# print("두 수 출력 :",a,b)
# c = a
# a = b
# b = c

# print("교체된 두 수 출력 :",a,b)

# a = 100      # int타입
# st = "Hello" # str타입
# print("변수값 :",a)
# print("변수값 :"+a) # 에러 - 다른타입은 연산자를 사용할 수 없음. "" 안에 있는 건 str이기 때문
# # 쉼표는 다른타입도 사용 가능, 웬만해선 쉼표 사용
# print("변수값 :",st)
# print("변수값 :"+st)


a = 10
b = 5
print(a,"+",b,"=",a+b)

c = 100
d = 7
print(c,"*",d,"=",c*d)
print("%d * %d = %d" % (c,d,c*d))
print(c,"/",d,"=",c/d)
print("%d / %d = %07.2f" % (c,d,c/d))

