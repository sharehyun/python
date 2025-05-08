import oracledb

def connections():
    try: conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
    except Exception as e: print(e)
    return conn
conn = connections()
cursor = conn.cursor()


title = ['번호','이름','국어','영어','수학','총합','평균','등수','등급','반']

## db연결
while True:
    print("[ 학생성적프로그램 ]")
    print("-"*30)
    print("1. 학생전체출력")
    print("2. 반별 1등학생 출력")
    print("3. 반별 최하등수 출력")
    print("4. 부서별 최고연봉 출력")
    print("5. stuscore2 반배정")
    print("6. 회원정보 rownum 사용 11-20 출력")
    print("-"*30)
    
    choice = int(input("원하는 번호를 입력하세요.>> "))
    print()
    
    if choice == 1:
        print("[ 학생전체출력 ]")
        print("-"*90)
        print("{}\t{}\t\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print("-"*90)
        sql = "select * from stuscore2"
        cursor.execute(sql)
        students = cursor.fetchall()
        for s in students:
            if len(s[1])>7:
                print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]}\t{s[7]}\t{s[8]}\{s[9]}")
            else:
                print(f"{s[0]}\t{s[1]}\t\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]}\t{s[7]}\t{s[8]}\t{s[9]}")
            print()
    elif choice ==2:
        pass
    elif choice ==3:
        pass
    elif choice ==4:
        print("-"*60)
        print("[ 부서별 최고연봉 출력 ]")
        print("-"*60)
        sql = """select a.department_id,department_name,emp_name,salary from employees a, departments c
                where salary in (
                select max(salary) from employees b
                where a.department_id = b.department_id
                group by department_id
                ) and a.department_id = c.department_id"""
        cursor.execute(sql)
        departments = cursor.fetchall()
        print("부서id\t부서명\t\t사원명\t\t\t연봉")
        for d in departments:
            if len(d[1])>=5: print(f"{d[0]}\t{d[1]}\t{d[2]}\t\t{d[3]}")
            else: 
                if len(d[2])>=16: print(f"{d[0]}\t{d[1]}\t\t{d[2]}\t{d[3]}")
                else:print(f"{d[0]}\t{d[1]}\t\t{d[2]}\t\t{d[3]}")
        print()
        
    elif choice ==5:
        sql = """update stuscore 
                set sclass = case
                when sno between 1 and 10 then 1
                when sno between 11 and 20 then 2
                when sno between 21 and 30 then 3
                when sno between 31 and 40 then 4
                when sno between 41 and 50 then 5
                when sno between 51 and 60 then 6
                when sno between 61 and 70 then 7
                when sno between 71 and 80 then 8
                when sno between 81 and 90 then 9
                when sno between 91 and 100 then 10
                else 11
                end"""
        cursor.execute(sql)
        conn.commit()
        print("반배정이 완료되었습니다.")
        
    elif choice ==6:
        pass
    
    else:
        print("[ 프로그램 종료 ]") 
        break
