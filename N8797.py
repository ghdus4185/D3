import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrot = [list(map(int, input().split())) for _ in range(N)]
    r1, r2, r3, r4 = 0, 0, 0, 0
    for i in range(N):
        for j in range(N):
            # r1
            if 0 <= i < N-(N//2):
                if 1+i <= j <= N-2-i:
                    r1 += carrot[i][j]
            # r2
            if 1 <= i <= N // 2:
                if N-i <= j <= N-1:
                    r2 += carrot[i][j]
            elif N//2 < i <= N-1:
                if N //2 + (i - N//2) <= j <= N - 1:
                    r2 += carrot[i][j]
            # r3
            if N//2 < i < N:
                if N//2 - (i-N//2) <= j <= N//2 + (i-N//2):
                    r3 += carrot[i][j]
            # r4
            if 1 <= i <= N // 2:
                if 0 <= j <= i:
                    r4 += carrot[i][j]
            elif N//2 < i <= N-1:
                if 0 <= j <= N//2-(i-N//2):
                    r4 += carrot[i][j]
    print('#{} {}'.format(tc, max(r1, r2, r3, r4) - min(r1, r2, r3, r4)))