import sys
sys.stdin = open('input.txt', 'r')

def go(x, y, d):
    global minV
    if minV < d:
        return
    if x == N-1 and y == N-1:
        if minV > d:
            minV = d
    for k in range(2):
        ni = x + di[k]
        nj = y + dj[k]
        if ni < N and nj < N:
            go(ni, nj, d + matrix[ni][nj])

T = int(input())
di = [1, 0]
dj = [0, 1]
for tc in range(1, T +1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    minV = 100000
    go(0, 0, matrix[0][0])
    print('#{} {}'.format(tc, minV))