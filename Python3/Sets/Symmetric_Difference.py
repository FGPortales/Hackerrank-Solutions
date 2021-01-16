def my_function():
    int(input())
    set_m = set(input().split())
    int(input())
    set_n = set(input().split())

    total = set_m.difference(set_n).union(set_n.difference(set_m))
    total = [int(v) for v in total]
    total.sort()
    return(total)


if __name__ == '__main__':
    result = my_function()
    for v in result:
        print(v)
