import sys
sys.stdin = open('input.txt')

def dfs(n):
    global cnt

    for i in range(2, N+1):
        if adj[n][i] == 1 and i not in check:
            cnt += 1
            check.append(i)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 사람수, 친한관계수
    adj = [[0] * (N+1) for _ in range(N+1)]
    visited = [0] * (N+1)
    check = []

    # 직접 초대된 친구들 저장
    for i in range(M):
        a, b = map(int, input().split())
        if a == 1:
            check.append(b)
        adj[a][b] = 1
        adj[b][a] = 1

    # 직접 초대된 친구들이랑 인접한 친구들 찾기
    cnt = 0
    for i in range(len(check)):
        dfs(check[i])

    # print(check)
    print('#{} {}'.format(tc, len(check)))