while True:
    print("[ 프로그램 구현 ]")
    print("-"*20)
    print("1. 숫자맞추기")
    print("2. 로또맞추기")
    print("3. 학생성적프로그램")
    print("0. 종료")
    print("-"*20)

    choice = int(input("\n원하는 번호를 입력하세요.>> "))
    
    if choice == 1:
        print("[ 숫자맞추기 프로그램 ]")
    elif choice == 2:
        print("[ 로또맞추기 프로그램 ]")
    elif choice == 3:
        print("[ 학생성적 프로그램 ]")
    elif choice == 0:
        print("[ 프로그램 종료 ]")
        break


# 함수 사용 - 프로그램 명령 단순화, 코드를 짧게 하기 위해(반복이 많을 때, 이유 - Error 찾기가 어렵기 때문)


# while True:
#     num = int(input("숫자를 입력하세요.>> "))
#     if num==0:
#         break  # 반복문을 빠져나오는 방법 - break or 횟수의 제한

