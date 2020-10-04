n = int(input())

l = list(map(int,input().split()))
t = tuple(l)
print(hash(t))