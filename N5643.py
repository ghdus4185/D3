# 키순서 문제 <= 위상정렬
# 모든 점에서 2차 배열을 만들고
# 전에 몇개 후에 몇개가 정해지는지 갯수를 확인해서 그 갯수가 n-1이면 가능한 노드
# 1. 모든선 최단경로를 만들기
# 2. 최단경로 배열을 해석해서 가능한 노드 확인
# 3. 가능한 노드의 총 갯수 출력

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 노드수
    M = int(input()) # 간선수
    x = float('inf')
    arr = [[0]*N for _ in range(N)]
    # 주어진 입력으로 모든선 그래프를 만든다.
    for _ in range(M):
        a, b = map(int, input().split())
        arr[a-1][b-1] = 1
        # 그 위치에서 갈 수있는곳을 확인하고 갈 수 있는곳에 2를 체크
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0: # 갈 수 있으면
                for k in range(N):
                    if arr[j][k] != 0:
                        if not arr[i][k]:
                            arr[i][k] = arr[j][k] + arr[i][j]
    for i in range(N):
        print(arr[i])
    res = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j]:
                cnt += 1
        for j in range(N):
            if arr[j][i]:
                cnt += 1
        if cnt == N-1:
            res += 1
    print('#{} {}'.format(tc, res))