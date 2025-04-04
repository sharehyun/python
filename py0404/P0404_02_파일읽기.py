# 파일입출력 : 파일 열기 - 파일읽기, 파일쓰기 - 파일닫기
# 파일열기 - 3가지모드 r:읽기모드, w:쓰기모드, a:추가모드, b: 이진파일-파일복사
# f = open("a.txt","r") # 읽기모드
# f = open("a.txt","w") # 쓰기모드
# f = open("a.txt","a") # 추가모드

# news.txt 파일 출력하시오.
f = open("py0404/news.txt","r",encoding="utf-8")
for line in f:
    print(line.strip())
f.close()


# 파일읽어오기 - 절대경로
# f = open("C:/workspace/python/a.txt",'r',encoding='utf-8')  # 경로 사이에는 /를 넣거나 \\를 넣거나...
# f = open("py0404/b.txt",encoding="utf-8")   # 폴더안에 있는 파일읽어오기
# for line in f:
#     print(line.strip())
# f.close()    # 읽기가 끝나면 꼭 close를 넣어줘야 함

# while True:  # 3줄
#     line = f.readline()
#     if not line: break  # 라인 안에 아무 데이터가 없다면 빠져나와라
#     print(line.strip())
# f.close


# # 파일읽기 - readlines(): 모두 읽어오기
# f = open("a.txt","r",encoding="utf-8")
# lines = f.readlines() # 모두읽어오기
# for line in lines:
#     print(line.strip())
# f.close

# # 파일읽기 - r 1줄읽기 read()
# f = open("a.txt","r",encoding="utf-8")
# print(type(f))
# # 모든 줄을 실행 - for 문을 사용
# for line in f:
#     print(line.strip())  # strip은 공백제거
# f.close()
# print("완료되었습니다.")



# 파일의 입출력
# 기존의 input - print는 콘솔 환경
# 이제 file에서 읽고 쓰기
# 읽기 - read(), readline(), readlines()
# 쓰기 - write(), writelines()

# 파일처리 3단계 : 파일 열기 - 파일 읽기 및 쓰기 - 파일 닫기

# 파일 열기 모드
