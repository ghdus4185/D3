T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    cell = [list(map(int, input().split())) for _ in range(N)]
    field = [[0] * 650 for _ in range(650)]
    r = 650//2
    for i in range(r-N//2, r+cell):
        for j in range(N):
            pass