from stuFunc import *


while True:
    print("[ 학생성적프로그램 ]")
    print("-"*30)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적검색")
    print("4. 학생성적정렬")
    print("5. 학생성적출력(아이디, 전화번호 포함)")
    print("8. 등수처리")
    print("9. 등급처리")
    print("0. 프로그램 종료")
    print("-"*30)
    choice = int(input("숫자를 입력하세요.>> "))
    
    if choice == 1:   # 학생성적입력
        stuInsert()
    elif choice == 2:  # 학생성적출력
        stuAllSelect()
    elif choice == 3:  # 학생성적검색
        stuSearch()
    elif choice == 4:  # 학생성적정렬
        stuSort()
    elif choice == 5:  # 아디전번
        pass
    elif choice == 8:  # 등수처리
        rankUpdate()
    elif choice == 9:  # 등급처리
        gradeUpdate()
    else:
        print("프로그램 종료")
        break



# ## update
# sql = "update stuscore2 set rank = 0"
# cursor.execute(sql)
# conn.commit()



# ## select
# sql = "select * from stuscore2"
# cursor.execute(sql)

# rows = cursor.fetchall()
# for r in rows:
#     print(r)
    
# conn.close()

# print("종료")