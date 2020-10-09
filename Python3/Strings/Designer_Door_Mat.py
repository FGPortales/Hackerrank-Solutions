N , M = map(int, input().split())

for v in range(N):
    if v == N//2:
        print('WELCOME'.center(M,'-'))
    elif v < N//2:
        print(('-'*(((N//2)-v)*3)+'.|.')+'.|.'*2*v+ ('-'*(((N//2)-v)*3)).rjust(((N//2)-v)*3))
    elif v > N//2:
        print('-'*(((N//2)-v)*-3)+'.|.' +'.|.'*((M-(((((N//2)-v)*-3)*2)+1))//3)+('-'*(((N//2)-v)*-3)).rjust(((N//2)-v)*-3))
