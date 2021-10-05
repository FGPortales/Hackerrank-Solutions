
def main():
    a = set(map(int, input().split()))
    state = True
    for _ in range(int(input())):
        s = set(map(int, input().split()))
        state &= a.issuperset(s)
    print(state)


if __name__ == '__main__':
    main()
