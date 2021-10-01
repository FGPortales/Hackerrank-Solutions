from collections import Counter
from collections import defaultdict


def main():
    n = input()
    arr = list(map(int, input().split()))
    customers = int(input())
    d = defaultdict(list)
    counter = Counter(arr)
    for v in range(customers):
        s, p = map(int, input().split())
        if counter.get(s, 0) > 0 and counter.get(s) > len(d[s]):
            d[s].append(p)
    s = 0
    for prices in d:
        s = s + sum(d[prices])
    print(s)


if __name__ == '__main__':
    main()
