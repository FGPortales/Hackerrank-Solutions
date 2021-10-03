
def merge_the_tools(word, k):
    for i in range(0, len(word), k):
        print(''.join(sorted(set(word[i:i+k]), key=word[i:i+k].index)))


if __name__ == '__main__':
    word, k = input(), int(input())
    merge_the_tools(word, k)
