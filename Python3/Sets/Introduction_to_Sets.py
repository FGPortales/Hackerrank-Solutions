
# INTRODUCTION TO SETS
'''
print(set())
print(set('Hackerranck'))
print(set([1,2,1,2,3,4,5,6,0,9,12,22,3]))
a = set((1,2,3,4,5,5))
print(a)
print(type(a))
print(set(set(['H','a','c','k','e','r','r','a','n','k'])))
b = set({'Hacker' : 'DOSHI', 'Rank' : 616 })
print(b)
for v in b:
    print(v)
l = enumerate('Hackerrank')
x = set(l)
for v in x:
    print(v)
'''

def average(array):
    array = set(array)
    return sum(array)/len(array)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)