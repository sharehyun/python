# 5x5 리스트 0으로 초기화 (간단)
# sample_list = [[0]*5 for i in range(5)]
# print(sample_list)


# # 5x5 리스트 0으로 초기화
# sample_list = list() #list초기화
# for i in range(5):
#     temp = []
#     for j in range(5):
#         temp.append(0) # [0,0,0,0,0]
#     sample_list.append(temp)  # [[0,0,0,0,0]]
# print(sample_list)

# a_list = [i+1 for i in range(25)]
# [1,2,3,4........23,24,25]

# import random
# # 1. 순차적 리스트 생성
# sample_list = [i+1 for i in range(25)]
# # 2. 리스트 섞기
# random.shuffle(sample_list)  # 랜덤리스트 - 리스트의 숫자가 랜덤으로 섞임
# #3. 2차원 초기화 리스트 생성
# a_list = [[0]*5 for i in range(5)] # 깊은복사
# #4. 2차원 리스트에 랜덤리스트의 값을 입력
# for i in range(5):
#     for j in range(5):
#         a_list[i][j] = sample_list[5*i+j]  # 랜덤숫자가 들어감.

# # 5x5 리스트 출력
# for i in range(5):
#     for j in range(5):
#         print(a_list[i][j], end="\t")
#     print()

# # 5x5 리스트 초기화
# a_list = [[0]*3]*5   # 얕은 복사
# a_list = [[0]*5 for i in range(5)]  # 깊은 복사, 중요
# print(a_list)
# for i in range(5):
#     for j in range(5):
#         a_list[i][j] = 5*i+(j+1)
# print(a_list)


# # 1-25
# import random
# a_list = [i+1 for i in range(25)]
# print(a_list)
# random.shuffle(a_list)
# # 랜덤으로 섞여진 리스트 출력
# print(a_list)


# a_list = [
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,12,13,14,15],
#     [16,17,18,19,20],
#     [21,22,23,24,25]
# ]

# for i in range(5):
#     for j in range(5):
#         print(a_list[i][j],end=" ")
#     print()


# a_list = [
#     [1,2,3],     #[0][0],[0][1],[0][2]
#     [4,5,6],     #[1][0],[1][1],[1][2]
#     [7,8,9]      #[2][0],[2][1],[2][2]
# ]

# for i in range(3):  #0,1,2
#     for j in range(3):  #0,1,2
#         print(a_list[i][j], end="\t")
#     print()

# # 1차원 리스트
# aa = [10,20,30]
# print(aa[0])  # 10

# # 2차원 리스트
# aa = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]

# print(aa[0])
# print(aa[0][0])


# a_list = [1,2,3,4,5,6,7,8,9]
# a_list[5] = 10 
# print(a_list)

# # 값을 변경할 때 1:2, 2의 위치값이 포함, 변경됨
# a_list[1:2] = [100,200]
# print(a_list)

# # 역순출력
# a_list = [1,2,3,4,5]  
# print(a_list[::-1])

# print(a_list[1:2+1])  # == print(a_list[1:3])


# # 모양 출력
# for i in range(10):
#     for j in range(i+1):  # 1,2,3,4,5,6,7,8,9,10
#         print("*",end="")
#     print()


# for i in range(10):
#     if i%2 == 0: continue
#     print(i)


# continue - 그 위치에서 중지, 다시 for문 실행
# 1-10까지 진행을 하는데, 1,2,3-continue(제외),4,5,6,7,8,9,10
# break - 반복문 완전 중지 
# 1-10까지 진행하는데 1,2,3-break(반복문 끝) 
# pass - 실행할 구문이 없음, for문을 계속 반복
# 1-10까지 진행 1,2,3-pass,4,5,6,7,8,9,10 10번을 실행
# 입력한 숫자의 합이 50을 넘으면 프로그램을 종료하고 총합을 구하시오.
# 입력한 숫자 중 5의 배수는 제외시킬 것


# sum = 0
# while True:   # 영원히 반복, 밑에 조건을 추가해야 함
#     if sum<50:
#         num = int(input("숫자를 입력하시오.>> "))
#         if num%5==0: 
#             print(f"입력한 숫자 {num}, 5의 배수 제외!")
#             continue # 실행을 1번 중지
#         else: sum += num
#     else: break
    
# print(f"총합 : {sum}")


# 1-100까지의 숫자의 합을 구할 때, 합계가 200을 넘을 때의 숫자를 출력하시오.
# 1+2+3+4... 값이 200이 넘는 위치값
# break : 반복문을 중지시켜줌
# sum = 0
# for i in range(100):
#     sum += i
#     if sum>200:
#         print(f"숫자 : {i}\n합계 : {sum}")
#         print(f"숫자 : {i-1}\n합계 : {sum-i}")
#         break

# # 반복문 - for, while

# # 1-10까지 리스트 생성
# a_list = [i+1 for i in range(100)]
# print(a_list)

# # a_list 홀수의 합계를 구하시오.
# sum = 0           # 변수 sum 선언
# for i in a_list:  
#     if i%2==1:    # 홀수이면,
#         sum+=i    # i의 값을 합계변수에 더함
# print("홀수 합계 :",sum)
    
        
# # random.random() 함수 : 0 <= x < 1 사이의 랜덤실수를 가져옴.
# import random
# print(random.random())  # 0.000000000000000000 <= x < 1.000000000000000000 18자리
# print(int(random.random()*10)+1)  # 1,10
# print(int(random.random()*10)+0)  # 0,9
# print(random.randint(1,10))

# print(random.randint(1,10+1))

# import random
# a_list = [i+1 for i in range(45)]
# print(a_list)

# random.shuffle(a_list)
# print(a_list)

# print(a_list[:6])


# 로또 프로그램
# 6개 랜덤숫자와 입력숫자 6개를 출력하시오.

# import random
# lotto = [i+1 for i in range(45)] # 1,2,3,4,5..........45
# lotto_input = []
# my_input = []

# lotto_input = random.sample(lotto,6) # 리스트에서 중복 없이 6개를 가져옴. 파이썬에만 있음
# for i in range(6):
#     lotto.append(random.randint(1,45))   # 중복 가능

# for i in range(6):
#     num = int(input("{}번째 번호를 입력하세요.>> ".format(i+1)))
#     my_input.append(num)

# print("로또 번호 : {}".format(lotto_input))
# print("입력 번호 : {}".format(my_input))



# 10번의 숫자를 입력받아, 합계를 구하시오.
# i = 0
# sum1 = 0
# while i<10:
#     input_num1 = int(input("숫자를 입력하시오.>> "))
#     sum1 += input_num1
#     i += 1
# print("합계 :",sum1)



# sum2 = 0
# for i in range (10):
#     input_num2 = int(input("input number>> "))
#     sum2 += input_num2
# print("sum :",sum2)


# while 문
# i = 0
# while i<10:
#     print(i)
#     i=i+1

# for문
# for i in range(10):  # 10번 반복
#     print(i)

# for i in range(0,3,1):
#     print(f"{i+1}. 안녕하세요? for문을 공부하는 중입니다.")