import sys
sys.stdin = open('input.txt', 'r')

def f(r):
    global way
    cnt = 1
    i = 0
    p = 0
    while i < N-1:
        if r[i] - r[i+1] == 0 or r[i] - r[i+1] == -1 or r[i] - r[i+1] == 1:
            if r[i] - r[i+1] == -1:
                if cnt >= X:
                    cnt = 0
                else:
                    break
            elif r[i] - r[i+1] == 1:
                cnt = 1
                j = 1
                while i+1+j < N:
                    if r[i+1] == r[i+1+j]:
                        cnt += 1
                    else:
                        break
                    j += 1
                if cnt >= X:
                    cnt = -1
                    i += (X-1)
                else:
                    break
        else:
            break
        cnt += 1
        i += 1
    else:
        way += 1
        p = 1
    rr = r[::-1]
    dp.append(dict(r=p))
    dp.append(dict(rr=p))

T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())
    land = [list(map(int, input().split())) for _ in range(N)]
    way = 0
    dp = []
    # 가로 한 줄 확인
    for i in range(N):
        if land[i] in dp:
            way += dp[land[i]]
        else:
            f(land[i])
    # 세로 한 줄
    for i in range(N):
        column = []
        for j in range(N):
            column += [land[j][i]]
        if column in dp:
            way += dp[column]
        else:
            f(column)
    print('#{} {}'.format(tc, way))