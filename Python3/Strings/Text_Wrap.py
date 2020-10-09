import textwrap

S = input()
w = int(input())

print(textwrap.fill(S,w))

# My function
# def wrap(string, max_width):
#     return textwrap.fill(string, max_width)