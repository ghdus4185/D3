import sys
sys.stdin = open('input.txt', 'r')

def houes(x, y, k):
    global maxV
    h = 0
    check = [[0] * N for _ in range(N)]
    q = []
    q.append((x, y))
    if vilige[x][y] == 1:
        h += 1
    check[x][y] = 1
    while q:
        i, j = q.pop(0)
        for m in range(4):
            ni = i + d[m][1]
            nj = j + d[m][0]
            if 0 <= ni < N and 0 <= nj < N:
                if 0 < check[i][j] <= k - 1 and check[ni][nj] == 0:
                    check[ni][nj] = check[i][j] + 1
                    if abs(ni-x)+abs(nj-y) <= k-1:
                        q.append((ni, nj))
                    if vilige[ni][nj] == 1:
                        h += 1
    if maxV > h:
        return
    # 손해가 없으면
    if (h * M) - cost[k-1] >= 0:
        if maxV < h:
            maxV = h

cost = [1, 5, 13, 25]
for i in range(22):
    cost.append(cost[-1]+len(cost)*4)

d= [[1,0], [-1,0], [0,-1], [0,1]]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    vilige = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0

    for k in range(1, N+2): # k가 1~N+1
        maxH = 0
        # k가 1일때 모든점에서 가장 많은 집에 서비스할 수 있는 집 개수를 저장한다.
        for i in range(N):
            for j in range(N):
                houes(i, j, k)
    print('#{} {}'.format(tc, maxV))