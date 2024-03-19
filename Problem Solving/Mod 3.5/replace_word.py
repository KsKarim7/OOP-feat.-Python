# s = input()
s = "BRITISHEGYPTGHANA"
# lst = s.split("EGYPT")
# print(s[2:7])
k = 0
ss = " "
for i in range(len(s)):
    if(k+5 < len(s)):
        if(s[k:k+5] == "EGYPT"):
            k+=6
            ss+=" "
        else:
            ss += s[k]
            k+=1
    if(k<len(s)):  
            ss += s[k]
            k+=1
print(ss)