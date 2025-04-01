a_list = [ [1,2,3,4,5],[6,7,8,9,10] ]
count = 0
# 숫자입력

while True:
    # 화면출력
    print(a_list)
    num = int(input("숫자를 입력하세요.>> "))
    for i in range(len(a_list)): #len(a_list) == 5
        if a_list[i] == num:
            a_list[i] = "X"
            count += 1
            break

    if count == 5:
        print("빙고 완성!!")
        print(f"완성 개수 ㅣ {count}")
        break

    print(f"현재 X개수 ㅣ {count}")