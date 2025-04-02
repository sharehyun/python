# 데이터분석 / 웹스크래핑 / 디장고로 시스템 개발?? / 중간프로그램 / 자바 / 스프링 / 프로젝트

students = [
    [1,'홍길동',100,100,100,300,100.0,1],
    [2,'유관순',100,100,99,299,99.67,2],
    [3,'이순신',100,100,99,299,99.67,3]
] 

# students = list() # 다차원리스트
count = 4     # 학생번호를 생성
title = ['번호','이름','국어','영어','수학','합계','평균','등수']

# 무한반복
while True:
    # 화면출력
    print("-"*30)
    print(" "*5,end="")
    print("[ 학생성적프로그램 ]")
    print("-"*30)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 학생성적삭제")
    print("5. 학생성적정렬")
    print("6. 학생성적검색")
    print("7. 등수처리")
    print("0. 프로그램 종료")
    print("-"*30)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    
    if choice == 1:
        no = count
        print("[ 학생성적입력 ]")
        name = input(f"{no}번 학생 이름을 입력하세요.>> ")
        kor = int(input("국어 점수를 입력하세요.>> "))
        eng = int(input("영어 점수를 입력하세요.>> "))
        math = int(input("수학 점수를 입력하세요.>> "))
        total = kor+eng+math
        avg = total/3
        rank = 0
        
        students.append([no,name,kor,eng,math,total,avg,rank])
        count+=1
        
        print(f"{name} 학생성적이 등록되었습니다.")
        print()
    elif choice == 2:
        print("[ 학생성적출력 ]")
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print("-"*60)
        for s in students:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*s))
        print()
    
    elif choice == 3:
        print("[ 학생성적수정 ]")
        name = input("수정할 학생 이름을 입력하세요.")
        for i,s in enumerate(students):   #
            if name in s:
                print(f"{name} 학생 이름이 목록에 있습니다.")
                choice = int(input(f"{name} 학생 성적을 삭제하시겠습니까?(0. 취소, 1. 삭제)>> "))
                if choice == 1:
                    del s[i]