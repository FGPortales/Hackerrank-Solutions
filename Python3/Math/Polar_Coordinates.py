import cmath


def main():
    complex_number = input()
    print(abs(complex(complex_number)))
    print(cmath.phase(complex(complex_number)))


if __name__ == '__main__':
    main()
