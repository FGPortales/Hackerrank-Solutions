from itertools import product

list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

for value in list(product(list_a, list_b)):
    print(value, end=' ')
