# 파일 이어쓰기 - a (있는 글에서 이어쓰기)
f = open("py0404/memo2.txt","a",encoding="utf-8")
f.write("1,홍길동,100,100,99\n")
f.close()

f = open("py0404/memo2.txt","a",encoding="utf-8")
f.write("2,유관순,50,50,50\n")
f.close()




# # 파일쓰기 - w (모두삭제후 다시쓰기)
# f = open("py0404/memo.txt","w",encoding="utf-8")
# print("[ 메모장 ]")
# print("-"*15)
# print("저장하려는 글자를 입력하세요.(x.종료)")
# while True:
#     line = input("")
#     if line.lower() == "x": break
#     f.write(line+"\n")
# f.close()
# print("글쓰기 종료")

# 글자를 10번 반복해서 저장하시오.
# 안녕하세요. 
# f = open("py0404/aaa.txt","w",encoding="utf-8")
# for i in range(10):
#     f.write(f"{i+1}. 안녕하세요.\n")
# f.close()


# f = open("aa.txt","w",encoding="utf-8")   # w로 열면 파일명이 없으면 새로 만들어서 넣어줌.
# # 한글은 3byte라... 다시 처리 필요함
# # euc-kr 한국에서만 적용, utf-8은 국제 적용 cp949
# f.write("안녕하세요.\r\n")   # \r : 문장의 끝으로 이동, \n : 줄바꿈
# f.write("반가워요\n")
# f.close()