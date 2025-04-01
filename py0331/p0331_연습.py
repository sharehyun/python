# 1차원리스트 생성 후 랜덤으로 섞기
# 2차원리스트 생성 후 1차원리스트 값을 넣기
# 2차원 출력 - for문을 두 번
# 입력부분
# 좌표에 값 넣기

import random
first_list = [i+1 for i in range(25)]
random.shuffle(first_list)

a_list = [[0]*5 for i in range(5)]
for i in range(5):
    for j in range(5):
        a_list[i][j] = first_list[5*i+j]

while True:
    print(" "*10,end="")
    print("[ 좌표 입력 프로그램 ]")
    print("-"*45)
    print("0  |",end="\t")
    for i in range(5):
        print(i,end="\t")

    print()
    print("-"*45)
    for i in range(5):
        print(f"{i}  |",end="\t")
        for j in range(5):
            print(a_list[i][j],end="\t")
        print()

    # 입력
    num = int(input("1-25까지의 숫자를 입력하세요>> "))
    for i in range(5):
        for j in range(5):
            if a_list[i][j] == num:
                a_list[i][j] = "X"
                break