q = list(map(int, input().split()))

a = list(int(x) for x in input().split())

for v in range(q[1]):
    e = a.pop(0)
    a.append(e)

print(*a,sep=' ') # * -> indica que puede haber más de un onjeto
# for v in a:
#     print(v,end=" ")


# OTRA SOLUCION DE HACKERRANK
# import collections
# n,k=map(int, input().split())
# arr = [int(i) for i in input().split()]
# d=collections.deque(arr)
# d.rotate(-k)
# fin = list(d)
# print(' '.join(str(i) for i in d))




