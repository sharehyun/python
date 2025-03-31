# 좌표맞추기 프로그램 구현하기

#1차원 리스트 만들고 랜덤 섞기
import random
first_list = [i for i in range(25+1)]
random.shuffle(first_list)

#2차원 리스트 만들어 넣기
a_list = [[0]*5 for i in range(5)]
for i in range(5):
    for j in range(5):
        a_list[i][j] = first_list[5*i+j]

# 출력
while True:
    print("[좌표 맞추기 프로그램]")
    print("0  |",end="\t")
    for i in range(5):
        print(i,end="\t")
    print()
    print("-"*45)
    
    for i in range(5):
        print(f"{i}",end="\t")
        for j in range(5):
            print(a_list[i][j],end="\t")  
        print()  
        

    break