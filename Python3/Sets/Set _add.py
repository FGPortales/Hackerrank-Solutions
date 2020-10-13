import sys
# example: set.add()
'''
s = set('Hackerrank')
print(s)
s.add('H')
print(s.add('a'))
print(s)
'''



N = int(input())
se = set()
for v in range(N):
    se.add(input())
print(len(se))
