from dbconn import *

conn = connections()   # 오라클 접속
cursor = conn.cursor() # sql developer 연결

while True:
    print("-"*30)
    print("[ 학생성적프로그램 ]")
    print("-"*30)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 학생성적검색")
    print("5. 학생성적정렬")
    print("0. 프로그램 종료")
    print("-"*30)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    if choice == 1:
        ### 직접입력
        name = input("이름을 입력하세요.>> ")
        kor = int(input("국어점수를 입력하세요.>> "))
        eng = int(input("영어점수를 입력하세요.>> "))
        math = int(input("수학점수를 입력하세요.>> "))
        total = kor+eng+math
        avg = total/3

        ### insert - 1개 저장
        query = "insert into stuscore values(stuscore_seq.nextval,:name,:kor,:eng,:math,:total,:avg,0)"
        cursor.execute(query,name=name,kor=kor,eng=eng,math=math,total=total,avg=avg)
        conn.commit()
        print(f"{name} 학생 성적이 저장되었습니다.")
        print()
        
    elif choice == 2:
        query = 'select * from stuscore'
        cursor.execute(query)  # 명령문 실행
        rows = cursor.fetchall()   # 실행 결과 - 여러개
        for r in rows:
            print(r)
        print()
            
    elif choice == 3:
        ## 이름을 입력하세요. -> 학생검색
        
        name = input("수정하려는 학생 이름을 입력하세요.>> ")
        kor = int(input("국어점수를 수정하세요>> "))
        query = "update stuscore set kor=:kor,total=:kor+eng+math,avg=(:kor+eng+math)/3 where name=:name"
        cursor.execute(query,kor=kor,name=name)
        conn.commit()
        print("수정이 되었습니다.")
        
        
    elif choice == 4:
        ### 이름 검색해서 해당 학생 출력
        name = input("검색하려는 학생 이름을 입력하세요.>> ")
        # name = '%'+name+'%'  # %를 인식을 못함
        # like '%'||:name||'%' ||는 concat명령어(글자를 합침)
        query = "select * from stuscore where name like '%'||:name||'%'"
        cursor.execute(query,name=name) # 명령문 실행
        rows = cursor.fetchall()
        name = name - '%'
        if len(rows)<=0:
            print(f"{name} 학생을 찾지 못했습니다.")
            continue
        # 검색하려는 학생이 있으면
        for r in rows:
            print(r)
        print()
        
    elif choice == 5:
        ## 정렬
        print("이름 순차정렬")
        query= "select * from stuscore order by name"
        cursor.execute(query)
        rows = cursor.fetchall()
        for r in rows:
            print(r)
        print()
        
    else: break




# 종료
conn.close()
print("종료")


# ### select - 한개 데이터 가져오기
# query = 'select count(*) from stuscore'
# cursor.execute(query)
# cnt = cursor.fetchone()  # 실행결과 - 한개
# print("학생수 : ",cnt[0]) # (100,) 데이터형태
# # cnt = cursor.fetchall()  # 실행결과 - 한개
# # print("학생수 : ",cnt[0][0])  # [(100,)] 배열형태


# ##  select - 여러개 데이터 가져오기
# query = 'select * from stuscore'
# cursor.execute(query)  # 명령문 실행
# rows = cursor.fetchall()   # 실행 결과 - 여러개
# for r in rows:
#     print(r)

# # 종료
# conn.close()