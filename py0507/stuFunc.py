import oracledb

#db연결
def connections():
    try: conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
    except Exception as e: print(e)
    return conn

#학생성적입력
def stuInsert():
    conn = connections()
    cursor = conn.cursor()
    name = input("학생 이름을 입력하세요.>> ")
    kor = int(input("국어 점수를 입력하세요.>> "))
    eng = int(input("영어 점수를 입력하세요.>> "))
    math = int(input("수학 점수를 입력하세요.>> "))
    total = kor+eng+math
    avg = total/3
    sql = f"insert into stuscore values(stuscore_seq.nextval,'{name}',{kor},{eng},{math},{total},{avg},0,'F')"
    cursor.execute(sql)
    conn.commit()
    
    sql = "update stuscore a set rank = (select ranks from (select sno,rank() over (order by total desc) as ranks from stuscore) b where a.sno = b.sno)"
    cursor.execute(sql)
    conn.commit()
    
    sql = """update stuscore a 
    set sgrade = (select grades 
    from (select sno,avg,grade as grades from stuscore,scoregrade 
    where avg between minscore and maxscore) b
    where a.sno=b.sno)"""
    cursor.execute(sql)
    conn.commit()
    
        
    print(f"{name} 학생 성적을 입력했습니다.")
    

#학생전체출력
def stuAllSelect(sql = "select * from stuscore order by sno"):
    conn = connections()
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for r in rows:
        print(r)
        
# 학생성적검색
def stuSearch():
    conn = connections()
    cursor = conn.cursor()
    search = input("검색할 학생 이름을 입력하세요.>> ")
    # sql = f"select * from stuscore where name like '%{search}%'"
    sql = "select * from stuscore where name like '%'||:search||'%'"
    cursor.execute(sql,search=search)
    rows = cursor.fetchall()
    if len(rows)>0:
        for r in rows:
            print(r)
    else: print(f"{search} 학생이 목록에 없습니다.")
    cursor.close()

# 학생성적정렬
def stuSort():
    print("[ 학생성적정렬 ]")
    print("1. 이름순 정렬")
    print("2. 성적순 정렬")
    print("3. 국어순 정렬")
    print("4. 영어순 정렬")
    print("5. 수학순 정렬")
    choice = int(input("숫자를 입력하세요.>> "))
    if choice == 1: sorting('이름','name')
    elif choice == 2: sorting('성적','total')
    elif choice == 3: sorting('국어','kor')
    elif choice == 4: sorting('영어','eng')
    elif choice == 5: sorting('수학','math')

        

## 순차정렬, 역순정렬
def sorting(sName,sName2):
    conn = connections()
    cursor = conn.cursor()
    print(f"1. {sName}순차정렬")
    print(f"2. {sName}역순정렬")
    choice = int(input("숫자를 입력하세요.>> "))
    if choice == 1:
        sql = f"select * from (select * from stuscore order by total) order by {sName2}"
    else:
        sql = f"select * from (select * from stuscore order by total desc) order by {sName2} desc"
    cursor.execute(sql)
    stuAllSelect(sql)


# 등수처리 - 1,2,3...
def rankUpdate():
    conn = connections()
    cursor = conn.cursor()
    sql = "update stuscore a set rank = (select ranks from (select sno,rank() over (order by total desc) as ranks from stuscore) b where a.sno = b.sno)"
    cursor.execute(sql)
    conn.commit()
    print("등수처리 완료")

# 등급처리 - A,B,C...
def gradeUpdate():
    conn = connections()
    cursor = conn.cursor()
    sql = """update stuscore a 
    set sgrade = (select grades 
    from (select sno,avg,grade as grades from stuscore,scoregrade 
    where avg between minscore and maxscore) b
    where a.sno=b.sno)"""
    cursor.execute(sql)
    conn.commit()
    print("등급처리 완료")


