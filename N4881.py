import sys
sys.stdin = open('input.txt', 'r')

def find(n, s):
    global minV
    if s >= minV:
        return

    if n == N:
        if s < minV:
            minV = s
        return

    else:
        for i in range(N):
            if col[i] == 0:
                col[i] = 1
                find(n+1, s+num[n][i])
                col[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = [list(map(int, input().split())) for _ in range(N)]

    minV = 1000000000
    s = 0
    col = [0] * N
    minV = 10000

    find(0,s)

    print('#{} {}'.format(tc, minV))