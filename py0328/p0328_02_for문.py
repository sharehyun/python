print("안녕하세요.")
print("안녕하세요.")
print("안녕하세요.")

# range(3) -> 0,1,2 해서 3번 돌게 됨. 시작은 0부터
for i in range(3): #3번 반복해줘
    print("안녕하세요.",i)

# range(1,4) -> 1,2,3 : 4 앞에까지 출력
for i in range(1,4):
    print("안녕하세요.",i)

for i in range(1,3+1):
    print("안녕하세요.",i)

# range(1,11,5) - 첫번째숫자:시작번호, 두번째숫자:마지막번호-1만큼, 세번째숫자:간격   다른 프로그램에서도 똑같이 적용됨
for i in range(1,11,5): #5씩 증가
    print("안녕",i)

# range 자리에 list타입 가능
a_list = [1,2,3,4,5]
for i in a_list:
    print("안녕",i)