# 카드 SPADE-4, DIAMOND-3, HEART-2, CLOVER-1
# 번호 1-A,2,3,4,5,6,7,8,9,10,11-J,12-Q,13-K

# 카드 1장 - 카드모양, 번호
# 카드모양 4개
# 13개
# 카드 총 개수 : 52장 카드가 존재

# 리스트 - 딕셔너리
# cList = [
#     {"shape":"SPADE","no":1},
#     {"shape":"SPADE","no":2},
# ]

cList = []
sh = ["CLOVER","HEART","DIAMOND","SPADE"]
no = ["","A","2","3","4","5","6","7","8","9","10","J","Q","K"]

# 카드 생성
for i in range(52):
    cList.append({"shape":i//13,"no":i%13+1})

# 카드 랜덤으로 섞기
import random
random.shuffle(cList)

# myCard, youCard

# 5장을 입력
myCard = []
youCard = []
# 카드 5장씩 배분
for i in range(5):
    myCard.append(cList[i])
for i in range(5,10):
    youCard.append(cList[i])

# 내 카드 출력 - 번호에 해당되는 글자를 출력
print("[ 내 카드 ]")
for i in myCard:
    print(f"[ {sh[ i["shape"] ]}, { no[i["no"]] } ]")
print()

# 상대 카드 출력
print("[ 상대 카드 ]")
for i in youCard:
    print(f"[ {sh[ i["shape"] ]}, { no[i["no"]] } ]") 
print()



# 내카드, 상대카드를 비교해서 승리,패배,무승부
score = {"myWin":0,"youWin":0,"draw":0}
for i in range(5):
    if myCard[i]['no'] > youCard[i]['no']:
        score['myWin'] += 1
    elif myCard[i]['no'] < youCard[i]['no']:
        score['youWin'] += 1
    else:
        score['draw'] += 1
        
print("[ 카드 승부 확인 ]")
print(f"승리 : {score['myWin']}, 패배 : {score['youWin']}, 무승부 : {score['draw']}")


# 승리한 카드 출력
score = [0]*5   #[2,1,2,2,0]
for i in range(5):
    if myCard[i]['no'] > youCard[i]['no']:
        score[i] += 2
    elif myCard[i]['no'] < youCard[i]['no']:
        score[i] += 1
    else:
        score[i] += 0

print("[ 카드 승부 확인 ]")
print(f"승리 : {score.count(2)}, 패배 : {score.count(1)}, 무승부 : {score.count(0)}")
print()

print("[ 승리 카드 ]")
for i,c in enumerate(myCard):
    if score[i]==2:
        print(f"[ {sh[c['shape']]}, {no[c['no']]} ]",end=" ")


## 내 시도
# score = {'myWin':0,"youWin":0,"draw":0}
# outCard = []

# for i in range(5):
#     if myCard[i]['no'] > youCard[i]['no']:
#         outCard.append({'outcome':'win','shape':i['sh'],'no':i['no']})
        
    


# 패배 카드 출력


# 무승부 카드 출력



# # 내 시도
# win = 0
# lose = 0
# draw = 0

# for i in range(5):
#     for j in range(5):
#         if myCard[i["no"]]>=youCard[j["no"]]:
#             win=+1
#         elif myCard[i["no"]]==youCard[j["no"]]:
#             draw=+1
#         else:
#             lose=+1

# print(f"나의 점수- 승리 {win}회 / 패배 {lose}회 / 무승부 {draw}회")
            
            



# 11-J, 12-Q, 13-K, 1-A
# 카드 출력
# for c in cList:
#     print(c['shape'],c['no'])

# import math
# import random

# # 0.0000000000000000 <= x 1.0000000000000000
# print(random.random())

# # 1 - 45
# print(random.randint(1,45))

# # 리스트에서 1개 랜덤추출
# a_list = [1,2,3,4,5]
# print(random.choice(a_list))

# # 리스트에서 개수만큼 랜덤 추출 - 중복없이
# print(random.sample(a_list,2))

# # 리스트를 랜덤으로 섞기 - 리스트 순서를 랜덤으로 섞기
# random.shuffle(a_list)
# print(a_list)

# a = 3.141592
# b = 3.51582

# # a에서 소수점 3자리에서 ceil올림해서 2자리까지 표시해서 출력하시오.
# print(math.ceil(a*100)/100)  # 3.15

# # b에서 소수점 5자리에서 ceil올림해서 4자리까지 표시해서 출력하시오.
# print(math.ceil(b*10**4)/10**4)  # 3.5159

# # math 안에 있는 함수를 출력
# print(dir(math))
# print(math.pi)





# # 올림
# print(math.ceil(a))  # 4
# # 반올림
# print(round(a))   # 3
# print(round(b,3))   # 3자리까지 표시, 3.516
# print(round(a,4))   # 4자리까지 표시, 3.1416
# # 버림
# print(math.floor(b))  # 3