# 1차원리스트 생성 후 랜덤으로 섞기
# 2차원리스트 생성 후 1차원리스트 값을 넣기
# 2차원 출력 - for문을 두 번
# 입력부분
# 좌표에 값 넣기

# 1차원리스트 생성 후 랜덤으로 섞기
import random
first_list = [i for i in range(25+1)]
random.shuffle(first_list)

# 2차원리스트 생성 후 1차원리스트 값을 넣기
a_list = [[0]*5 for i in range(5)]
for i in range(5):
    for j in range(5):
        a_list[i][j] = first_list[5*i+j]

# 2차원 출력
print("        [좌표 입력 프로그램]")
print("-"*45)
for i in range(5):
    for j in range(5):
        print(a_list[i][j],end="\t")