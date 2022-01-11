from collections import deque


def main():
    # d = deque()
    # d.append(1)
    # print(d)
    # d.appendleft(2)
    # print(d)
    # d.append(3)
    # print(d)
    # d.clear()
    # print(d)
    # d.extend('12')
    # print(d)
    # d.clear()
    # print(d)
    # d.extend('1')
    # print(d)
    # d.extend('234')
    # print(d)
    # d.extendleft('678')
    # print(d)
    # n = int(input())
    d = deque()
    for _ in range(int(input())):
        method, *value = input().split()
        if method == 'append':
            d.append(int(value[0]))
        elif method == 'appendleft':
            d.appendleft(int(value[0]))
        elif method == 'popleft':
            d.popleft()
        elif method == 'pop':
            d.pop()
    for v in d:
        print(v, end=' ')


if __name__ == '__main__':
    main()
