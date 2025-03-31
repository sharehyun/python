# x좌표 : 1
# y좌표 : 3
# x,y좌표를 한꺼번에 넣고싶음... 1,3 -> 문자로 인식

# num1 = int(input("X좌표 : "))
# num2 = int(input("Y좌표 : "))

# print(f"[X,Y좌표 : {num1},{num2}]")

num = input("X,Y좌표 (0,0) : ")    # 1,3,5,7
n_list = num.split(",")            # 1 따로, 3 따로 리스트로 저장   # CSV 파일은 ","로 분리되어 split 활용 가능
print(f"[X,Y좌표 : {n_list}]")
