di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def dfs(si, sj):
    global res
    visited[si][sj] = 1
    for i in range(4):
        ni = si + di[i]
        nj = sj + dj[i]
        if 0 <= ni <= N - 1 and 0 <= nj <= N - 1 and cross[ni][nj] != 1 and visited[ni][nj] == 0:
            if cross[ni][nj] == 3:
                res = 1
                return
            dfs(ni, nj)

for tc in range(int(input())):
    N = int(input())
    cross = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    res = 0
    for i in range(N):
        a = 0
        for j in range(N):
            if cross[i][j] == 2:
                a = 1
                startx, starty = i, j
                break
        if a == 1:
            break
    dfs(startx, starty)
    print('#{} {}'.format(tc+1, res))
