from sModule import *

# Students 객체 선언
#--------------------------
students = Students()
title = ["번호","이름","국어","영어","수학","합계","평균","등수"]


#--------------------------
# 타이틀
#--------------------------
def tmenu_print():
    print("-"*30)
    print("[ 학생성적프로그램 ]")
    print("-"*30)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 등수처리")
    print("0. 프로그램 종료")
    choice = 0
    try:
        choice = int(input("원하는 번호를 입력하세요.>> "))
    except Exception as e: print(e)  # 오류 원인 인쇄
    return choice


# 학생성적입력
def stu_input():
    print("[ 학생성적입력 ]")
    print("-"*30)
    name = input(f"{Student.count}번 학생 이름을 입력하세요.>> ")
    score = [0]*3
    for i in range(len(score)):
        score[i] = int(input(f"{title[i+2]} 점수를 입력하세요.>> "))
    students.add(Student(name,*score))
    print(f"{name} 학생 성적이 입력되었습니다.")
    
    
# 학생성적입력
def stu_output():
    print("[ 학생성적출력 ]")
    print("-"*60)
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
    print("-"*60)
    for s in students.students:
        print(f"{s.no}\t{s.name}\t{s.kor}\t{s.eng}\t{s.math}\t{s.total}\t{s.avg:.2f}\t{s.rank}")
        
# 학생성적수정
def stu_fix():
    print("[ 학생성적수정 ]")
    name = input("수정할 학생 이름을 입력하세요.>> ")
    temp = 0
    if name in students.students:
        temp = 1
        print(f"{name} 학생을 목록에서 찾았습니다.")
        print("[ 수정 과목 선택 ]")
        print("-"*30)
        print("1. 국어")
        print("2. 영어")
        print("3. 수학")
        print("-"*30)
        try: choice = int(input("수정할 과목의 번호를 입력하세요.>> "))
        except Exception as e:
            print(e)
        if choice == 1:
            pass
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        
    if temp == 0: print(f"{name} 학생을 목록에서 찾지 못했습니다. 다시 입력하세요!")

# 등수처리