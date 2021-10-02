
def minion_game(word):
    word_vowel = 0
    word_conso = 0
    size = len(word)
    for i in range(size):
        if word[i] in ['A', 'E', 'I', 'O', 'U']:
            word_vowel += (size-i)
        else:
            word_conso += (size-i)

    if word_conso > word_vowel:
        print('Stuart {}'.format(word_conso))
    elif word_vowel > word_conso:
        print('Kevin {}'.format(word_vowel))
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)
