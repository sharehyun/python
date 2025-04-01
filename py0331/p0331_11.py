#1차원 리스트 생성, 랜덤 숫자 입력
import random
first_list = [i+1 for i in range(25)]
random.shuffle(first_list)

#2차원 리스트 생성, 1차원 숫자 입력
a_list = [[0]*5 for i in range(5)]
for i in range(5):
    for j in range(5):
        a_list[i][j] = first_list[5*i+j]

# 출력
while True:
    print(" "*10,end="")
    print("[ 좌표 입력 프로그램 ]")
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
    
    num = int(input("1~25번 숫자를 입력하세요.>> "))
    
    for i in range(5):
        for j in range(5):
            if num == a_list[i][j]:
                a_list[i][j] = "X"
                break
        

