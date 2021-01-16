n = int(input())
arr_string = []
for v in range(n):
    arr_string.append(input())
q = int(input())
arr_queries = []
for v in range(q):
    arr_queries.append(input())
for x in range(q):
    c = 0
    for y in range(n):
        if arr_queries[x] == arr_string[y]:
            c += 1
    print(c)

# OPTION 2
'''
n = int(input())
strs = [input() for x in range(n)]
q = int(input())
for _ in range(q):
    print(strs.count(input()))
'''
