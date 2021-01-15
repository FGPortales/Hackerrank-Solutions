from itertools import combinations_with_replacement

s , k = input().split()

[print(''.join(value)) for value in list(combinations_with_replacement(''.join(sorted(s)), int(k)))]