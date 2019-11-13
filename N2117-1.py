# 모든 집의 좌표를 가지고 있는다.
# 최대 K를 구한다.
# 한점에서 거리가 (K-1) 안에 있는 집의 개수를 센다. => 비용계산
# 가능하면 break
# 최대 K일때 손해를 보지않고 서비스 할 수 있는 집의 개수를 검사

import sys
sys.stdin = open('input.txt', 'r')

computed = [1, 5, 13, 25]
for i in range(50):
    computed.append((5+i)**2+(4+i)**2)
computed = [0] + computed

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxK = 2*N-1

    # 모든 집의 좌표를 가지고 있는다.
    town = []
    h = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                town.append([i, j])
                h += 1
    # 거리가 k 안에 있는 집의 개수를 세고 이익을 계산한다.
    maxV = 0
    for k in range(maxK-1, 0, -1): # k를 정함
        for i in range(N):
            for j in range(N): # i, j 좌표를 정함
                cnt = 0
                for v in range(h): # 집의 개수만큼 for문
                    # 각 집의 거리랑 현재 좌표랑 거리가 k보다 작으면
                    if abs(town[v][0] - i) + abs(town[v][1]-j) < k:
                        # 거리가 k보다 작으면
                        cnt += 1
                # 손해가 나지 않을 때
                if (cnt * M) - computed[k] >= 0:
                    # 가장 많은 서비스를 받은 집보다 크면
                    if maxV < cnt:
                        # 갱신
                        maxV = cnt


    print('#{} {}'.format(tc, maxV))