arr = list(map(int,input().split()))
band = 0
while(band == 0):
    if (arr[0]+arr[1]) == (arr[2] + arr[3]):
        print("YES")
        band = 1
    elif ((arr[0] + arr[1]) > (arr[2] + arr[3])) or arr[3] > arr[1]:
        print("NO")
        band = 1
    arr[0] = arr[0] + arr[1]
    arr[2] = arr[2] + arr[3]

