sh = ["CLOVER","HEART","DIAMOND","SPADE"]
no = ["","A","2","3","4","5","6","7","8","9","10","J","Q","K"]

class Card:
    def __init__(self,sh,no,count):  # 클래스 변수 정의
        self.sh = sh
        self.no = no
        self.count = count

    def card_list(self):  # 카드 리스트 생성
        self.cards = []
        for i in range(52):
            shape = i // 13
            num = i % 13 + 1
            self.cards.append({'shape':shape,'no':num})
        
    def ran_shuffle(self):  # 카드 섞기
        import random
        random.shuffle(self.cards)
    
    def card_deal(self):   # 카드 배부
        dealtcards = self.cards[:self.count]
        self.cards = self.cards[self.count:]
        return dealtcards
    
    def card_print(self):
        mycard = self.card_deal()
        youcard = self.card_deal()
        print("[ 내 카드 ]")
        for c in mycard:
            print(f"[ {self.sh[c['shape']]}, {self.no[c['no']]} ]")
        print()    
        print("[ 상대 카드 ]")
        for c in youcard:
            print(f"[ {self.sh[c['shape']]}, {self.no[c['no']]} ]")
        print()    
        return mycard,youcard

    def card_match(self):
        mycard,youcard = self.card_print()
        score = [0]*self.count  #[2,1,2,2,0]
        for i in range(self.count):
            if mycard[i]['no'] > youcard[i]['no']:
                score[i] += 2
            elif mycard[i]['no'] < youcard[i]['no']:
                score[i] += 1
            else:
                score[i] += 0

        print(f"승리 : {score.count(2)}, 패배 : {score.count(1)}, 무승부 : {score.count(0)}")
        print()

        print("[ 승리 카드 ]")
        for i,c in enumerate(mycard):
            if score[i]==2:
                print(f"[ {self.sh[c['shape']]}, {self.no[c['no']]} ]",end=" ")

    def __str__(self):
        return f"{self.cards}"
    
        


