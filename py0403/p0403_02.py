# import stu_func         #  모듈 사용
# import stu_func as stu  #  별칭사용
from stu_func import *    #  * = stu_print,stu_input,stu_output... stu_func에 있는 모든 것
# import random - 남이 만든 모듈(random)을 사용

students = [
    {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
    {"no":2,"name":"유관순","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
    {"no":3,"name":"이순신","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
]

count = 4
title = ['번호','이름','국어','영어','수학','합계','평균','등수']
choice = 0

while True:
    # 화면출력부분
    choice = stu_print()
    
    if choice == 1:  # 학생성적입력
        count = stu_input(count,students)

    elif choice == 2:  # 학생성적출력
        stu_output(title,students)

    elif choice == 3:  # 학생성적수정
        print("[ 학생성적수정 ]")
        name = input("수정하려고 하는 학생이름을 입력하세요.>> ")
        temp = 0       # 찾지 못했을 경우
        for s in students:
            if s['name'] == name:
                temp = 1
                print(f"{name} 학생이 목록에 있습니다. 성적을 수정합니다.")
                print("-"*30)
                print("[ 수정 과목 선택 ]")
                print("-"*30)
                print("1. 국어")
                print("2. 영어")
                print("3. 수학")
                print("-"*30)
                choice = int(input("원하는 번호를 입력하세요.>> "))
                sub_list = ['','kor','eng','math']
                if choice == 1:
                    stu_fix(s,sub_list,choice,title,name)
                
                elif choice == 2:
                    stu_fix(s,sub_list,choice,title,name)
                
                elif choice == 3:
                    stu_fix(s,sub_list,choice,title,name)

        if temp == 0:
            print(f"{name} 학생을 목록에서 찾지 못했습니다. 다시 입력하세요!!")
            print()
                

    elif choice == 4:  # 등수처리
        stu_rank(students)

    elif choice == 0:  # 프로그램 종료
        print("[ 프로그램 종료 ]")
        break