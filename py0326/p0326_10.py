print(" ∧＿∧\n(　-ω- ) 후우〜\n( つ旦O\nと＿)_)")
print("-"*50)
print("\n두다다다다다다다\n두다다다다다다다\n　(∩`・ω・)\n＿/_ミつ/￣￣￣/\n　　＼/＿＿＿/")
print("-"*50)

num1 = int(input("첫 번째 숫자를 입력하시오 : "))
num2 = int(input("두 번째 숫자를 입력하시오 : "))

add_print = f"{num1} + {num2} = {num1+num2}"
sub_print = f"{num1} - {num2} = {num1-num2}"
mul_print = f"{num1} * {num2} = {num1*num2}"
div_print = f"{num1} / {num2} = {num1/num2:.0f}"

print(add_print)
print(sub_print)
print(mul_print)
print(div_print)
print("-"*50)

name = input("이름을 입력하시오 : ")
kor = int(input("1. 국어 점수를 입력하시오 : "))
eng = int(input("2. 영어 점수를 입력하시오 : "))
math = int(input("3. 수학 점수를 입력하시오 : "))

total = kor+eng+math

total_score = f"과목 합계 : {(total)}"
avg_score = "과목 평균 : {:.0f}".format(total/3)

print("이름 :", name)
print(total_score)
print(avg_score)

