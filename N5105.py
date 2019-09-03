def f(i, j, e, N):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    global minV
    if maze[i][j] == 3: # 도착지면
        if minV > e:
            minV = e
    else: # 도착지가 아니면
        maze[i][j] = 1 # 현재칸에 방문 표시(진행 방향에서 다시 돌아오는 것 방지)
        for k in range(4): #4방향 탐색해서 이동 가능한 칸으로 이동
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N: # 미로를 벗어나지 않고
                if maze[ni][nj] !=1: # 갈 수 있는 칸이면(벽이 아니면)
                    f(ni, nj, e+1, N)
        maze[i][j] = 0 # 새로운 경로로 현재칸에 진입 허용

T = int(input())
for tc in range(T):
    N = int(input())
    maze = [[int(x) for x in input()] for i in range(N)]
    for i in range(N):
        if 2 in maze[i]:
            sRow = i    # 출발 row index
            sCol = maze[i].index(2) # 출발 column index
    minV = 100000
    f(sRow, sCol, 0, N) # 미로탐색
    if minV == 100000:
        minV = 1
    print('#{} {}'.format(tc+1, minV-1))
