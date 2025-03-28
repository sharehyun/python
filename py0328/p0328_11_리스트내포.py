arr = [i for i in range(100)]
print(arr)

# 리스트 내포 100개 값에 +100 전부 더하여 출력하시오.
# [100,101,102,103........199]
arr2 = [i+100 for i in arr]
print(arr2)
# 리스트로 받을 수 있다는 장점! 패턴이 있는 숫자를 포함한 리스트 만들기

a_list = []
for i in range(100):
    a_list.append(i)
print(a_list)

aa_list = [i for i in range(100)]  # 위 식과 동일함 앞의 i가 결과값, 뒤가 for문 (프로그래밍은 뒤에서 앞으로!)
print(aa_list)

# while문은 조건이 맞을때까지 무한루프 가능
# for문은 정해진 횟수만큼 루프 가능



# arr = [1,2,3,4,5,6,7,8,9,10]
# # arr2 = [1,23,4,5,........10]

# # 리스트 내포(for) - 리스트를 만들때 for문이 존재함
# arr2 = [i+1 for i in range(100)]
# print(arr2)
# # a_list = [1,2,3]

# aa_list = ["1m","2m","3m"]
# aaa_list = [str(i)+"m" for i in aa_list]
# print (aaa_list)


# arr3 = [str(i)+"cm" for i in arr2]
# print (arr3)

# arr3_list = []
# for i in arr2:
#     arr3_list.append(str(i)+"cm")

# print(arr3_list)