
def operation(q):
    ans=0
    for x in range(len(q)):
        i = (len(q)-1)-x
        if q[i] - (i+1) > 2:
            print("Too chaotic")
            return
        for y in range(max(0,q[i]-2),i):
            if q[y] > q[i]:
                ans += 1
    print(ans)           

t = int(input())
for v in range(t):
    n = int(input())
    q = list(map(int, input().rstrip().split()))
    operation(q)