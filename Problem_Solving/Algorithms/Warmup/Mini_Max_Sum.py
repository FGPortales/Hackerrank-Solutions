arr = list(map(int, input().split()))
sum_min = sum(arr) - max(arr)
sum_max = sum(arr) - min(arr)
print(sum_min, end=" ")
print(sum_max)
