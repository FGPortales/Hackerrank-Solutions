# ###################### OPTION 2 #################################
def print_formatted(n):
    line = "{x:" + str(len((bin(n))[2:])) + "d} " +  "{x:" + str(len((bin(n))[2:])) + "o} " + "{x:" + str(len((bin(n))[2:])) + "X} "+ "{x:" + str(len((bin(n))[2:])) + "b} "
    for v in range(1,n+1):
        print(line.format(x=v))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

#################### PRACTICING ################################
# line = "{0:" + str(len(bin(17))) + "d} " +  "{0:" + str(len(bin(17))) + "o} "
# print(line)
# print(line.format(1))
# print("{0:7d} {0:7o}".format(17))
# print("{n:7d} {n:7o}".format(n=17))
# for i in (1, 10, 100):
#     print('{num:02d}'.format(num=i))

# ###################### OPTION 1 ##############################3
# def check_letter(n):
#     if n == 10:
#         res = 'A'
#     elif n == 11:
#         res = 'B'
#     elif n == 12:
#         res = 'C'
#     elif n == 13:
#         res = 'D'
#     elif n == 14:
#         res = 'E'
#     elif n == 15:
#         res = 'F'
#     else:
#         res = n
#     return res


# def octal(n):
#     n = str(n)
#     if int(n) < 8:
#         res = str(n)        
#     else:
#         res = str(octal(int(n)//8)) + str(int(n)%8)
#     return res

# def hex(n):
#     n = str(n)
#     if int(n) < 16:
#         res = str(check_letter(int(n)))
#     else:
#         res = str(hex(int(n)//16)) + str(check_letter(int(n)%16))
#     return res

# def bin(n):
#     n = str(n)
#     if int(n) < 2:
#         res = str(n)
#     else:
#         res =  str(bin(int(n)//2)) + str(int(n)%2)
#     return res

# n = int(input())

# for v in range(1,n+1):
#     print(str(v).rjust(len(bin(n))), str(octal(v)).rjust(len(bin(n))), str(hex(v)).rjust(len(bin(n))), str(bin(v)).rjust(len(bin(n))))

# import sys
# stdin = sys.stdin

# n = int(stdin.readline())
# m = n
# w = 0
# while m > 0:
# 	m //= 2
# 	w += 1
# fom = "{0:" + str(w) + "d} " +"{0:" + str(w) + "o} " +"{0:" + str(w) + "X} " +"{0:" + str(w) + "b} "
# print(w,"*")
# for i in range(1,n+1):
# 	print(fom.format(i))