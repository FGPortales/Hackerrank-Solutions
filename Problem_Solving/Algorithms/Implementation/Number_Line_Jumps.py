def kangaroo(x1, v1, x2, v2):
    if v1 > v2 and not (x2 - x1) % (v1 - v2):
        res = 'YES'
    else:
        res = 'NO'
    return res
arr = list(map(int, input().split()))
print(kangaroo(arr[0],arr[1],arr[2],arr[3]))
