fruits = ['사과','배','딸기','바나나','멜론']

# enumerate index 번호를 받을 수 있음
for i,fruit in enumerate(fruits):
    if len(fruits)-1 != i:
        print("{}. {}".format(i+1,fruit),end=", ")
    else: 
        print("{}. {}".format(i+1,fruit))


# scores = [65,90,100,100,50]
# for score in scores:
#     print(score,end=" ")