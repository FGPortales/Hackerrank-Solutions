T = int(input())
for v in range(T):
    try:
        N = float(input())
        if(N == 0.0):
            print(False)
        else:
            print(True)
    except:
        print(False)

