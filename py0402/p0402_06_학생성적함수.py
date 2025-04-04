### 파일 - 저장해서 불러오기
### DB에서 가져오기

### 전역변수 선언부분



### 함수 부분 ###
# 학생성적입력 함수
def stu_input(count):
    print("-"*30)
    print("[ 학생성적 입력 ]")
    print("-"*30)
    while True:
        no = count
        name = input(f"{no}번 학생 이름을 입력하세요.(0. 이전화면 이동)>> ")
        # 이전화면 이동 확인
        if name == "0": break # 학생성적입력에서 전체화면으로 이동
        score = [0]*3  # list생성
        score_cal(0,score) # 국어점수입력, 확인
        score_cal(1,score) # 영어점수입력, 확인
        score_cal(2,score) # 수학점수입력, 확인


        # no, name, kor, eng, math
        # 합계, 평균 구하기
        total = score[0]+score[1]+score[2]
        avg = total/3
        rank = 0
        students.append({"no":no,"name":name,"kor":score[0],"eng":score[1],"math":score[2],"total":total,"avg":avg,"rank":rank})
        print(f"{name} 학생 성적이 입력되었습니다.")
        count += 1
        print()
        return count



# 국어,영어,수학 점수입력하고 확인하는 함수
def score_cal(i,score):
    while True:
        score[i] = input(f"{title[i+2]} 점수를 입력하세요.>> ")
        if score[i].isdigit():
            score[i] = int(score[0])      # 숫자변환
            if 0 <= score[i] <= 100: # 0에서 100사이의 값인지 확인
                break
            else: print("점수는 1~100 사이의 값을 입력하셔야 합니다.")
        else: print("숫자만 가능합니다.")


students = [
    {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
    {"no":2,"name":"유관순","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
    {"no":3,"name":"이순신","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
] # 리스트랑 하는 건 똑같음. 

count = 4     # 학생번호를 생성
title = ['번호','이름','국어','영어','수학','합계','평균','등수']

while True:
    print()
    print("[ 학생성적 프로그램 ]")
    print("-"*30)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("0. 프로그램종료")
    print("-"*30)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    print()
    
    # 번호선택
    if choice == 1:
        stu_input(count)
    elif choice == 2:
        print("-"*30)
        print(" "*20,end="")
        print("[ 학생성적 출력 ]")
        print("-"*60)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print("-"*60)
        for s in students:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
        print()
    
    elif choice == 3:
        print("[ 학생성적 수정 ]")
        print("-"*30)

        name = input("수정하려는 학생 이름을 입력하세요.>> ")
        temp = 0   # 찾고자하는 학생이 없을 경우

        for s in students:
            if s["name"]==name:   # 찾았을 경우
                temp = 1            # temp = 1 변경 - 찾았을 경우
                print(f"{name} 학생이 목록에 있습니다. 성적을 수정합니다.")
                print("[ 수정할 과목 선택 ]")
                print("1. 국어")
                print("2. 영어")
                print("3. 수학")
                print("-"*30)
                choice = int(input("원하는 번호를 입력하세요.>> "))
                sub_list = ['','kor','eng','math']
                
                # 수정할 과목 확인
                if choice == 1:
                    pre_kor = s['kor']  # 이전국어점수변수
                    print(f"현재 국어 점수: {pre_kor}")
                    s['kor'] = int(input("변경 국어점수 : "))
                    # 합계, 평균 수정
                    s['total'] = s['kor']+s['eng']+s['math']
                    s['avg'] = s['total']/3
                    print(f"국어점수 : {pre_kor} 점을 {s['kor']} 점으로 변경했습니다.")
                    
                elif choice == 2:
                    pre_eng = s['eng']  # 이전국어점수변수
                    print(f"현재 영어 점수: {pre_eng}")
                    s['eng'] = int(input("변경 영어점수 : "))
                    # 합계, 평균 수정
                    s['total'] = s['kor']+s['eng']+s['math']
                    s['avg'] = s['total']/3
                    print(f"영어점수 : {pre_eng} 점을 {s['eng']} 점으로 변경했습니다.")   
                    
                elif choice == 3:
                    pre_math = s['math']  # 이전국어점수변수
                    print(f"현재 수학 점수: {pre_math}")
                    s['math'] = int(input("변경 수학점수 : "))
                    # 합계, 평균 수정
                    s['total'] = s['kor']+s['eng']+s['math']
                    s['avg'] = s['total']/3
                    print(f"영어점수 : {pre_math} 점을 {s['math']} 점으로 변경했습니다.")   

            # 수정할 학생을 찾지 못했을 경우 - for문이 돌아갈 때마다 출력하지 않게 하기 위해 변수 temp 사용
                if temp == 0:
                    name = input(f"{name} 학생이 목록에 없습니다. 다시 입력하세요. >> ")
    elif choice == 0:
        print("[ 프로그램 종료 ]")
        break