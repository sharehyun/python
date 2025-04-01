# zip() - 2개 리스트를 합치는 것 -> list, dict타입 변경 가능
n_list = ['홍길동','유관순','이순신','강감찬','김구']
t_list = [100,99,89,79,100]     #[]는 리스트 {}는 딕셔너리 ()는 튜플 - 리스트,딕셔너리는 수정O / 튜플 값은 수정X  튜플 == 리스트
a_list = [10.0,9.0,8.0,7.0,10.0]
print(list(zip(n_list,t_list)))    # 2개 이상의 리스트를 통합하는 것 가능
print(dict(zip(n_list,t_list)))    # 딕셔너리는 key값과 value값이 하나씩 있어야 해서 2개만 가능

# LIFO(Last In Last Out요즘 많이쓰는것) - 스택 : 나중에 들어온 것이 처음으로 나감(recent files)
# FIFO(First In First Out) : 처음 들어온 것이 처음으로 나감





# tuple_list = list(zip(n_list,t_list))


# students = {"no": 1,"name": "홍길동","kor": 100}
# for key,value in students.items():
#     print(f"{key} : {value}")

# for key,value in enumerate(students):   # enumerate는 인덱스값을 가져오는거기 때문에 꼭 items로 받아야 함
#     print(f"{key} : {value}")

# # 2개의 리스트를 출력할 수 있음
# n_list = ['홍길동','유관순','이순신','강감찬','김구']
# t_list = [100,99,89,79,100]
# for n,t in zip(n_list,t_list):
#     print(f"{n} : {t}")


# # 리스트 내포 : if조건절을 넣을 수 있음(한 줄만)
# n_list = [i for i in range(1,51) if i%3==0]
# print(n_list)


# # 
# list = [1,2,3,4,5]
# # list +100*100
# # list2 = ['10,100', '10,200', '10,300', '10,400', '10,500']

# # 천단위 표시
# list2 = ["{:,d}".format((i+100)*100) for i in list]   # 암기하세요~ ㅎㅎ 좌표맞추기, 성적입력프로그램 은 외워야함
# print(list2)

# # list2 = [i*100 for i in list]   #리스트 내포, 리스트에 특정한 값을 더하거나 곱하더나 빼거나... 뒤에서 많이 씀
# # print(list2)


#-------------------------------------------------
# # set -> 중복을 제거해서 키를 확인
# myset1 = {1,2,2,3,3,3,5,5,7}
# print(myset1)

# menu_list = ['삼각김밥','바나나','삼각김밥','사과','바나나','도시락','삼각김밥']
# print(set(menu_list))  # list타입을 set타입으로 변경해서 확인 - 종류만 확인