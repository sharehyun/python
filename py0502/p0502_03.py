### 학생성적프로그램에서 1명의 학생을 등록해보세요.

from stuConn import *

conn = connections()

# 학생성적프로그램 입력하기
name = input("학생 이름을 입력하세요.>> ")
kor = int(input("국어 점수를 입력하세요.>> "))
eng = int(input("영어 점수를 입력하세요.>> "))
math = int(input("수학 점수를 입력하세요.>> "))
total = kor+eng+math
avg = total/3

query = "insert into stuscore values ( stuscore_seq.nextval,:name,:kor,:eng,:math,:total,:avg,0 )"
cursor = conn.cursor()
cursor.execute(query,name=name,kor=kor,eng=eng,math=math,total=total,avg=avg)
conn.commit()
conn.close()

print(f"{name} 학생 성적이 저장되었습니다.")