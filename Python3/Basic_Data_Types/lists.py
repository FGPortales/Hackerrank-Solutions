'''
    Consider a list (list = []). You can perform the following commands:

    1. insert i e: Insert integer  at position .
    2. print: Print the list.
    3. remove e: Delete the first occurrence of integer .
    4. append e: Insert integer  at the end of the list.
    5. sort: Sort the list.
    6. pop: Pop the last element from the list.
    7. reverse: Reverse the list.
'''

N = int(input())
arr = []
for v in range(N):
    command , *value = input().split()
    value = [int(x) for x in value]
    if command == 'insert':
        arr.insert(value[0], value[1])
    elif command == 'print':
        print(arr)
    elif command == 'remove':
        arr.remove(value[0])
    elif command == 'append':
        arr.append(value[0])
    elif command == 'sort':
        arr.sort()
    elif command == 'pop':
        arr.pop()
    elif command == 'reverse':
        arr.reverse()

