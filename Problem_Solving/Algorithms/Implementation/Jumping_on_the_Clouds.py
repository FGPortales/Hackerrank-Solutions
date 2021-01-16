int(input())
li = list(map(int, input().split()))
print(list)
jum = 0
s = 0
for i, v in enumerate(li):
    if li[i] == 1 or i != s:
        pass
    else:
        if i <= len(li)-3 and li[i+2] == 0:
            jum += 1
            s = i+2
        elif i <= len(li)-2 and li[i+1] == 0:
            jum += 1
            s = i+1
print(jum)
