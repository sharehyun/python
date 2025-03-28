# 3,5,7,9단 홀수단만 출력

# 시작 단과 끝나는 단을 입력받아, 출력하시오.
num1 = int(input("input number>> "))
num2 = int(input("input number>> "))

if num1>num2:
    t=num1; num1=num2; num2=t

for i in range(num1,num2+1):
    print("[ {} 단 ]".format(i),end=" ")
    for j in range(1,9+1):
        print("{} x {} = {}".format(i,j,i*j),end=" ")
    print()


# # 구구단 출력, 이중 for문
# for i in range(2,9+1):
#     # if문 삽입
#     if i%2 == 1: #홀수단만, 1을 0으로 바꾸면 짝수단만
#         print("[ {} 단 ]".format(i))
#         for j in range(1,9+1):
#             print("{} x {} = {}".format(i,j,i*j))  # print("{} x {} = {}".format(i,j,i*j),end=" ") 가로로 쭉~
#         print() # 단마다 줄바꿈용




# # 두 수를 입력받아, 두 수 사이의 합계를 구하시오.
# # ex. 1,7 입력시 1,2,3,4,5,6,7까지 합을 출력
# # 1,10 -> 10,1

# num1 = int(input("input number>> "))
# num2 = int(input("input number>> "))
# print(num1,num2)

# if num1>num2:
#     t = num1; num1 = num2; num2 = t  # num1,num2=num2,num1 파이썬만 가능

# sum = 0
# for i in range(num1,num2+1):
#     sum = sum + i
#     print("i : {} / sum : {}".format(i,sum))

# print("{}에서 {}까지의 합계 : {}".format(num1,num2,sum))