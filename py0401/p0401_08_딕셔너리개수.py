list = [
        "윤소호","최재웅","전동석","황휘","윤승우",
        "윤소호","윤소호","전동석","최재웅","최재웅",
        "윤소호","전동석","윤승우","최재웅","최재웅",
        "윤소호","윤소호","윤소호","전동석","최재웅",
        "윤소호","황휘","윤소호","윤승우","황휘",
        "윤소호","윤승우","윤소호","최재웅","최재웅",
        ]


singer = {}
## 각각의 가수가 몇번 존재하는지 출력하시오.
for i in list:
    if i not in singer:
        singer[i] = 1
    else:
        singer[i] = singer[i] + 1   # singer[i] += 1


for i,v in singer.items():  # for i,v in singer.items(): ...다른 것 같은데..??
    print(f"{i} : {v}")
    

    

# list = [1,2,3,1,2,3,5,6,8,9,10,1,2]
# dic = {}

# for i in list:
#     #dic에 추가, dic 키가 존재하는지 확인
#     if i not in dic:
#         dic[i] = ""  # 0이면 숫자로 인쇄 가능
#     # dic[i] += 1     # 키가 몇개 존재하는지 개수파악
#     dic[i] += "■"

# for i,d in enumerate(dic):
#     print(f"{i} : {dic[d]}")



# # dic = {1:3,2:3,2:1,5:1,6:1,8:1,9:1,10:1}