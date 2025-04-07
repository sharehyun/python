from stuModule import *
from stuFunc import *   # 함수, 변수 모두 다 가져옴


while True:
    choice = tmenu_print()   # 상단메뉴부분
    if choice == 1:
        stu_input()   # 학생성적입력 함수
    elif choice == 2:
        stu_output()
    elif choice == 3:
        pass