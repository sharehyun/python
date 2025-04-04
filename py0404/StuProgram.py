from StuFunc import *    #  * = stu_print,stu_input,stu_output... stu_func에 있는 모든 것
# import random  # 남이 만든 모듈(random)을 사용

students = []

##### 파일 불러오기
# stu.txt파일에서 데이터 읽어와 students = [] 데이터 입력
# 1,홍길동,100,100,100,300,100.0,
with open("py0404/stu.txt","r",encoding="utf8") as f:
    while True:                # 여러줄일때 반복문 적용
        line = f.readline()    # 1줄 읽어오기
        if not line: break     # 데이터 없을때 종료
        s = line.strip().split(",")  # 1줄 문자열을 ,(쉼표) 기준으로 분리
        students.append({
            "no":int(s[0]),"name":(s[1]),"kor":int(s[2]),"eng":int(s[3]),
            "math":int(s[4]),"total":int(s[5]),"avg":float(s[6]),"rank":int(s[7])
        })



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
    
    elif choice == 5:  # 학생성적정렬
        students2 = [*students]  # 복사
        print("[ 학생성적정렬 ]")
        print("1. 이름 순차정렬")
        print("2. 이름 역순정렬")
        print("3. 합계 순차정렬")
        print("4. 합계 역순정렬")
        print("5. 번호 순차정렬")
        print("6. 번호 역순정렬")
        print("0. 이전화면이동")
        print("-"*30)
        choice = int(input("원하는 번호를 입력하세요.>> "))
        if choice == 1:  # 이름순차정렬
            students2.sort(key=lambda x:x['name'])
        elif choice == 2:  # 이름역순정렬
            students2.sort(key=lambda x:x['name'],reverse=True)
        elif choice == 3:  # 합계순차정렬
            students2.sort(key=lambda x:x['total'])
        elif choice == 4:  # 합계역순정렬
            students2.sort(key=lambda x:x['total'],reverse=True)
        elif choice == 5:  # 번호순차정렬
            students2.sort(key=lambda x:x['no'])
        elif choice == 6:  # 번호역순정렬
            students2.sort(key=lambda x:x['no'],reverse=True)
        elif choice == 0:
            continue
        stu_output(title,students2)

    elif choice == 6:  # 학생성적삭제
        print("[ 학생성적삭제 ]")
        name = input("삭제하고자 하는 학생 이름을 입력하세요.>> ")
        temp = 0
        for i,s in enumerate(students):
            if name == s['name']:
                temp = 1
                print(f"{s['no']}번 {name} 학생을 찾았습니다.>> ")
                print(f"{name} 학생 성적을 삭제하시겠습니까?(*삭제시 복구불가)")
                answer = input("n-취소, y-삭제")
                if answer == 'y':
                    del students[i]
                    print(f"{name} 학생을 삭제했습니다.")
                    print()
                    break
        if temp == 0:
            print(f"{name} 학생이 목록에 없습니다. 다시 입력하세요.")
            print()

    elif choice == 7:  # 학생성적저장
        print("[ 학생성적저장 ]")
        with open("py0404/stu.txt","w",encoding="utf8") as f:
            for s in students:
                # 1,홍길동,100,100,100,300,100.0,1
                line = f"{s['no']},{s['name']},{s['kor']},{s['eng']},{s['math']},{s['total']},{s['avg']},{s['rank']}\n"
                f.write(line)
        print("파일이 저장되었습니다.")
        print()

    elif choice == 0:  # 프로그램 종료
        print("[ 프로그램 종료 ]")
        break