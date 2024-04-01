# inp = input()
# res = l = 0
# left = right = ""
# lst = []
# for s in inp:
#     if(s == "L"):
#         l+=1
#         left+= s
#     else:
#         l-=1
#         right += s
#     if(l==0):
#         res+=1
#         lst.append(left+right)
#         left = right = ""

# print(res)
# for i in lst:
#     print(f"{i}")

s = input()
counts = 0
substring = ''
balanced_substrings = []

for char in s:
    substring += char
    if char == 'L':
        counts += 1
    else:
        counts -= 1
    if counts == 0:
        balanced_substrings.append(substring)
        substring = ''

print(len(balanced_substrings))
for substr in balanced_substrings:
    print(substr)