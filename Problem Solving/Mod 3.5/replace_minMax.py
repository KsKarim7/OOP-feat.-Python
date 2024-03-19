n = int(input())
lst = list(map(int, input().split()))

# lst = [4,1,3,10,8]

mx = max(lst)
# print(mx)
mn = min(lst)
idx = lst.index(mn)
idxx = lst.index(mx)

lst[idx] = mx
lst[idxx] = mn

for i in lst:
    print(i,end=" ")