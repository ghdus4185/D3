import sys
sys.stdin = open('input.txt', 'r')

def f(x, y, check):
    global arr, p, visited
    stack = [[x, y]]
    while stack:
        i, j = stack.pop()
        for k in range(4):
            ni = i + d[k][0]
            nj = j + d[k][1]
            if 0 <= ni < 100 and 0 <= nj < 100:
                # 0이고 방문안했으면 그 점에서 다시 탐색
                if arr[ni][nj] == 3:
                    p = 1
                    return
                if arr[ni][nj] == 0 and check[ni][nj] == 0:
                    check[i][j] = 1
                    f(ni, nj, check)
                    check[i][j] = 0
    return

d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for tcc in range(1, 11):
    tc = int(input())
    arr = [list(map(int, ' '.join(input()).split())) for _ in range(100)]
    # 1은 벽을 나타내며 0은 길, 2는 출발점, 3은 도착점
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                si, sj = i, j
            elif arr[i][j] == 3:
                li, lj = i, j
    p = 0
    visited = [[0] * 100 for _ in range(100)]
    f(si, sj, visited)

    print('#{} {}'.format(tc, p))