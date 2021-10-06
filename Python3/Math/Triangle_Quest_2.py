
def main():
    # n = int(input())
    # c = 0
    # for i in range(1, n*2, 2):
    #     part1 = list(map(str, range(1, i-c+1)))
    #     part2 = part1 + part1[-2::-1]
    #     print(''.join(part2))
    #     c += 1

    for i in range(1, int(input()) + 1):  # More than 2 lines will result in 0 score. Do not leave a blank line also
        print(pow(int((pow(10, i)-1)/9), 2))


if __name__ == '__main__':
    main()
