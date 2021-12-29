from itertools import combinations


def main():
    n = int(input())
    letters = list(input().split())
    k = int(input())
    comb = list(combinations(''.join(letters), k))
    a = 0
    for v in comb:
        if 'a' in v:
            a += 1
    print(round(a/len(comb), 4))


if __name__ == '__main__':
    main()
