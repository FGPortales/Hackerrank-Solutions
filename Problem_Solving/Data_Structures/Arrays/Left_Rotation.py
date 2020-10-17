n, d = map(int, input().split())
arr = list(map(int, input().split()))

for v in range(d):
    arr.append(arr.pop(0))
for v in arr:
    print(v,end=" ")