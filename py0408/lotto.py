# 로또 프로그램 - p0328_08.py
import random
ran_list = random.sample(range(1,45+1),6)  # 1부터 45까지(괄호 안 뒷번호-1까지), 몇개 뽑을지

my_list = []   # 내가 입력한 번호를 적을 리스트

lotto_count = 0 # 당첨개수
lotto_list = [] # 당첨번호


i = 0  # 6번 입력하려고!
while i < 6:  # 6번 반복
    num = int(input("{}번째 숫자를 입력하시오.>> ".format(i+1))) # i는 0부터 시작하기 때문에, 첫번째 순서라고 나타내려고 i에 1을 더함
    if num not in my_list:   # 숫자가 my list에 없으면 넣기, 있으면 넣지 않음. 넣지 않으면 i에 더해지지 않기 때문에 무한히 반복됨
        my_list.append(num)   # 내 리스트에 추가
        i+=1                  # 반복횟수()
        
for j in range(6):
    if ran_list[j] in my_list:  
        lotto_count += 1 
        lotto_list.append(ran_list[j])

print("랜덤번호 : {}".format(ran_list))  # 로또 번호
print("입력번호 : {}".format(my_list))   
print("당첨개수 : {}".format(lotto_count))
print("당첨번호 : {}".format(lotto_list))