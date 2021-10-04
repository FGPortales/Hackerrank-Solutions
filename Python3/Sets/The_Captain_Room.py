
def main():
    k = int(input())
    numbers = list(map(int, input().split()))
    unique_numbers = set(numbers)
    print((sum(unique_numbers)*k - sum(numbers))//(k-1))


if __name__ == '__main__':
    main()
