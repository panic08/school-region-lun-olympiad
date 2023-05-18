import sys
def shd(a):
    d = 0
    for key in a:
        d+=1
    return d

a = []
b = []
globals = 0
c = 0
d = 0
i = int(input())
j = int(input())
while i != 0:
    temp = int(input())
    a.append(temp)
    i-=1
while j != 0:
    temp = int(input())
    b.append(temp)
    j-=1
c = 0
if i <= j:
    for key in a:
        if key > globals:
            globals = key
    for key in b:
        if key >= globals:
            c+=1
        else:
            d+=1
    d+=1
    if c > i:
        print(shd(a))
        sys.exit()
    print(d)
else:
    print(shd(a))

            