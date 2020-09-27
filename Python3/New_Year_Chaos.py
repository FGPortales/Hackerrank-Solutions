t = int(input())
arr = []
for i in range(t):
    
    arr.append(int(input()))
    arr.append(list(map(int, input().split())))

c = 0

for y,v in enumerate(arr):
    # print(arr," arreglo general")
    band = 0
    c_temp = 0
    if(y % 2 != 0):
        pass
    else:
        n = arr[y]
        qf = arr[y+1]
        # print(qf,"*")
        qi = list(int(x+1) for x in range(n))
        for i,v in enumerate(qf):
            if qf[i] == qi[i]:
                pass
            else:
                pi = qi.index(qf[i]) # initial position
                # print(pi,"**")
                a = pi-i
                # print(a,"--")
                if(a>2):
                    print("Too chaotic")
                    c_temp = 0
                    band = 1
                    break
                else:
                    c_temp = c_temp + (a)
                    # print(c_temp," contador temporal")
                    qi.insert(i,qi.pop(pi))
        if(band == 1):
            pass
        else:
            c = c + c_temp
            print(c)
    



# l = [2,4,6,8,10,12]

# print(l)
# l.insert(0,l.pop(2))
# print(l)


    