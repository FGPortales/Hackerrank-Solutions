from collections import defaultdict


def main():
    n, m = map(int, input().split())
    d = defaultdict(list)
    for v in range(n + m):
        if v >= n:
            var = input()
            arr = [i + 1 for i, v in enumerate(d['A']) if v == var]
            print(-1) if len(arr) == 0 else print(*arr)
        else:
            d['A'].append(input())


if __name__ == '__main__':
    main()
