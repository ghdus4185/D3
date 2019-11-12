import sys
sys.stdin = open('input.txt', 'r')

def f(n, k, res):
    global cnt
    if n == k:
        chc = [0] * M
        for i in range(N):
            chc[res[i]-1] = 1
        if 0 not in chc:
            cnt += 1
    else:
        for i in range(M):
            res[n] = i+1
            f(n+1, k, res)

T = int(input())
for tc in range(1, T+1):
    M, N = map(int, input().split())
    # M개의 지문을 다 써야함
    res = M**N
    cnt = 0
    res = [0] * N
    f(0, N, res)
    print('#{} {}'.format(tc, cnt % 1000000007))


