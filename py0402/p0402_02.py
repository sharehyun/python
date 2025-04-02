# 문자열

print('1234'.isdigit())    # 정수인지 확인
print('1234'.isalpha())    # 알파벳인지 확인 - 한글안됨
print('abc123'.isalnum())  # 모두 숫자인지 확인 - abc,a1,123 모두 가능
print('abc'.islower())     # 모두 소문자인지 확인
print('ABC'.isupper())     # 모두 대문자인지 확인

# a = "1234"
# if a.isdigit():  # 숫자로 변환가능
#     print("숫자로 변환 가능합니다.")

# my = int(input("숫자를 입력하세요.>> "))
  
# while True:
#     my_input = input("숫자를 입력하세요.>> ")
#     if my_input.isdigit():
#         my_input = int(my_input)
#     else:
#         print("숫자가 아닙니다. 숫자를 입력해 주세요.")


# map(함수, 데이터값)
# score = ['100','99','90']
# # 함수
# def cal(x):
#     return int(x)*100

# s_list = list(map(cal,score))
# print(s_list)

# sum = 0
# for s in score:
#     sum += int(s)   # 형변환 str->int
# print("합계 :",sum)

# txt = ","
# txt2 = txt.join("안녕")
# print(txt2)  # 안,녕


# # 데이터베이스(DB)는 리스트를 저장할 수 없음.
# # 문자열
# txt = "1,홍길동,100,100,100,300,100.0,1"
# txt_list = txt.split(",")
# print(txt_list)
# txt_list[1] = '유관순'
# print(txt_list)

# API
# CSV : 텍스트파일 형식(comma seperated values)
# Json
# XML(데이터의 타입 표준-가독성low, 용량도 크기 때문에 Json으로 바뀜) 참고:html

# txt = "a,b,c,d,안녕,반가워"
# print(txt.split(","))
# txt_list = txt.split(",")
# print(txt_list)

# txt = "  안녕하   세요    "
# print(txt.replace(" ",""))  # 문자를 다른 문자로 치환

# txt2 = "파이썬 공부가 쉬워요~ 너무 쉬워요. 파이썬은 재미있어요."
# print(txt2.replace("파이썬","자바"))

# txt3 = "----파---이썬----"
# print(txt3.strip("-"))  # 특정글자제거
# print(txt3.replace("-",""))


# print(txt)
# # 공백제거
# print(txt.strip())  # 앞뒤공백제거 / 오른쪽공백제거: rstrip() / 왼쪽공백제거: lstrip()

# txt = "파이썬 공부가 쉬워요! 너무 쉬워요. 파이썬은 재미있어요."
# print(txt.count("파이썬"))  # 문자열의 검색하려고 하는 글자 개수
# print(txt.count("요"))      
# print(txt.find("공부"))  # 있을때 index번호
# print(txt.find("자바"))  # 없을때 -1

# t = "aaa.py"
# print(t.endswith("py"))  # 있으면 True, 없으면 False


# txt = "abBBcDd heool apple"     # 대소문자
# print(txt.upper())  # 대문자로 출력
# print(txt.lower())  # 소문자
# print(txt.swapcase())  # 대문자는 소문자로, 소문자는 대문자로
# print(txt.title())     # 단어 첫 글자를 대문자로 바꿔줌

# txt = "안녕하세요"
# a_list = [1,2,3,4,5]

# print(a_list[1:3])  # 2,3
# print(txt[1:3])     # 녕하
# print(txt[2:])      # 하세요
# print(txt[:3])      # 안녕하

# print(txt*3)
# print("-"*50)
# print(len(txt))  # 글자 길이

# print(txt[::-1])  # 글자역순출력



# 문자열도 index 번호를 가짐
# print(txt[1])
# print(a_list[1])