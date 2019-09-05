# BFS를 냅다 돌리고
# 9가 있는 자리가 1로 표시하고 옆에 칸이 하나 떨어져 있는 거니까
# 물고기가 있는 값이랑 거리 정보를 비교해서 제일 짧은걸 0
# 아기상어는 1초에 상하좌우 인접한 한 칸씩 이동한다.
# 만약 자기보다 큰 물고기가 있는 칸은 지나갈 수 없다
# 만약 자기보다 작은 물고기는 먹을 수 있다.
# 크기가 같으면 지나갈 순 있고 먹을 순 없다.
# 먹을 수 있는 물고기가 공간에 없으면 엄마 상어에게 도움을 요청한다.
# 먹을 수 있는 물고기가 있으면 그 중 가장 거리가 짧은 물고기를 먹으러 간다.
# 거리는 물고기와 아기상어 사이의 칸 수
# 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면
# 가장 왼쪽 물고기를 먹는다.
# 물고기를 먹으면 그 칸은 빈 칸이 된다.
# 아기상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 증가한다.
# 가장 처음 아기상어의 크기는 2

# 잡아먹을 수 있는 얘가 나왔을 때 그 애의 최소거리를 가지고 있고
# 거리가 멀어지면
def bfs(si,sj):
    global sea, eatCnt

    for i in range(N):
        for j in range(N):
            if sea[i][j] >= size:
                return second

    for i in range(N):
        for j in range(N):
            sea:
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    sea = [list(map(int, input().split())) for _ in range(N)]

    size = 2
    fish1 = 0
    fish2 = 0
    second = 0
    eatCnt = 0
    for i in range(N):
        for j in range(N):
            if sea[i][j] == 9:
                si, sj = i, j
                break
    # r = 1
    # sec = 0
    # eatCnt = 0
    # while 1:
    print('#{} {}'.format(tc, second))

# bfs
#     visited[][]
#     checked[][] 최소 거리의 물고기만 표시
#     while(큐가 비어있지 않으면)
#         상어 위치를 pop()
#         상어가 checked에 기록 안된 먹을 수 있는 물고기를 만나면
#                 최초인 경우
#                     최소 거리로 저장하고
#                     checked[][]에 거리 기록
#                 최소 거리와 같은 거리에 있는 경우
#                         checked[][]에 거리 기록
#         # 다음에 이동할 칸 enqueue
#         주변에 비어있거나 상어 이하 크기의 물고기가 있는 칸이면
#                 eunqueue()
#                 visited[][]에 거리 표시
#
#     checked[][]를 왼쪽 위부터 탐색해서 최초로 0이 아닌 칸을 만나면 거리 정보를 리턴
#     0이 아닌 칸이 없으면 0 리턴 (거리정보=시간정보)
# 원래 물고기 크기에 9가 없으니까 9를 지우고 시작해야함
