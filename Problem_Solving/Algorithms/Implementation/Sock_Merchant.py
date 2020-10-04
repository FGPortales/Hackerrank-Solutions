from collections import Counter

l = list(map(int,input().split()))
print(Counter(l))
b = list(Counter(l).values())
np = 0
for v in b:
    np = np + v//2
print(np)

