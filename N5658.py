import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    num = input()
    base = []

    for i in range(N//4):
        for j in range(4):
            temp = num[(N//4)*j:(N//4)*(j+1)]
            if temp not in base:
                base.append(temp)
        num = '' + num[-1] + num[:-1]

    base.sort()
    base.reverse()
    res = 0
    for i in range(len(base[K-1])):
        if 48 <= ord(base[K-1][i]) <= 57:
            res += (ord(base[K-1][i]) - 48) * (16**(len(base[K-1])-1-i))
        else:
            res += (ord(base[K-1][i]) - 55) * (16**(len(base[K-1])-1-i))
    print('#{} {}'.format(tc, res))
