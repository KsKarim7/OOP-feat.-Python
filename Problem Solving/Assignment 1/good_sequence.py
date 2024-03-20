dictt= {}
n = int(input())
lst = lst = list(map(int,input().split()))
for i in lst:
    if(i not in dictt):
        dictt[i] = 1
    else:
        dictt[i] += 1
ans =0
for k,c in dictt.items():
    if( k != c):
        if(k < c):
            ans += c - k
        elif(k>c):
            ans+= c

print(ans)

# for k,c in dictt.items():
#     print(f"{k}: {c}")
