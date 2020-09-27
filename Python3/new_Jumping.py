n = int(input().strip())
c = [ int(c_temp) for c_temp in input().strip().split(' ')]
dp = []
dp.append(0)
dp.append(n + 1 if c[1] else 1)
for i in range(2,n):
    print(dp,'**')
    dp.append(n + 1 if c[i] else min(dp[-1]+1, dp[-2]+1))
    print(dp,'$$')
    print()
print(dp[-1])
print(dp)
