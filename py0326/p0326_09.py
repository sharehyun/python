# 이름 입력, 국어, 영어, 수학, 과학 입력받아 이름, 점수 합계, 평균 출력. 소수점 첫째자리까지 출력
# name = input("이름을 입력하시오 : ")   #여기부터 입력
# kor = int(input("국어 점수를 입력하시오 : "))
# eng = int(input("영어 점수를 입력하시오 : "))
# math = int(input("수학 점수를 입력하시오 : "))
# sci = int(input("과학 점수를 입력하시오 : " ))

# total = kor+eng+math+sci  #변수 - 점수 총합
# avg = total/4             #변수 - 점수 평균 

# print("이름 :",name)      #여기부터 출력
# print("국어 :",kor)
# print("영어 :",eng)
# print("수학 :",math)
# print("과학 :",sci)
# print("합계 :",total)
# print("평균 : %.1f" % avg)



# 프린트 시 \n : 엔터키, \t : tab키
print("안녕하세요.\n 반갑습니다.\t 저는 홍길동이라고 합니다.")

# format() 문자형태 함수
a = 10
b = 3
print("%d / %d = %.2f" % (a,b,a/b))
str_print = "{} / {} = {:.2f}".format(a,b,a/b)
print(str_print)
# f함수 = format()
str_print2 = f"{a} / {b} = {(a/b):.2f}"
print(str_print2)
