import sys
sys.stdin = open('input.txt',  'r')

def f(n, k, r, used):
    global maxV, N, P
    if n == N:
        if maxV < r:
            maxV = r
    else:
        if used[n] == 0:
            used[n] = 1
            print(P[k][n]/100)
            r *= (P[k][n]/100)
            f(n+1, k+1, r, used)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    # 첫번째 column중에 하나 두번째 중에 하나 ...
    # 컬럼을 사용했는지 않했는지 체크
    maxV = 0
    c = [0] * N
    f(0, 0, 1, c)
    # for i in range(N):
    #     used = [0] * N
    #     for j in range(N):
    #         used[i] = 1
    #         res = (P[j][i]/100)
    #         # print(res)
    #         for k in range(N):
    #             if used[k] == 0:
    #                 used[k] = 1
    #                 print(P[j][k])
    #                 res *= (P[j][k]/100)
    #                 break
    #         if 0 not in used:
    #             if maxV < res:
    #                 maxV = res
    # print('#{} %.6f'.format(tc) %(maxV*100))