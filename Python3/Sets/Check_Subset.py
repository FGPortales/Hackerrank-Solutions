def main():
    t = int(input())
    for _ in range(t):
        n1 = int(input())
        set1 = set(map(int, input().split()))
        n2 = int(input())
        set2 = set(map(int, input().split()))
        print(True) if set1 <= set2 else print(False)


if __name__ == '__main__':
    main()
