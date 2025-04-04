#파일 읽어오기
# 1. open() 2. f.read() 3. f.close()
# r:읽기, w:쓰기, a:이어쓰기

f = open("py0404/stu.txt","r",encoding="utf8")
# 1줄이면 상관X / 여러줄이면 반복문을 실행
students = []
while True:
    data = f.readline()  # 1줄을 읽어와라!
    if not data: break  # 읽어올 데이터가 없으면 읽기 끝!
    # data : 1,홍길동,60,100,100,260,86.66666666666667,3
    # strip() : 공백제거, split() : 공백제거
    s = data.strip().split(",")
    students.append({
        'no':int(s[0]),'name':s[1],'kor':int(s[2]),'eng':int(s[3]),'math':int(s[4]),
        'total':int(s[5]),'avg':float(s[6]),'rank':int(s[7])
    })
f.close()

