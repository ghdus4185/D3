import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(T):
    # 벌통크기 : N 벌통 개수: M 최대 꿀: C
    N, M, C = map(int, input().split())
    bee = [list(map(int, input().split())) for i in range(N)]

    gain = 0
    for i in range(N-1):
        for j in range(N-M+1):
            high1 = 0
            arr = bee[i][j:j+M] # m개씩 슬라이싱
            for ti in range(1, 2 ** M): # 부분 집합 갯수
                s = 0
                ss = 0
                for tj in range(M): #
                    if ti & (1 << tj) and s + arr[tj] <= C:
                        s += arr[tj]
                        ss += arr[tj] ** 2
                if high1 < ss:
                    high1 = ss

            for n in range(i + 1, N):
                for m in range(N - M + 1):
                    high2 = 0
                    arr = bee[n][m:m+M]
                    for ti in range(1, 2**M):
                        s = 0
                        ss = 0
                        for tj in range(M):
                            if ti & (1 << tj) and s + arr[tj] <= C:
                                s += arr[tj]
                                ss += arr[tj] ** 2
                        if high2 < ss:
                            high2 = ss

                        if gain < high1 + high2:
                            gain = high1 + high2

    print('#{} {}'.format(tc+1, gain))