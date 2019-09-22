import sys
sys.stdin = open('input.txt', 'r')

def perm(n, k):
    global c, minV
    if n == k:
        res = [1] + (p[:k]) + [1]
        c = 0
        for i in range(N):
            c += matrix[res[i]-1][res[i+1]-1]
        if minV > c:
            minV = c
    else:
        for i in range(n, k):
            p[n], p[i] = p[i], p[n]
            perm(n+1, k)
            p[n], p[i] = p[i], p[n]

# def npr(n, k, N):
#     if n == k:
#         print(p)
#     else:
#         for i in range(N):
#             if used[i] == 0:
#                 used[i] = 1
#                 p[n] = i+2
#                 npr(n+1, k, N)
#                 used[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # p = [i for i in range(2, N+1)]
    minV = 100000
    used = [0] * (N -1)
    p = [0] * (N-1)
    npr(0, N-1, N-1)
    # perm(0, N-1)
    # print('#{} {}'.format(tc, minV))