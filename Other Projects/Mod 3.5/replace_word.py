s = input()

k = 0
ss = ""
while k < len(s):
    if s[k:k+5] == "EGYPT":
        ss += " "
        k += 5
    else:
        ss += s[k]
        k += 1

print(ss)