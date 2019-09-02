import sys
sys.stdin = open('sample_input.txt', 'r')

# 가장 높은 봉우리를 찾아야한다
# 내 주변을 선택할 때 나보다 낮은 얘들을 선택하거나 한번 깎아서 선택할 수 있다.
# 이후에 깎는게 더 유리할 수 있으므로
# 1) 낮은 칸으로 이동해보기
# 2) 높거나 같은 칸에 대해서 2가지 선택 깍는다 or 깍지않는다.
# 3) 깍아서 지나갈 수 있는 상황이라면 굳이 많이 깍지 않고 딱 나보다 작은 정도만
# 깍는다.
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
            elif visited[ni][nj] == 0 and c > 0 and arr[i][j] > arr[ni][nj]-K:
                # 주변 점을 깍아서 이동
                org = arr[ni][nj] # 원래 높이 저장
                arr[ni][nj] = arr[i][j] -1 # 주변 점을 깍아서 이동
                f(ni, nj, 0, e+1)
                arr[ni][nj] = org # 높이 원상 복구
                # 돌아왔을 때를 생각해서 깍기 전 높이를 저장해둔다
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