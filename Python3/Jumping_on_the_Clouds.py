int(input())
l = list(map(int,input().split()))
print(l)
jum = 0
s = 0
for i,v in enumerate(l):
    if l[i] == 1 or i != s:
        pass
    else:
        if i <= len(l)-3 and l[i+2] == 0:
            jum += 1
            s = i+2
        elif i <= len(l)-2 and l[i+1] == 0:
            jum += 1
            s = i+1
print(jum)


    

