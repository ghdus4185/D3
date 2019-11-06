import sys
sys.stdin = open('input.txt',  'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    # 첫번째 column중에 하나 두번째 중에 하나 ...
    # 0 1 2
    # 1 0 2
    maxV = 0
    for i in range(N):
        used = [0] * N
        for j in range(N):
            used[i] = 1
            res = (P[j][i]/100)
            for k in range(N):
                if used[k] == 0:
                    used[k] = 1
                    print(P[j+1][k])
                    res *= (P[j][k]/100)
                    break
            if 0 not in used:
                if maxV < res:
                    maxV = res
    print('#{} %.6f'.format(tc) %(maxV*100))
