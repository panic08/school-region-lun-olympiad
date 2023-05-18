s1 = int(input())
higher = float('-inf') 
smallest = float('inf')
while s1 != 0:
    temp = float(input())
    if temp > higher:
        higher = temp
    if temp < smallest:
        smallest = temp
    s1 -= 1
print(int(higher - smallest))
