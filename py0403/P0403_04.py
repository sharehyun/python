# 로또 프로그램
import random
# 6개 숫자 랜덤 번호 생성
# 6개 입력한 번호 생성
# 당첨번호 확인
# 출력
my_lotto = [0]*6  # 입력 후 번호 담기
win_lotto = []
lotto = [i+1 for i in range(45)] # 로또 랜덤번호
lotto2 = [*lotto]  # 로또 순차적번호 출력

def lotto_mix():
    global lotto, lotto2
    random.shuffle(lotto)
    lotto2 = [i+1 for i in range(45)]

lotto_mix()
while True:
    print()
    print("[ 로또 프로그램 ]")
    print("-"*30)
    print("1. 로또프로그램 재실행")
    print("2. 로또번호 입력")
    print("3. 로또번호 당첨확인")
    print("4. 로또리스트 모두 확인")
    print("5. 내가 입력한 로또번호 확인")
    print("0. 프로그램 종료")
    print("-"*30)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    print()
    
    if choice == 1:
        lotto_mix()
    
    elif choice == 2:
        count = 0  # 로또번호 입력 개수
        lotto2 = [i+1 for i in range(45)]  # 재입력시 초기화
        while True:
            print(" "*15,end="")
            print("[ 로또번호입력 ]")
            print("-"*50)
            # 로또번호 순번출력부분--------------
            for i in range(45):
                if i%7 == 0: 
                    if i != 0:  # 맨처음 엔터 제거용
                        print()
                print(lotto2[i],end="\t")

            print()
            # 번호 입력
            print("-"*50)
            choice = int(input("로또번호를 입력하세요.(0. 이전화면 이동)>> "))
            if choice == 0:
                print("이전화면으로 이동합니다.")
                print()
                break

            # 해당로또번호 X표시부분 검증
            if choice<0 or choice>45:
                print(f"{choice}번 번호는 없는 번호입니다. 다시 확인해주세요.")
            temp = 0
            
            # 나의 로또번호 리스트에 입력
            for i in lotto2:
                if i == choice: 
                    lotto2[i-1] = "X"
                    my_lotto[count] = choice  # append보다 속도가 빠름. (== my_lotto.append(count))
                    count += 1  # 입력로또번호개수 1 증가
                    temp = 1    # 로또번호 존재확인변수
            if temp == 0: print(f"{choice}번은 이미 입력하신 번호입니다. 다시 입력하세요.")

            if count >= 6:
                print("로또 번호 6개를 모두 입력하셨습니다.")
                break

    elif choice == 3:
        # 로또당첨확인
        for i in lotto[:6]:
            for j in my_lotto:
                if i == j: win_lotto.append(i)
        win_lotto.sort()
                
        # 출력
        print("[ 로또당첨번호 확인 ]")
        print("-"*50)
        print("로또당첨번호 :",lotto[:6])
        print("내 로또번호 :",my_lotto)
        print("당첨된 로또번호 :",win_lotto)
        print("당첨개수 :",len(win_lotto))
    
    elif choice == 4:
        print("[ 로또리스트 모두 확인 ]")
        print(lotto)

    
    elif choice == 5:
        print("[ 나의 로또번호 확인 ]")
        my_lotto.sort()
        print(f"입력 번호 : {my_lotto}")  # reverse=True : 역순정렬

    
    else:
        print("[ 프로그램 종료 ]")
        break

