import sys
sys.stdin = open('input.txt', 'r')

def npr(n, k, N):
    global a
    if n == k:
        if sum(p) not in a:
            a.append(sum(p))
    else:
        for i in range(N):
            if used[i] == 0:
                used[i] = 1
                p[n] = nums[i]
                npr(n+1, k, N)
                used[i] = 0

T = int(input())
for tc in range(1, T+1):
    nums = list(map(int, input().split()))
    N = 7
    k = 3
    used = [0] * N
    p = [0] * k
    a = []
    maxV = 0
    npr(0, k, N)
    a.sort()
    print('#{} {}'.format(tc, a[-5]))