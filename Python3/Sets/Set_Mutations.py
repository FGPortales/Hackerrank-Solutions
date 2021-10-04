
def main():
    n = input()
    A = set(map(int, input().split()))
    N = int(input())
    for _ in range(N):
        op, size = input().split()
        elements = set(map(int, input().split()))
        operation = '{}({})'.format(op, elements)
        exec('A.{}'.format(operation))
    print(sum(A))


if __name__ == '__main__':
    main()
