# 5x5 2차원 리스트 -> 랜덤으로 1-25까지 숫자를 넣기
# 1차원 리스트 생성
# 1차원 리스트 랜덤으로 섞기
# 2차원 리스트 생성
# 2차원 리스트에 1차원 랜덤번호를 넣기

import random
# 1차원리스트 생성 후 랜덤으로 섞기
first_list = [i+1 for i in range(25)]
random.shuffle(first_list)

# 2차원리스트 생성 후 1차원리스트 값을 넣기
a_list = [ [0]*5 for i in range(5) ]
for i in range(5):
    for j in range(5):
        a_list[i][j] = first_list[5*i+j]  #0,1,2,3.....24

# 2차원 출력 - for문을 두 번
while True:
    print("         [좌표 맞추기 프로그램]")
    print("-"*45)
    print("0  |",end="\t")
    for i in range(5):
        print(i, end="\t")
    print()
    print("-"*45)

    for i in range(5):
        print(f"{i}  |",end="\t")
        for j in range(5):
            print(a_list[i][j],end="\t")
        print()

    # 입력부분
    print("-"*45)
    num = int(input("1-25번 숫자를 입력하세요.>> "))
    
    # 좌표에 값 넣기
    for i in range(5):
        for j in range(5):
            if a_list[i][j] == num: 
               a_list[i][j] = "X"
    print()