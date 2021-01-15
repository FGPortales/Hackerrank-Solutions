from itertools import combinations

*s , k = map(str, input().split())
i = 1
arr = [value for value in sorted(''.join(s))]
while(i <= int(k)):
    [print(''.join(value)) for value in list(combinations(''.join(arr), i))]
    i += 1
