## 학생성적 프로그램

print("-"*50)
name = input("이름을 입력하시오.>> ")
kor = int(input("국어 점수를 입력하시오.>> "))
eng = int(input("영어 점수를 입력하시오.>> "))
math = int(input("수학 점수를 입력하시오.>> "))

total = kor+eng+math
avg = total/3

print("\n이름\t국어\t영어\t수학\t합계\t평균")
print("-"*50)
print("{}\t{}\t{}\t{}\t{}\t{:.2f}".format(name,kor,eng,math,total,avg))