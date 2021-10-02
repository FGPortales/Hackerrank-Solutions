import re


def main():
    n = int(input())
    for _ in range(n):
        try:
            print(bool(re.compile(input())))
        except re.error:
            print(False)


if __name__ == '__main__':
    main()