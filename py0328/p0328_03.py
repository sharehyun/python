# 반복문을 사용해서 1-10까지 출력
# for i in range(1,11):
#     print(i)

# a=10
# if a<9 and a>5:  # True and False 전부 연산하지 않고 앞에서 False면 뒤에 연산X
#     print(a)

# if a>5 or a<9:   # True or False  전부 연산하지 않고 앞에서 True면 뒤에 연산X
#     print(a)
    
# a_list = [1,2,3,4,5] #0번째부터 시작. 0번째==1, 4번째==5
# print(a_list[2])
# print(a_list[1:4]) # [시작위치:끝나는위치] 여러개를 한꺼번에 출력하는 것 : 슬라이싱
# print(a_list[:3])  # [:끝나는위치] 처음부터 출력
# print(a_list[2:])  # [시작위치:] 끝까지 출력
# print(a_list[::2]) # [::증가값] 2개씩 증가해서 출력
# print(a_list[::3])
# print(a_list[::-1]) # 역순으로 출력
# print(a_list[:-1])  # 제일 마지막 거 제외하고 출력

# a = "안녕하세요"  # 글자 분리해서 출력 가능, list타입과 같음
# print(a[2])
# print(a[1:4])
# print(a[:3])
# print(a[2:])
# print(a[::-1])
# print(a[:-1])
# print(a[::-2])

# print(a[:7]) # 슬라이싱은 없는 값 출력시 error 나지 않음
# # print(a[7])  # 인덱싱 없는 것 출력시 IndexError
# print(len(a_list)) # 리스트 개수 확인
# print(a_list[:len(a_list)-1])
# print(len(a))      # 문자열 길이

# a_list[1:11:2] 1부터 11-1까지 2씩 증가해 출력
# for i in range(1,11,2):
#     print(i, end=" ") # end=" " 줄바꿈 없이 출력

# break
sum = 0
i = 0
for i in range(1,100+1):
    sum = sum+i
    print("i : {} / sum : {}".format(i,sum))
    if sum>=100: break

print("sum 100이상 i값 : {}".format(i))
print("sum 100이상 sum값 : {}".format(sum))
        
# print("1-100까지 합계 : {}".format(sum))
# 합계가 100 넘는 위치의 숫자는 얼마일까요?
# 1+2+3+4+5+6+7...... 합계가 100 넘는 위치가 어디인지, 값 출력
