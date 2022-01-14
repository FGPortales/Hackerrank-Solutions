from collections import OrderedDict, Counter


class OrderedCounter(Counter, OrderedDict):
    pass


if __name__ == '__main__':
    s = input()
    [print(*v) for v in OrderedCounter(sorted(s)).most_common(3)]
