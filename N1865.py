import sys
sys.stdin = open('input.txt',  'r')

def f(n, k):
    global res, maxV
    if n == k:
        for i in range(N):
            res *= (P[i][arr[i]]/100)
        if maxV < res:
            maxV = res
    else:
        for i in range(N):
            if used[i] == 0:
                used[i] = 1
                arr[n] = i
                f(n+1, k)
                used[i] = 0
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    # 첫번째 중에 하나 두번째 중에 하나 ...
    arr = [0] * N
    used = [0] * N
    maxV = 0
    res = 1
    f(0, N)
    print('#{} {}'.format(tc, str(maxV * 100) + '00000'))
