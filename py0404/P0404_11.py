from StuFunc2 import *  # stufunc에서 전체 가져오기


### 파일 읽어오기
students = []
with open("py0404/stu.txt","r",encoding="utf8") as f:
    while True:
        data = f.readline()
        if not data: break
        s = data.strip().split(",")
        students.append({
            "no":int(s[0]),"name":s[1],"kor":int(s[2]),"eng":int(s[3]),
            "math":int(s[4]),"total":int(s[5]),"avg":float(s[6]),"rank":int(s[7])
        })

title = ['번호','이름','국어','영어','수학','합계','평균','등수']
count = len(students)+1

while True:
    print("[ 학생성적 프로그램 ]")
    print("-"*30)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 등수처리")
    print("5. 학생성적정렬")
    print("6. 학생성적삭제")    
    print("7. 학생성적저장")
    print("0. 프로그램종료")
    print("-"*30)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    print()

    if choice == 1:  # 학생성적입력
        print("[ 학생성적입력 ]")
        print("-"*30)
        no = count
        name = input(f"{no}번 학생 이름을 입력하세요.>> ")
        kor = int(input("국어 성적을 입력하세요.>> "))
        eng = int(input("영어 성적을 입력하세요.>> "))
        math = int(input("수학 성적을 입력하세요.>> "))
        total = kor+eng+math
        avg = total/3
        rank = 0
        
        students.append({'no':no,'name':name,'kor':kor,'eng':eng,'math':math,'total':total,'avg':avg,'rank':rank})
        print(f"{name} 학생 성적이 입력되었습니다.")
        count += 1
        print()
        
    elif choice == 2:  # 학생성적출력
        print(" "*20,end="")
        print("[ 학생성적출력 ]")
        print("-"*60)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print("-"*60)
        for s in students:
            print(f"{s["no"]}\t{s["name"]}\t{s["kor"]}\t{s["eng"]}\t{s["math"]}\t{s["total"]}\t{s["avg"]:.2f}\t{s["rank"]}")
        print()

        
    elif choice == 3:  # 학생성적수정
        print("[ 학생성적수정 ]")
        print("-"*30)
        name = input("수정하려는 학생 이름을 입력해 주세요.>> ")
        temp = 0
        for s in students:
            if name in s['name']:
                temp = 1
                print(f"{name} 학생을 목록에서 찾았습니다.")
                print("[ 수정 과목 선택 ]")
                print("-"*30)
                print("1. 국어")
                print("2. 영어")
                print("3. 수학")
                print("-"*30)
                choice = int(input("원하는 번호를 입력하세요.>>"))
                sub_list = ["","kor","eng","math"]   # s[key값]을 숫자에 맞춰 다르게 입력하기 위해!
                if choice == 1:
                    stu_fix(s,sub_list,choice,title,name)
                elif choice == 2:
                    stu_fix(s,sub_list,choice,title,name)
                elif choice == 3:
                    stu_fix(s,sub_list,choice,title,name)
                    
        if temp == 0:   # 찾지 못했을 경우
            print(f"{name} 학생을 목록에서 찾지 못했습니다. 다시 입력하세요!!")
            print()   # break하면 프로그램이 끝나버림 ㅠㅠ

    elif choice == 4:  # 등수처리
        stu_rank(students)

    elif choice == 5:  # 학생성적정렬
        pass
    elif choice == 6:  # 학생성적삭제
        pass
    elif choice == 7:  # 학생성적저장
        pass
    elif choice == 0:  # 프로그램종료
        print("[ 프로그램 종료 ]")
        break