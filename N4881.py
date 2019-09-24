def stack(n, s):
    if n == N:
        return minV

# 첫번째열에서 하나
# 두번째열에서 하나
# 세번째 열에서 하나 뽑아서 더함

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input()))
    minV = 1000000000
    s = 0
    stack = []
    for i in range(N):
        for j in range(N):
            for k in range(N):
                s += num[i][j]
    if minV > s:
        minV = s

    print('#{} {}'.format(tc, minV))