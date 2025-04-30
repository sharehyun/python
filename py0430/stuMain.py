### 학생성적 프로그램

students = []
title = ['번호','이름','국어','영어','수학','합계','평균','등수']
count=1

while True:
    print("-"*30)
    print("[ 학생성적프로그램 ]")
    print("-"*30)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 학생성적삭제")
    print("5. 학생성적정렬")
    print("6. 학생성적검색")
    print("0. 프로그램 종료")
    print("-"*30)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    print()
    
    if choice == 1:
        print("[ 학생성적입력 ]")
        print("-"*30)
        no = count
        name = input("학생 이름을 입력하세요.>> ")
        kor = int(input("국어 점수를 입력하세요.>> "))
        eng = int(input("영어 점수를 입력하세요.>> "))
        math = int(input("수학 점수를 입력하세요.>> "))
        total = kor+eng+math
        avg = total/3
        rank = 0
        students.append({'no':no,'name':name,'kor':kor,'eng':eng,'math':math,'total':total,'avg':avg,'rank':rank})
        print(f"{name} 학생 성적이 입력되었습니다.")
        count+=1
        continue
        
    elif choice == 2:
        print("[ 학생성적출력 ]")
        print("-"*60)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print("-"*60)
        for s in students:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
        print()
        continue
    
    elif choice == 3:
        print("[ 학생성적수정 ]")
        name = input("수정할 학생 이름을 입력하세요.>> ")
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
                choice = int(input("수정할 과목을 선택해 주세요.>> "))
                if choice == 1:
                    print("[ 국어 과목 수정 ]")
                    pre_score = s['kor']
                    print(f"현재 국어 점수 : {pre_score}")
                    s['kor'] = int(input("수정할 국어 점수를 입력해주세요.>> "))
                    print("수정 전 국어 점수 : ",pre_score)
                    print("수정 후 국어 점수 : ",s['kor'])
                    s['total'] = s['kor']+s['eng']+s['math']
                    s['avg'] = s['total']/3
                    
                elif choice == 2 :
                    print("[ 영어 과목 수정 ]")
                    pre_score = s['eng']
                    print(f"현재 영어 점수 : {pre_score}")
                    s['eng'] = int(input("수정할 영어 점수를 입력해주세요.>> "))
                    print("수정 전 영어 점수 : ",pre_score)
                    print("수정 후 영어 점수 : ",s['eng'])
                    s['total'] = s['kor']+s['eng']+s['math']
                    s['avg'] = s['total']/3
                    
                elif choice == 3:
                    print("[ 수학 과목 수정 ]")
                    pre_score = s['math']
                    print(f"현재 수학 점수 : {pre_score}")
                    s['math'] = int(input("수정할 수학 점수를 입력해주세요.>> "))
                    print("수정 전 수학 점수 : ",pre_score)
                    print("수정 후 수학 점수 : ",s['math'])
                    s['total'] = s['kor']+s['eng']+s['math']
                    s['avg'] = s['total']/3
                    
        if temp == 0:
            print(f"{name} 학생을 목록에서 찾지 못했습니다.")
            continue
                        
    elif choice == 4:
        print("[ 학생성적삭제 ]")
        name = input("삭제할 학생 이름을 입력하세요.>> ")
        temp = 0
        for i,s in enumerate(students):
            if name in s['name']:
                temp = 1
                print(f"{name} 학생을 목록에서 찾았습니다.")
                answer = input("성적을 삭제하시겠습니까?(y-삭제,n-취소)>> ")
                if answer == 'y':
                    print(f"{name} 학생 성적을 삭제했습니다.")
                    del students[i]
                elif answer == 'n':
                    print("삭제를 취소합니다.")
        if temp == 0:
            print(f"{name} 학생을 목록에서 찾지 못했습니다.")
                        
                        
    elif choice == 5:
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
        students2 = [*students]
        if choice == 1:  # 이름 순차정렬
            students2.sort(key=lambda x:x['name'])
        elif choice == 2: # 이름 역순정렬
            students2.sort(key=lambda x:x['name'],reverse=True)
        elif choice == 3: # 총합 순차정렬
            students2.sort(key=lambda x:x['total'])
        elif choice == 4: # 총합 순차정렬
            students2.sort(key=lambda x:x['total'],reverse=True)
        elif choice == 5: # 번호 순차정렬
            students2.sort(key=lambda x:x['no'])
        elif choice == 6: # 번호 역순정렬
            students2.sort(key=lambda x:x['no'],reverse=True)
            
        print("-"*60)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print("-"*60)
        for s in students2:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
        print()
        
            
                        
    elif choice == 6:
        print("[ 학생성적검색 ]")
        name = input("검색하려는 학생 이름을 입력하세요.>> ")
        temp = 0
        for s in students:
            if name in s['name']:
                temp = 1
                print(f"{name} 학생을 목록에서 찾았습니다.")
                print("-"*60)
                print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
                print("-"*60)
                print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
                print()
                continue
        if temp == 0:
            print(f"{name} 학생을 목록에서 찾지 못했습니다.")         
        
    
    else:
        print("[ 프로그램 종료 ]")
        break

