s, t = map(int, input().split())
a, b = map(int, input().split())
m, n = map(int, input().split())
thrown_apples = list(map(int, input().split()))
thrown_oranges = list(map(int, input().split()))
apples = 0
oranges = 0
for v in range(m):
    thrown_apples[v] = thrown_apples[v] + a
    if thrown_apples[v] >= s and thrown_apples[v] <= t:
        apples += 1
for v in range(n):
    thrown_oranges[v] = thrown_oranges[v] + b
    if thrown_oranges[v] >= s and thrown_oranges[v] <= t:
        oranges += 1

print("{}\n{}".format(apples,oranges))