from itertools import permutations

*s , k = map(str, input().split())

for value in sorted(list(permutations(''.join(s), int(k)))):
    print(''.join(value))