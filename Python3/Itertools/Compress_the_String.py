from itertools import groupby

my_string = input()

[print(f'({len(list(g))},{k})', end=' ') for k, g in groupby(my_string)]
    