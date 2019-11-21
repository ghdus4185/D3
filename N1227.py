import sys
sys.stdin = open('input.txt', 'r')


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

    visited = [[0] * 100 for _ in range(100)]
    p = 0
    stack = [[si, sj]]
    while stack:
        x, y = stack.pop()
        for k in range(4):
            ni = x + d[k][0]
            nj = y + d[k][1]
            if 0 <= ni < 100 and 0 <= nj < 100:
                if arr[ni][nj] == 3:
                    p = 1
                    break
                elif arr[ni][nj] == 0 and visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    stack.append([ni, nj])

    print('#{} {}'.format(tc, p))