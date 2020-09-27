arr_answer = []
# def searchChaotic(qf):
#     for x,v in enumerate(qf,n):
#         i = (n - 1) - x
#         d = abs((v-1)-i)
#         print(d,"<<<<<")
#         if d > 2:
#             return "Too chaotic"

t = int(input())


for v in range(t):
    n = int(input())
    qf = list(map(int,input().rstrip().split())) 
    #r = searchChaotic(qf,n)
    #print(r,"**")
    #if r == None:
    c = 0
    for x in range(n):
        i = (n - 1) - x
        band = 0
        mb = i+1 # numero que debe de estar en esta posicion
        #d = i - np
        if qf[i] != mb:
            np = qf.index(mb) # posicion del numero que debe estar aqui
            d = i - np
            if( d > 2 ):
                arr_answer.append("Too chaotic")
                c = 0
                band = 1
                break
            else:
                c = c + d
                qf.insert(i,qf.pop(np))
    if(band != 1):
        arr_answer.append(c)
    # else:
    #     arr_answer.append("Too chaotic")

for v in arr_answer:
    print(v)

