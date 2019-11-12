import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    # DP
    V = [0] * (N+1)
    C = [0] * (N+1)
    bag = [[0] * (K+1) for _ in range(N+1)]
    maxC = 0
    for i in range(1, N+1):
        V[i], C[i] = map(int, input().split()) # 부피, 가치
    print(V)
    print(C)
    for i in range(N+1):
        for j in range(N+1):
            bag[0]
    # i번째 열의 j번을 위에꺼랑 비교했을 때 큰값으로 다 채운다.



        # if i == 0:
        #     for j in range(K):
        #         if v <= j:
        #             bag[i][j] = c
        # for j in range(K):
        #     bag[i][j] = max(bag[i-1][j], c)
    # print(maxC)