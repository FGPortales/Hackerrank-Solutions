def permutations(x,y,z):
    arr = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                arr.append([i,j,k])
    return arr

def not_sum(arr,n):
    aux = []
    for v in arr:
        if sum(v) != n:
            aux.append(v)
    return aux

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print(not_sum(permutations(x,y,z),n))

# OTRO CODIGO DE HACKERRANCK

# X = int(raw_input())
# Y = int(raw_input())
# Z = int(raw_input())
# N = int(raw_input())
# lis = [[x, y, z] for x in range(X+1) for y in range(Y+1) for z in range(Z+1) if x + y + z != N]
# print lis