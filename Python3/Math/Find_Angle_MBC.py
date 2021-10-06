import math


def main():
    ab = int(input())
    bc = int(input())
    h = math.sqrt(ab**2 + bc**2)
    print('{}{}'.format(round(math.asin(ab/h)*180/math.pi), chr(176)))


if __name__ == '__main__':
    main()
