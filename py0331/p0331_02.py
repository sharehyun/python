# 삭제 del, pop, remove, clear
a_list = [1,2,3,4,5]
del a_list[2] # 위치값 삭제
print(a_list)

a_list.pop()  # 맨뒤 삭제, 특정위치 삭제
print(a_list)

a_list.remove(1)  # 데이터값으로 삭제
print(a_list)

a_list.clear()   # 전체삭제
print(a_list)


# 리스트는 주로 대량의 데이터를 전달, 작업값이 많아 insert는 자주 사용하지 X
# 프로그램은 항상 효율성을 중시해야...
# 리스트추가 : append,insert,extend
# a_list = [1,2,3]
# a_list.append(4)
# print(a_list)
# a_list.insert(1,100) # 특정 위치에 값을 추가 - 1 위치에 100을 삽입
# print(a_list)
# a_list.extend([100,200,300]) # 리스트를 추가
# print(a_list)

# 리스트 내포 (더 빠름)
# a_list = [i for i in range(1,10+1)]
# print(a_list)


# 리스트 - append 추가방법
# a_list = []
# for i in range(1,10+1):
#     a_list.append(i)
# print(a_list)


# index 번호를 넣으려먼 enumerate를 사용
# a_list = [273,10,5,9,100,1000,50]
# for idx,value in enumerate (a_list):
#     print(f"{idx+1} : {value}")