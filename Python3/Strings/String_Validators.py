if __name__ == '__main__':
    string = input()
    b1,b2,b3,b4,b5 = 0,0,0,0,0
    alnum,alpha,digit,lower,upper = False,False,False,False,False
    for v in string:
        if v.isalnum() and b1 == 0:
            alnum = True
            b1 = 1
        if v.isalpha() and b2 == 0:
            alpha = True
            b2 = 1
        if v.isdigit() and b3 == 0:
            digit = True
            b3 = 1
        if v.islower() and b4 == 0:
            lower = True
            b4 = 1
        if v.isupper() and b5 == 0:
            upper = True
            b5 = 1
print(alnum)
print(alpha)
print(digit)
print(lower)
print(upper)

