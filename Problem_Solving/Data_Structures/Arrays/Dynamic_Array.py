
lastAnswer = 0
arr = []

def xor_operation(a,b):
    if a ^ b >= 1:
        res = 1
    else:
        res = 0
    return res

n, q = map(int, input().split())


for v in range(n):
    arr.append([])

for v in range(q):
    queries = list(map(int, input().split()))
    ec = (xor_operation(queries[1], lastAnswer))%n
    if queries[0] == 2:
        lastAnswer = arr[ec][queries[2]%len(arr[ec])]
        print(lastAnswer)
    else:
        arr[ec].append(queries[2])