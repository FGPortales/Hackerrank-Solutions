

# arr = []
# m = 0
# for i in range(6):
#     arr.append(list(map(int,input().split())))

# print(arr)

arr = [
    [-9, -9, -9, 1, 1, 1],
    [0, -9, 0, 4, 3, 2],
    [-9, -9, -9, 1, 2, 3],
    [0, 0, 8, 6, 6, 0],
    [0, 0, 0, -2, 0, 0],
    [0, 0, 1, 2, 4, 0]]

# arr = [ [ 0,-4,-6, 0,-7,-6],
#         [-1,-2,-6,-8,-3,-1],
#         [-8,-4,-2,-8,-8,-6],
#         [-3,-1,-2,-5,-7,-4],
#         [-3,-5,-3,-6,-6,-6],
#         [-3,-6, 0,-8,-6,-7]]

m = -64
for i in range(6):
    if i >= 4:
        pass
    else:
        for j in range(6):
            if j >= 4:
                pass
            else:
                s = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] +\
                 arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
                if s > m:
                    m = s

print(m)
# for i,e in enumerate(arr):
#     if i > 3 and i < 6:
#         pass
#     elif:
#         s = s + arr[i] + arr[i+1] + arr[i+2] + arr[i+7]
