# n = int(input())

# l = list(map(str,input().split()))
# print(l)

int(input())
s = input().upper()
ns = 0  # nivel sea
cv = 0  # counter valley
for v in list(s):
    a = ns
    if v == 'D':
        ns -= 1
    elif v == 'U':
        ns += 1
    if a < 0 and ns == 0:
        cv += 1
print(cv)
