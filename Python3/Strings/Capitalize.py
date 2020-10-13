
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    c = ''
    for v in re.split(r" ",s):
        c = c + v.capitalize() + " "
    return c
    
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    d = solve(s)
    print(d)


# OPTION 2
'''
for v in list(map(str, input().split())):
    print(v.capitalize(), end=" ")
'''