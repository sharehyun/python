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
    # num1 = int(input("X좌표 : "))
    # num2 = int(input("Y좌표 : "))
    
    
    # 15 숫자를 넣으면 X표시가 되도록
    num = 15
    
    # if num1<0 and num1>4:
    #     print("숫자를 잘못 입력하셨습니다. 다시 입력하세요.")
    #     continue
    # if num2<0 and num2>4:
    #     print("숫자를 잘못 입력하셨습니다. 다시 입력하세요.")


    # 좌표에 값 넣기
    # a_list[num2][num1] = "X"
    # print()