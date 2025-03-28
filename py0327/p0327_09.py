# 0보다 같거나 크고, 1미만 인 랜덤실수 값을 뽑아서 전달해줌.
# 0 <= x < 1  0.1245234554
# print(random.random())

# print(random.randint(1,10)) # 1,100   0-99


# 랜덤숫자를 맞추는 프로그램
# ran_num = random.randint(1,5)
# in_num = int(input("랜덤숫자 맞추기!! 1-5까지의 숫자 1개를 입력하세요.>> "))
# if ran_num == in_num:
#     print("정답입니다. 랜덤숫자 : {}".format(ran_num))
# else:
#     print("오답입니다. 랜덤숫자 : {}, 입력숫자 : {}".format(ran_num,in_num))    



# 1-100까지의 숫자 10개를 입력 받음

# num = []
# for 반복문
# for n in range(1,11): # 1,2,3,4,5,6,7,8,9,10
#     print(n)

import random
num = []    
# 1-100 랜덤숫자 1개 생성    
ran_num = random.randint(1,100)
n = 0 # 몇번 시도
for n in range(1,11):
    in_num = int(input("숫자를 입력하세요.>> ")) 
    num.append(in_num) #num list타입에 데이터를 추가
    if ran_num == in_num:
        print("정답입니다. 랜덤숫자 : {} ".format(ran_num))  
        break 
    elif ran_num>in_num:
        print("더 큰수를 입력하세요. 입력숫자 : {}".format(in_num))    
    else:
        print("더 작은 수를 입력하세요. 입력숫자 : {}".format(in_num))    

print("도전 회수 : {}".format(n))
print("입력된 숫자 : {}".format(num))        
print("랜덤 숫자 : {}".format(ran_num))
