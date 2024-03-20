inp = input()
res = l = 0
left = right = ""
lst = []
for s in inp:
    if(s == "L"):
        l+=1
        left+= s
    else:
        l-=1
        right += s
    if(l==0):
        res+=1
        lst.append(left+right)
        left = right = ""

print(res)
for i in lst:
    print(f"{i}")