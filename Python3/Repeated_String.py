s = input().strip()
n = int(input())
print(s)

ta = ((n // len(s)) * s.count('a')) + s[ : (n % len(s)) ].count('a')
print(ta)
