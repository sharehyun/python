# 1. sModule.py - class 2개
# 2. sMain.py - sModule.py 사용해서 프로그램구현
# 3. sFunc.py 함수를 옮겨보기

from sModule import *
from sFunc import *


while True:
    choice = tmenu_print()
    
    if choice == 1:
        stu_input()
        
    if choice == 2:
        stu_output()
    
    if choice == 3:
        print("[ 프로그램 종료 ]")
        break