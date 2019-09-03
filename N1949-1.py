#깍는거 없이 최장 등산로 찾기
def f(i, j, c, e): # c : 깍는 횟수, e : 이동거리
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    global N, K, maxV, visited, arr

    if maxV < e:
        maxV = e
    visited[i][j] = 1 # 등산로에 포함되었음을 표시

    #주변탐색
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if ni >= 0 and ni < N and nj >= 0 and nj< N: # 유효좌표인지 확인
            if arr[i][j] > arr[ni][nj]:
                f(ni, nj, c, e+1) # 주변의 낮은 점으로 이동
    visited[i][j] = 0 # 다른 경로의 등산로에 포함될 수 있으므로
    return

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    h = 0
    for i in range(N):
        for j in range(N):
            if h < arr[i][j]:
                h = arr[i][j]
    maxV = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == h:
                f(i, j, 1, 1)

    print('#{} {}'.format(tc+1, maxV))