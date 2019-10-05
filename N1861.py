import sys
sys.stdin = open('input.txt', 'r')

def bfs(x, y, n):
    global cnt

    for k in range(4):
        ni = x + di[k]
        nj = y + dj[k]
        if 0 <= ni < N and 0 <= nj < N:
            if a[ni][nj] == n+1:
                cnt += 1
                bfs(ni, nj, n+1)

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = [list(map(int, input().split())) for i in range(N)]
    maxV = 0
    minV = 10000000000000
    for i in range(N):
        for j in range(N):
            cnt = 1
            bfs(i, j, a[i][j])
            if maxV < cnt:
                maxV = cnt
                minV = a[i][j]
            elif maxV == cnt:
                maxV = cnt
                if a[i][j] <= minV and cnt > 1:
                    minV = a[i][j]


    print('#{} {} {}'.format(tc, minV, maxV))