from stuModule import Student

s1 = Student("홍길동",100,100,99)
s2 = Student("유관순",99,100,99)

print(s1)  # class 객체에서 무슨 함수를 찾는다?? __str__

if s1 >= s2:
    print("s1이 더 크거나 같습니다.")
else:
    print("s1이 작습니다.")

# 변수의 if문 비교
a = 10
b = 20

if a>b:
    print("a가 큽니다.")
else:
    print("a가 작습니다.")
