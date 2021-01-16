
# def arrayManipulation(n, queries):
#     arr = [ 0 for v in range(n)]
#     for v in queries:
#         for x in range(v[0]-1,v[1]):
#             arr[x] = arr[x] + v[2]
#     return max(arr)
# def arrayManipulation(n, queries):
#     su = queries[0][2]
#     for x in range(len(queries)):
#         b = 0
#         for y in queries[:x]:
#             if queries[x][0] in range(y[0], y[1]+1):
#                 su_t = queries[x][2] + y[2]
#                 if su_t > su:
#                     su = su_t
#                 b = 1
#         if b == 0 and queries[x][2] > su:
#             su = queries[x][2]
#     return su
# n, m = map(int, input().split())
# queries = []
# for v in range(m):
#     queries.append(list(map(int, input().split())))
# result = arrayManipulation(n, queries)
# print(result)
