students = [
    {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
    {"no":2,"name":"유관순","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
    {"no":3,"name":"이순신","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
]

# dict타입은 sort() 함수를 사용할 수 없음
# students.sort()
# print(students)

# 리스트 sort() 정렬됨
# a_list = [20,50,10,40,90]
# a_list.sort()  # 순차정렬
# print(a_list)
# a_list.sort(reverse=True)
# print(a_list)

# 람다식 lamda -> 함수 축약형
# 람다식
# lambda 매개변수:리턴값
# lambda a:a*20  


# map() 함수 : 리스트에 함수를 적용해서 다시 리스트로 반환
## 나의 정리 : map() - 여러 개의 연속값이 들어간 리스트에 함수값을 적용하여 값을 돌려줌 (입력한 리스트의 값이 변환하는 것은 아님), 파이썬의 내장 함수
# iterator == list


# filter() 함수 : 리스트에 함수를 적용해서 조건에 맞는 것만 다시 리스트로 반환
## 나의 정리 : filter() 함수 - 함수 적용했을 때 True인것만(특정 조건을 만족하는 값만) 리턴해줌. 파이썬의 내장 함수

# filter함수관련
# a_list = [1,2,3,4,5]
# aa_list = []
# for i in a_list:
#     if i%2==0:
#         aa_list.append(i)
# print(aa_list)

# # filter함수 사용
# def func(x):
#     if x%2==0:
#         return x

# b_list = list(filter(func,a_list))
# print(b_list)

# c_list = list(filter(lambda x:x%2==0,a_list))
# print(c_list)


# a_list = [1,2,3,4,5]  # list 모든 값에 제곱을 해서 리스트를 생성
# aa_list = []

# for i in a_list:
#     aa_list.append(i**2)

# def func(x):
#     return x**2

# # map(함수,리스트) - 이게 뭔가?
# print(list(map(func,a_list)))
# print(a_list)

# # 람다식 - map() 함수를 lambda로 사용하면 코드를 줄일 수 있음.
# # 파이썬에는 소스코드 축약형이 많기 때문에 사용
# print(list(map(lambda x:x**2,a_list)))






# def 함수명(매개변수) : return 값
# def func2(a):
#     return a*20


# def add(a,b):   # 함수 - 명령어의 집합체
#     return a+b

# print(add(10,20))

# def func(a,b,c):
#     return max(a,b,c)   # max(a,b,c) 값들 중 가장 큰 수를 찾아낼 때 씀

