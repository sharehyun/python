students = [
    {'no': 1, 'name': '홍길동', 'kor': 60, 'eng': 100, 'math': 100, 'total': 260, 'avg': 86.66666666666667, 'rank': 3}, 
    {'no':2, 'name': '유관순', 'kor': 100, 'eng': 80, 'math': 99, 'total': 279, 'avg': 93.0, 'rank': 1}, 
    {'no': 3, 'name': '이순신', 'kor': 100, 'eng': 100, 'math': 55, 'total': 255, 'avg': 85.0, 'rank': 4}, 
    {'no': 4, 'name': '강감찬', 'kor': 80, 'eng': 60, 'math': 71, 'total': 211, 'avg': 70.33333333333333, 'rank': 5},
    {'no': 5, 'name': '김구', 'kor': 90, 'eng': 90, 'math': 98, 'total': 278, 'avg': 92.66666666666667, 'rank': 2}
]

# stu.txt파일의 문자를 읽어와서 list타입으로 변경
# -------------
# list타입을 -> stu.txt 저장
# 딕셔너리형태를 -> 1,홍길동,60,100,100,260,86.66666666666667,3    # 딕셔너리형태로넣기엔 분리하기가 복잡해서 데이터만 넣고 다시 분류하는것
s = {'no': 1, 'name': '홍길동', 'kor': 60, 'eng': 100, 'math': 100, 'total': 260, 'avg': 86.66666666666667, 'rank': 3}
data = f"{s['no']},{s['name']},{s['kor']},{s['eng']},{s['math']},{s['total']},{s['avg']},{s['rank']}"
print(s)
print("-"*50)
print(data)

# stu.txt 파일 저장
f = open("py0404/sut.txt","w",encoding='utf8')
for s in students:
    data = f"{s['no']},{s['name']},{s['kor']},{s['eng']},{s['math']},{s['total']},{s['avg']},{s['rank']}\n"
    f.write(data)
f.close()

    
