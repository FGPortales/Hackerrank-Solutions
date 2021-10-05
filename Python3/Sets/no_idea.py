
def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    a = set(map(int, input().split()))
    print(len(a))
    b = set(map(int, input().split()))
    print(len(b))
    h = []
    for i in arr:
        if i in a:
            h.append(1)
        elif i in b:
            h.append(-1)
    print(sum(h))


if __name__ == '__main__':
    main()
