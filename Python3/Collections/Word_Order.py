from collections import OrderedDict, Counter


class OderedCounter(Counter, OrderedDict):
    pass


def main():
    words = OderedCounter(input() for _ in range(int(input())))
    print(len(words))
    print(*words.values())


if __name__ == '__main__':
    main()