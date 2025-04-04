# with함수 사용시 f.close() 생략
# 모든 학생 영어점수 +1

# stu.txt -> 영어성적을 +1, 합계도 +1
# 전체리스트를 출력
# 1,홍길동,100,99,199
# 2,유관순,90,90,180
# 3,이순신,80,81,161

# [성적출력]
# 1,홍길동,100,99,199
# 2,유관순,90,90,180
# 3,이순신,80,81,161

students = []

f = open("py0404/stu.txt","r",encoding="utf-8")
while True:
    line = f.readline()
    if not line : break
    print (line.strip())
    s = line.strip().split(",")
    print("영어 :",int(s[3])+1)
    print("합계 :",int(s[4])+1)
    students.append({"no":int(s[0]),"name":s[1],"kor":int(s[2]),"eng":int(s[3])+1,"total":int(s[4])+1})
    print("{},{},{},{},{}".format(*s))
    students.append(s)
f.close()



# f = open("py0404/stu2.txt","r",encoding="utf-8")
# line = f.readline()
# a_list = line.strip().split(",")   # list타입으로 변경해서 전달
# print(a_list)
# print(int(a_list[3])+1)

# students = []


# f.close


# aStr = "1,홍길동,100,99,199"
# a_list = aStr.split(",")   # list타입으로 변경해서 전달
# print(a_list)
# print(int(a_list[3])+1)

# with open("py0404/stu.txt","r",encoding="utf-8") as f:
#     for line in f:
#         print(line.strip())
        