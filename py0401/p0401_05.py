students = [
    [1,'홍길동',100,100,100,300,100.0,1],
    [2,'유관순',100,100,99,299,99.67,2],
    [3,'이순신',100,100,99,299,99.67,2]
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
        total = kor+eng+math   # 국어, 영어, 수학 합계를 구함
        avg = total/3
        rank = 0
        students.append([no,name,kor,eng,math,total,avg,rank])  #append = 입력받은 데이터를 students 리스트에 추가
        print(f"{name} 학생 성적이 입력되었습니다.")
        count += 1  # 인원수가 늘었기 때문에 학생번호 추가

    elif choice == 2:
        print("[ 학생성적출력 ]")
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))  # * 뒤의 리스트에 들어있는 정보값을 앞의 format에 맞춰 입력
        print("-"*60)
        for s in students:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}".format(*s))

    elif choice == 3:
        print("[ 학생성적수정 ]")
        name = input("수정하려는 학생 이름을 입력해 주세요.>> ")
        temp = 0
        for i,s in enumerate(students):  # enumerate - index 넘버를 가져옴. 데이터를 통으로 가져와야 할 때 써야 함
            if name in s:
                temp = 1
                print(f"{name} 학생이 목록에 있습니다.")
                print("[ 수정하려는 과목 선택 ]")
                print("1. 국어")
                print("2. 영어")
                print("3. 수학")
                print("0. 취소")
                choice = int(input("어떤 과목의 성적을 수정하시겠습니까?>> "))
                print("-"*30)
                if choice == 1:
                    print("[ 국어 성적 수정 ]")
                    print(f"기존 국어 점수 : {s[2]}")
                    s[2] = int(input("수정 국어 점수 : "))
                    s[5] = s[2]+s[3]+s[4]
                    s[6] = s[5]/3
                    print(f"{name} 학생 국어 성적이 수정되었습니다.")
                if choice == 2:
                    print("[ 영어 성적 수정 ]")
                    print(f"기존 영어 점수 : {s[3]}")
                    s[3] = int(input("수정 영어 점수 : "))
                    s[5] = s[2]+s[3]+s[4]
                    s[6] = s[5]/3
                    print(f"{name} 학생 영어 성적이 수정되었습니다.")
                if choice == 3:
                    print(f"기존 수학 점수 : {s[4]}")
                    s[4] = int(input("수정 수학 점수 : "))
                    s[5] = s[2]+s[3]+s[4]
                    s[6] = s[5]/3
                    print(f"{name} 학생 수학 성적이 수정되었습니다.")
        if temp == 0:
            print(f"{name} 학생의 이름이 목록에 없습니다. 다시 입력하세요.")
            
    elif choice == 4:
        print("[ 학생성적수정 ]")
        name = input("삭제할 학생의 이름을 입력하세요.>> ")
        temp = 0
        for i,s in enumerate(students):
            temp = 1
            if name in s:
                choice = int(input(f"{name} 학생의 성적을 삭제하시겠습니까?(0. 취소, 1. 삭제)>> "))
                if choice == 1:
                    print(f"{name} 학생 성적을 삭제했습니다.")
                    del students[i]
                elif choice == 0:
                    print(f"{name} 학생 성적 삭제를 취소했습니다.")
                break
        if temp == 0:
            print(f"{name} 학생 이름을 찾지 못했습니다. 다시 입력하세요.")          
    elif choice == 0:
        break