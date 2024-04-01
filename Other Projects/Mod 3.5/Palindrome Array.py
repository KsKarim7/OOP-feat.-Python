# lst = []
# n= int(input())

# for i in range(n):
#     n = int(input())
#     lst.append(n)
n = int(input())
lst = input().split()
i = 0
m= n-1
flag = True
while(i <= n//2):
    if(lst[i] != lst[m-i]):
        flag = False
        break
    i+=1

if(flag==True):
    print("YES")
else: print("NO")