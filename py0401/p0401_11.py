students = [
    {'no':1,'name':'홍길동','kor':100,'eng':100,'math':100,'total':300,'avg':100.0,'rank':1},
    {'no':2,'name':'유관순','kor':100,'eng':100,'math':99,'total':299,'avg':99.67,'rank':2},
    {'no':3,'name':'이순신','kor':100,'eng':100,'math':99,'total':299,'avg':99.67,'rank':2},
] 

count = 4     # 학생번호를 생성
title = ['번호','이름','국어','영어','수학','합계','평균','등수']

while True:
    print("[ 학생성적 프로그램 ]")
    print("-"*30)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("0. 프로그램종료")
    print("-"*30)

    choice = int(input("원하는 번호를 입력하세요.>> "))
    
    # 선택
    if choice == 1:
        print("-"*60)
        print(" "*20,end="")
        print("[ 학생성적입력 ]")
        print("-"*60)
        # 반복 입력
        while True:
            no = count 
            name = input(f"{no}번 학생 이름을 입력하세요.(0. 이전 화면)>> ")
            if name == '0': break
            kor = int(input("국어 점수를 입력하세요.>> "))
            eng = int(input("영어 점수를 입력하세요.>> "))
            math = int(input("수학 점수를 입력하세요.>> "))
            total = kor+eng+math
            avg = total/3
            rank = 0
            
            students.append({'no':no,'name':name,'kor':kor,'eng':eng,'math':math,'total':total,'avg':avg,'rank':rank})
            count += 1
            print(f"{name} 학생 성적을 입력했습니다.")
            print()
        
    # 출력
    elif choice == 2:
        print(" "*20,end="")
        print("[ 학생성적출력 ]")
        print("-"*60)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print("-"*60)
        for s in students:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
        print()
    elif choice == 0:
        print("[ 프로그램 종료 ]")
        break
    
    
