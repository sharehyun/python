#1-100까지 랜덤숫자를 생성해서 정답을 맞추는 프로그램을 구현하시오.

#1. 랜덤숫자 생성
#2. num list생성
#3. n 변수 생성
#4. 10번 for문 생성
#5. num list에 저장
#6. 정답비교
#7. 데이터 출력

#도전 회수 : 5
#도전 번호 : [1,2,3,4,5]
#랜덤 번호 : 

import random
num = []
n=0

ran_num = random.randint(1,100)

in_num = int(input("숫자를 입력하세요.>> "))
num.append(in_num)


if in_num==ran_num:
    print("정답입니다. 랜덤 숫자 : {}".format(ran_num))

elif in_num>ran_num:
    print("더 작은 수를 입력하세요. 입력 숫자 : {}".format(in_num))
else:
    print("더 큰 수를 입력하세요. 입력 숫자 : {}".format(in_num))

