import random

# 랜덤으로 1-45까지 숫자 6개 ran_list
# 입력받은 숫자 6개를 my_list 저장
# 랜덤번호 : 
# 입력번호 : 
# 당첨개수 : 
# 당첨번호 : 

# 랜덤번호 6개 리스트
ran_list = random.sample(range(1,45+1),6)
my_list = [] # 입력번호 저장 리스트
lotto_count = 0 # 당첨개수
lotto_list = [] # 당첨번호

i = 0
while i < 6:
    num = int(input("{}번째 숫자를 입력하시오.>> ".format(i+1))) # i는 0부터 시작하기 때문에 i에 1을 더함
    if num not in my_list:
        my_list.append(num)
        i+=1

# 당첨 비교 ran_list, my_list
# for j in range(6):
#     for k in range(6):
#         if ran_list[j] == my_list[k]:
#             lotto_count += 1
#             lotto_list.append(my_list[k])
#             break

for j in range(6):
    if ran_list[j] in my_list:
        lotto_count += 1 
        lotto_list.append(ran_list[j])

print("랜덤번호 : {}".format(ran_list))
print("입력번호 : {}".format(my_list))
print("당첨개수 : {}".format(lotto_count))
print("당첨번호 : {}".format(lotto_list))


# 반복을 해서 ran_list에 10개를 입력시키는 프로그램을 구현하시오.
# 단, 같은 숫자가 들어가지 않도록 하시오.


# ran_list = random.sample(range(1,45+1),6)랑 이하 같음
# ran_list = []
# i = 0
# while i<6:
#     ran_input = random.randint(1,10)
#     if ran_input not in ran_list:
#         ran_list.append(ran_input)
#         i += 1
