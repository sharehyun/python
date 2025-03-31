a = 10
a_list = [1,2,3,4,5]

print("a :",a)

a_list[0] = 100

print("a_list :",a_list)   # [100,2,3,4,5]

# a변수와 b변수는 다른 변수임
b = a
b = 1000
print("a :",a)  # 10
print("b :",b)  # 1000


# 새롭게 복사 : 깊은 복사 - 함수로 넘어가면 얕은복사가 편해짐
# a_list = [1,2,3,4,5]
# b_list = [*a_list]
# b_list[1] = 200

# print(a_list)  # [100,2,3,4,5]
# print(b_list)

## 주소값 복사 : 얕은복사
# # a_list, b_list 다른 리스트인가?
# a_list = [1,2,3,4,5]
# b_list = a_list  # 위치값을 저장하기 때문에 
# b_list[1] = 200

# print(a_list)  # [100,2,3,4,5]

#배열은 "객체"라는 구조로 되어 있음 
#bool int float/string list dictionary 변수는 구조가 다름
# a_list = [1,2,3,4,5] 
# sum = 0
# for i in a_list:
#     sum = sum + i
# print(sum)

# 구구단
# 2 x 1 = 2
# for i in range(2,10):  #for문 위치에 따라 어떤식으로 logic이 도는지 익히기
#     print("[ {} 단 ]".format(i))
#     for j in range(1,10):
#         print("{} x {} = {}".format(i,j,i*j))
#     print()