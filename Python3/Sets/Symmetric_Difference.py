
def my_function():
    int(input())
    set_m = set(map(int, input().split()))
    int(input())
    set_n = set(map(int, input().split()))
    [print(v) for v in sorted(set_m ^ set_n)]


if __name__ == '__main__':
    my_function()
