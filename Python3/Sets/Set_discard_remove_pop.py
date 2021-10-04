
def main():
    n = int(input())
    s = set(map(int, input().split()))
    N = int(input())
    for _ in range(N):
        try:
            command, value = input().split()
            if command == 'remove':
                s.remove(int(value))
            if command == 'discard':
                s.discard(int(value))
        except ValueError:
            s.pop()
        except KeyError:
            pass
    print(sum(s))


if __name__ == '__main__':
    main()