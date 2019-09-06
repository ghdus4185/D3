import sys
sys.stdin = open('input.txt', 'r')
# sys.setrecursionlimit(10000)

def bfs(x, y, r):
    global grid, result, di, dj

    r += grid[x][y]

    if len(r) == 7:
        result.add(r)
        return
    else:
        for k in range(4):
            ni = x + di[k]
            nj = y + dj[k]
            if 0 <= ni < 4 and 0 <= nj < 4:
                bfs(ni, nj, r)

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
T = int(input())
for tc in range(1, T+1):
    grid = [input().split() for _ in range(4)]

    result = set()
    res = ''
    for i in range(4):
        for j in range(4):
            bfs(i, j, res)
    print('#{} {}'.format(tc, len(result)))
    # 임의의 위치에서 시작
    # 인접한 격자로 총 6번 이동하면서 각 칸에 있는 숫자를 저장
    # 격자판을 벗어나는 이동은 하지 않음
    # 서로 다른 7가지 프로그램을 구하는 개수
