# 조건문 <if, if~else, if~elif~else>
# 3가지 조건
# 음수, 0, 양수

# num = int(input("숫자를 입력하세요.>> "))
# if num>0:
#     print("양수입니다.")
# elif num==0:
#     print("0입니다.")
# else:
#     print("음수입니다.")

# ## 시험성적을 입력받아 60점 이상이면 합격, 미만이면 불합격이라고 출력

# score = int(input("점수를 입력하시오.>> "))
# if score >= 60:
#     print("합격입니다.")
# else:
#     print("불합격입니다.")
    
## 70점 이상 합격, 60~69 재시험, 60미만 불합격

# score = float(input("점수를 입력하시오.>> "))
# if score >= 70:
#     print("합격입니다.")
# elif score >= 60:
#     print("재시험 응시 가능합니다.")
# else:
#     print("불합격입니다.")

# 90점이상 A, 80점이상 B, 70점이상 C, 60점이상 D, 그외 F
# 100~97 A+, 96~93 A, 92~90 A-, 89~87 B+ ...
score = int(input("점수를 입력하세요.>> "))

if score>=90:
    print("A",end="")
    if score>=97: print("+")
    elif score>=93: pass
    else: print("-")
elif score>=80:
    print("B",end="")
    if score>=87: print("+")
    elif score>=83: pass
    else: print("-")
elif score>=70:
    print("C",end="")
    if score>=77: print("+")
    elif score>=73: pass
    else: print("-")
elif score>=60:
    print("D",end="")
    if score>=67: print("+")
    elif score>=63: pass
    else: print("-")
else:
    print("F")

# print("안녕",end="") # end 옵션을 사용하면 줄바꿈을 하지 않음
# print("하세요")