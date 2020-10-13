import string
def print_rangoli(size):
    al = string.ascii_lowercase   
    c1 = 1
    arr = []
    for x in range(size*2-1):
        s1 = al[size-1]
        if x < size:
            for y in range(1,c1):
                if y < (c1//2 + 1):
                    i = (size-1)-y
                    s1 = s1 + '-' + al[i]
                else:
                    i = i + 1
                    s1 = s1 + '-' + al[i]
            c1 += 2
            print(s1.center((size*2-1)+(size*2-2),'-'))
            arr.append(s1.center((size*2-1)+(size*2-2),'-'))
    for v in range(2,len(arr)+1):
        print(arr[-v])
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
