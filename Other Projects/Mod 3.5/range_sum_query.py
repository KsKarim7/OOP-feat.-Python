# n = list(map(int, input().split()))
n = input().split()
lst = list(map(int,input().split()))
for i in range(int(n[1])):
    s = 0
    q = list(map(int,input().split()))
    for i in range(q[0]-1,q[1]):
        s += lst[i]
    print(s)
    