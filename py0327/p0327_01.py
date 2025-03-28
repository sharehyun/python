# 파이썬 변수타입
# 1. bool - True / False 
# 2. 숫자 : int(정수), float(실수)
# 3. str : 문자열

# 변수선언
# 변수 = 10
# a = 20
# num = 30

# # print()
# print("안녕")
# print("안녕", a)
# print("입력된 숫자 : %d" % (a))
# print("입력된 숫자 : {}".format(a))
# print(f"입력된 숫자 : {a}")

# 입력 - input => 타입 : str타입
# 입력된 값은 str타입이기 때문에 형변환을 해줘야 함.
# num1 = int( input("숫자를 입력하세요.>> ") ) # 입력된 값을 int타입으로 변경
# num2 = int( input("숫자를 입력하세요.>> ") )
# print("입력된 숫자 : {}, {} / 합계 : {}".format(num1,num2,num1+num2))

# 학생성적 프로그램
# 이름, 국어, 영어, 수학 입력받아 함계, 평균 출력
print("-"*50)
print("                학생성적프로그램")
print("-"*50)
name = input("이름을 입력하세요.>> ")
kor = int(input("국어점수를 입력하세요.>> "))
eng = int(input("영어점수를 입력하세요.>> "))
math = int(input("수학점수를 입력하세요.>> "))

total = kor+eng+math
avg = total/3

print("\n이름\t국어\t영어\t수학\t합계\t평균")
print("-"*50)
print("{}\t{}\t{}\t{}\t{}\t{:.2f}".format(name,kor,eng,math,total,avg))
print("-"*50)

