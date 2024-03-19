lst = input().split()
res = []
for i in lst:
    res.append(i[::-1])
j = 0
for i in res:
    if(j == len(res)-1):
        print(i,end="")
    else:print(i,end=" ")
    j+=1
