import sys
sys.stdin = open('input.txt', 'r')

def npr(n, k, N, m):
    global res, minV

    if minV < m:
        return

    if n == k:
        minV = m
    else:
        for i in range(N):
            if used[i] == 0:
                used[i] = 1
                npr(n+1, k, N, m + matrix[n][i])
                used[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    p = [0] * N
    minV = 1000000
    npr(0, N, N, 0)
    print('#{} {}'.format(tc, minV))