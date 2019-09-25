import sys
sys.stdin = open('input.txt', 'r')

def ncr(n, r):
    global cnt
    if r == 0:
        if sum(p) == K:
            cnt += 1
    elif n < r:
        return
    else:
        p[r-1] = a[n-1]
        ncr(n-1, r-1)
        ncr(n-1, r)

T = int(input())
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for tc in range(1, T+1):
    N, K = map(int, input().split())
    r = N
    p = [0] * r
    cnt = 0
    ncr(12, r)
    print('#{} {}'.format(tc, cnt))