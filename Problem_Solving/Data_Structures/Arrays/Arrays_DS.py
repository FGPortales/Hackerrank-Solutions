n = int(input())
arr = list(map(int, input().split()))
for v in range(n):
    i = (n-1)-v
    print(arr[i], end=" ")