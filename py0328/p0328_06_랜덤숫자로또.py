# 숫자 맞추기 프로그램
import random
input_list = [] # 입력한 숫자 저장 리스트타입 변수
lotto = random.randint(1,45) # randint(1,45) 1~45번 사이의 숫자 1개를 가져옴.

#------------------
for i in range(10):    # 10번 반복
    input_num = int(input("{}번째 도전 : 숫자를 입력하세요. (1~45 사이)>> ".format(i+1)))
    input_list.append(input_num) # 리스트에 숫자 추가
    # 랜덤번호와 입력번호 비교
    if lotto == input_num:
        print("당첨")
        break  #for문 종료
    elif lotto>input_num:
        print("틀렸습니다. {}보다 더 큰 수를 입력하세요. 지금까지 입력한 번호 : {}".format(input_num,input_list))
    else:
        print("틀렸습니다. {}보다 더 작은 수를 입력하세요. 지금까지 입력한 번호 : {}".format(input_num,input_list))

#------------------

print("랜덤번호 : {}".format(lotto))
print("입력번호 : {}".format(input_list))