
def main():
    n = input()
    english_students = set(map(int, input().split()))
    b = input()
    frech_students = set(map(int, input().split()))
    print(len(english_students|frech_students))


if __name__ == '__main__':
    main()