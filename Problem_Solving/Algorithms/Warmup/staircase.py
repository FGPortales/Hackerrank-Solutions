n = int(input())
s = "{:>" + str(n) + "}"
for v in range(1, n+1):
    print(s.format('#'*v))
