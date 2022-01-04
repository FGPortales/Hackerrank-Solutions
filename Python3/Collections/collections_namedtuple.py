from collections import namedtuple


def main():
    # Point = namedtuple('ww', 'x,y')
    # pt1 = Point(2, 3)
    # pt2 = Point(3, 4)
    # dot_product = (pt1.x * pt2.x) + (pt1.y * pt2.y)
    # print(dot_product)
    Score = namedtuple('Score', 'ID, MARKS, NAME, CLASS')
    n = int(input())
    header = list(input().split())
    sum_score = 0
    for v in range(n):
        data = dict(zip(header, list(input().split())))
        sc = Score(**data)
        sum_score += int(sc.MARKS)
    print('{:.2f}'.format(sum_score/n))


if __name__ == '__main__':
    main()
