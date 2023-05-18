c = str(input())
s = str(input())
p = ""
p += c
for key in s:
    if (key <= c):
        c = key
        p = c + p
    else:
        p += key
print(p)