import sys
sys.stdin = open('input.txt', 'r')

def npr(n, N, s):
    global minV

    if s > minV:
        return

    if n == N:
        if minV > s:
            minV = s
    else:
        for i in range(N):
            if used[i] == 0:
                used[i] = 1
                npr(n+1, N, s+abs(area[i][0] - factory[n][0]) + abs(area[i][1] - factory[n][1]))
                used[i] = 0

N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
factory = [list(map(int, input().split())) for _ in range(N)]

minV = 1000000000000000000000000
used = [0] * N
npr(0, N, 0)
print(minV)