from itertools import product


def main():
    k, m = map(int, input().split())
    my_list = []
    for v in range(k):
        n, *element = map(int, input().split())
        my_list.append(element)
    result_list = map(lambda x: sum(n*n for n in x) % m, product(*my_list))
    print(max(result_list))


if __name__ == '__main__':
    main()
