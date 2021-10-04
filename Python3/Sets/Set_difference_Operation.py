
def main():
    n = input()
    english = set(map(int, input().split()))
    b = input()
    french = set(map(int, input().split()))
    print(len(english - french))


if __name__ == '__main__':
    main()
