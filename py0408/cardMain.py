# 카드 프로그램 - card객체사용
cList = []
for i in range(52):
    cList.append({"shape":i//13,"no":i%13+1})
    
import random
random.shuffle(cList)



class Card:
    shapes = ["CLOVER","HEART","DIAMOND","SPADE"]  # 카드 모양 정의
    numbers = ["","A","2","3","4","5","6","7","8","9","10","J","Q","K"]  # 카드 번호 정의
    # self.shape
    # self.number
    def __init__(self,shape,number):
        self.shape = shape  # 0~3
        self.number = number # 1~13
    
    # 카드 출력 형태 __str__
    def __str__(self):
        return f"[ {Card.shapes[self.shape]}, {Card.numbers[self.number]} ]"
    
    def __gt__(self, other):  # 크기 비교용
        return self.number > other.number

    def __lt__(self, other):  # 크기 비교용
        return self.number < other.number

    def __eq__(self, other):  # 크기 비교용!
        return self.number == other.number


class CardFunc:
    
    # 카드 섞기
    def c_shuffle(self):
        myCard = []
        youCard = []
        for i in range(5):
            myCard.append(cList[i])
        for i in range(5,10):
            youCard.append(cList[i])
            
    # 카드 출력
    


# cardMain.py
# 카드리스트 호출
# 카드객체 호출 45장
# 각각 5장을 나눠준 다음, 비교해서 큰수가 승리하는 형태로 구현