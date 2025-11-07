# n=5
# for row in range(n,0,-1):
#     for sp in range(n-row):
#         print(' ',end=' ')
#     for st in range(1,row+1):
#         print('*',end=' ')
#     print()

n=5
space=0
star=n
for i in range(n):
    for sp in range(i):
        print(" ",end=" ")
    for st in range(n-i):
        print("*",end=" ")
    print()
    space+=1
    star=-1