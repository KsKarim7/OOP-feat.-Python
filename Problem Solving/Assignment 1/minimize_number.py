n = int(input())
lst = list(map(int,input().split()))
flag = True
ans = 0
while(True):
    for i,it in enumerate(lst):
        if(it % 2 == 0):
            lst[i] = it // 2
        else:
            flag = False
            break
        if(i == n-1):
            ans += 1
    if(flag == False):
        break

print(ans)