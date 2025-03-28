# 구구단 출력

for i in range(1,9+1):
    for j in range(2,9+1):
        print("{} x {} = {}".format(j,i,i*j),end="\t")
    print()

# 은행가면 001 002 003... 010 011 012...... 999
# for i in range(0,1000):
#     print("{:03d}".format(i))