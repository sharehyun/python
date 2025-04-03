# 로또 프로그램
import random
# 6개 숫자 랜덤 번호 생성
# 6개 입력한 번호 생성
# 당첨번호 확인
# 출력


# 함수
def lotto_mix():
    global lotto,lotto2
    random.shuffle(lotto)
    lotto2 = [i+1 for i in range(45)]


lotto = [i+1 for i in range(45)]
lotto2 = [*lotto]
my_lotto = [0]*6
win_lotto = []

while True:
    print("-"*30)
    print("[ 로또 프로그램 ]")
    print("-"*30)
    print("1. 로또프로그램 재실행")
    print("2. 로또번호 입력")
    print("3. 로또번호 당첨확인")
    print("4. 로또리스트 모두 확인")
    print("5. 나의 로또번호 확인")
    print("0. 프로그램 종료")
    print("-"*30)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    print()
    
    if choice == 1:
        lotto_mix()
        print("[ 로또프로그램 재실행 ]")
    
    elif choice == 2:
        count = 0   # 카운트 0으로 초기화, 선언은 밖에 있어야 내부에서 카운트가 올라감
        while True:
            print(" "*15,end="")
            print("[ 로또번호 입력 ]")
            print("-"*50,end="")
            for i in range(45):
                if i%7 != 0:
                    print(lotto2[i],end="\t")
                else: 
                    print()
                    print(lotto2[i],end="\t")
            print()
            
            print("-"*50)
            choice = int(input("번호를 입력하세요.>> "))

            if 0>choice or 45<choice:
                print("1 이상 45 이하의 숫자를 입력해주세요.")
                
            temp = 0
            for i in lotto2:
                if i == choice:
                    temp = 1
                    lotto2[i-1] = "X"    # X표시 생성
                    my_lotto[count] = choice  # 내 로또번호 리스트에 내가 입력한 번호 추가
                    count += 1
            if temp == 0: print(f"{choice}번은 이미 입력하신 번호입니다. 다시 입력하세요.")
                
            if count >= 6:
                print("6개의 번호를 모두 입력하셨습니다.")
                print()
                my_lotto.sort()
                break

    
    elif choice == 3:
        # 로또 번호 중에 내가 입력한 번호에서 몇번이 맞았는지, 몇개가 맞았는지 확인 - win_lotto 리스트에 저장, 개수확인
        for i in lotto[:6]:    # 로또번호 i와  (6개)
            for j in my_lotto: # 내 로또번호 j (6개) 비교
                if i == j:
                    win_lotto.append(i)   # 로또번호에도 마이로또에도 있는 번호를 윈로또에 저장
                win_lotto.sort()
        
        print("[ 로또번호 당첨확인 ]")
        print("-"*30)
        print("로또 번호 :",lotto[:6])
        print("내 번호 :",my_lotto)
        print("맞춘 번호 :",win_lotto)
        print("맞춘 개수 :",len(win_lotto))
                    
                
    elif choice == 4:
        print("[ 로또리스트 모두 확인 ]")
        print("로또번호 :",lotto)
        
    elif choice == 5:
        print("[ 나의 로또번호 확인 ]")
        print("나의 로또번호 :",my_lotto)

    else:
        print("[ 프로그램 종료 ]")
        break