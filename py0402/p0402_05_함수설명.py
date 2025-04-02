def cal(*a,b=10):  # 가변매개변수, 키워드 매개변수 함께 사용 - 매개변수 키워드
    result = b
    for i in a:
        result += i
    return result

print(cal(1,2,b=100))


# # 키워드 매개변수 - 키워드 변수는 무조건 마지막에 있어야 함.
# def cal(a,b=10):
#     return a+b

# print(cal(1))


# # print()함수는 매개변수가 가변매개변수임.
# print(1,2,3,4,5)
# print(1,2)

# # 가변매개변수 사용
# def cal(*num):    # 전개연산자
#     result = 0
#     for n in num:
#         result+=n
#     return result

# print("2개 합계 :",cal(1,2))
# print("3개 합계 :",cal(10,20,30))
# print("4개 합계 :",cal(20,40,60,80))

# def cal(n1,n2):
#     return n1+n2

# def cal2(n1,n2,n3):
#     return n1+n2+n3

# def cal3(n1,n2,n3,n4):
#     return n1+n2+n3+n4

# n1 = 10
# n2 = 20
# n3 = 30
# n4 = 40

# result = cal(n1+n2)
# print(result)
# result2 = cal2(n1,n2,n3)
# print(result2)


# # global 변수 : 전역변수
# def func1():
#     # a = 20    # 지역변수이기에 함수를 벗어나면 사라짐.
#     global a    # 전역변수 호출
#     a = 20

# a = 10
# print("a :",a)  # a = 10
# func1()
# print("a :",a)  # a = 10

# def cal(ss):
#     ss['kor'] = int(input("수정할 국어점수를 입력하세요.>> "))
#     ss['total'] = ss['kor']+ss['eng']+ss['math']
#     ss['avg'] = ss['total']/3

# print("[ 학생성적 수정 ]")
# s = {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1}
# # 국어점수변경 함수호출
# cal(s)  # 변경된 국어점수가 변수에 입력
# print("수정된 국어점수 :",s['kor'])


# 매개변수로 일반변수 전달형태 - 리턴으로 값을 돌려줘서 입력시켜야 함 
# 국어점수변경 함수선언
# def cal(kor):
#     kor = int(input("수정할 국어점수를 입력하세요.>> "))
#     return kor

# print("[ 학생성적 수정 ]")
# kor = 100
# eng = 100
# math = 100
# # 국어점수변경 함수호출
# kor = cal(kor)  # 변경된 국어점수가 변수에 입력
# print("수정된 국어점수 :",kor)


# def cal(a_list):
#     a_list[0] = 100
#     a_list[1] = 200

# a_list = [0,0]   # 리스트타입 변수 : 주소값
# a_list[0] = 10
# a_list[1] = 20
# print("함수호출 전 a_list :",a_list[0],a_list[1]) # 10 20

# cal(a_list)  # 함수호출   b_list = a_list  주소가 복사됨. 얕은 복사
# print("함수호출 후 a_list :",a_list[0],a_list[1])  # 100 200


# 지역변수 - 함수 내에 선언되어 있는 변수, 함수 내에서만 활용
# 전역변수 - 함수 외에 선언되어 있는 변수, 프로그램 전체에서 활용

# # 함수선언
# def cal(a,b):
#     a = 100  # 지역변수 - 함수내 일반변수는 함수를 벗어나면 사라짐. (bool, int, float, str)
#     b = 200  # 선언이 영향을 미치려면 return으로 값을 넘겨줘서 다시 넣어야 함
# #-------------------------
# # 함수 밖
# a = 10  # 전역변수
# b = 20
# print("함수호출전 a,b :",a,b) # a=10, b=20

# # 함수호출
# cal(a,b)
# print("함수호출후 a,b :",a,b) # a=10, b=20


# # 이름, 국어, 영어, 수학 점수를 입력받아 합계, 평균을 출력하시오.
# students = [
#     {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
#     {"no":2,"name":"유관순","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
#     {"no":3,"name":"이순신","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
# ] 

# title = ['번호','이름','국어','영어','수학','합계','평균','등수']

# def stu_print():
#     print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
#     for s in students:
#         print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")

# print("1. 학생성적입력")
# print("2. 학생성적출력")
# choice = int(input("원하는 번호를 입력하세요.>> "))
# if choice == 2: stu_print()

# # 함수선언
# def cal(kor,eng,math):
#     # total = kor+eng+math
#     # avg = kor+eng+math/3
#     return kor+eng+math,(kor+eng+math)/3
    

# no = 1
# name = input("이름을 입력하시오.>> ")
# kor = int(input("국어점수를 입력하세요.>> "))
# eng = int(input("영어점수를 입력하세요.>> "))
# math = int(input("수학점수를 입력하세요.>> "))
# total,avg = cal(kor,eng,math)

# print(f"합계 : {total} / 평균 : {avg:.2f}")




# 직사각형 넓이와 둘레를 구하는 프로그램을 구현하시오.
# 넓이 = 가로 * 세로, 둘레 = (가로+세로)*2

# 가로, 세로길이를 입력받아 넓이와 둘레를 구하시오.
# 함수를 사용할 것

# def cal(x,y):
#     result1 = x*y
#     result2 = (x+y)*2
#     return result1,result2

# # 가로, 세로 입력
# num1 = int(input("가로 길이를 입력하세요.>> "))
# num2 = int(input("세로 길이를 입력하세요.>> "))
# result1,result2 = cal(num1,num2)
# print(f"넓이 : {result1} / 둘레 : {result2}")


# # cal 함수선언하시오.
# def cal(n_list):
#     sum = 0
#     for n in n_list:
#         if n%2==0: sum += n
#     return sum

# # 5개 입력받아 짝수만 모두 더한 값을 출력하시오.
# n_list = [0]*5
# for i in range(5):
#     n_list[i] = int(input("숫자를 입력>> "))
# result = cal(n_list)
# print("짝수의 합 :",sum)

# def aff(a,b):   #a,b는 매개변수, return을 쓰면 왔던 위치로 결과값을 보냄
#   return a+b  

# 함수를 사용해서 두 수를 입력받아
# 10~20 입력받으면 10+11+12+13.......20 출력하시오.

# def add(n1,n2):
#     sum = 0
#     if n1>n2: n1,n2 = n2,n1
#     for i in range(n1,n2+1):
#         sum += i
#     print(f"합계 : {sum}")

# n1 = int(input("숫자를 입력하시오.>> "))
# n2 = int(input("숫자를 입력하시오.>> "))

# add(n1,n2)


# 함수사용
# - 1. 중복코드가 있을때.
# - 2. 소스가 너무 복잡할때
# - 먼저 프로그램을 모두 구현해놓고, 중복되고 있는지 확인 후 함수를 사용


# num1,num2.num3 값을 입력받아 합계, 평균을 구하시오.
# # 함수선언
# def add(kor,eng,math):
#     return kor+eng+math


# kor = int(input("점수를 입력하세요.>> "))
# eng = int(input("점수를 입력하세요.>> "))
# math = int(input("점수를 입력하세요.>> "))

# total = kor + eng + math
# avg = total/3

# print(kor,eng,math,total,avg)

