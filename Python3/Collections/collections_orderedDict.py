from collections import OrderedDict


def main():
    n = int(input())
    ordered_dict = OrderedDict()
    for v in range(n):
        *item_name, net_price = input().split()
        name = ' '.join(item_name)
        value = ordered_dict.get(name, False)
        value += int(net_price)
        ordered_dict.update({name: value})

    for v in ordered_dict:
        print(v, ordered_dict[v])


if __name__ == '__main__':
    main()
