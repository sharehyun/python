a = "홍길동님! 안녕하세요. 반갑습니다. 안녕 반가워. 안녕안녕"
# a.find() for,while문을 사용해서 안녕이 몇번 나오는지 개수를 출력하시오.
i = 0
count = 0
while True:
    num = a[i:].find("안녕")
    if num != -1:  # 안녕이라는 글자가 있는 경우
        count += 1 # 개수 1 증가
        i += num+1
    else: break

print("개수 :",count)        
#         print(a[i:].find("안녕"))
# print(a[0:].find("안녕"))
# print(a[0+6+1:].find("안녕"))
# print(a[0+6+1+13+1:].find("안녕"))
# print(a[0+6+1+13+1+7+1:].find("안녕"))
# print(a[0+6+1+13+1+7+1+1+1:].find("안녕"))


# num = a.count("안녕")
# print(num)


# if "안녕" in a:
#     print("안녕이라는 글자가 있습니다.")

# print(a.find("안녕"))
