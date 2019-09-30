import sys
sys.stdin = open('input.txt', 'r')

# def ncr(i, N, v, c):
#     global maxV, cnt
#
#     cnt += 1
#
#     # 무게가 K보다 크면
#     if v > K:
#         return
#
#     # 무게가 K에 닿으면
#     elif v == K:
#         if maxV < c:
#             maxV = c
#         return
#
#     # 모든 원소를 다 넣으면
#     elif i == N:
#         if maxV < c:
#             maxV = c
#         return
#     else:
#         # 넣는다
#         ncr(i+1, N, v+bag[i][0], c + bag[i][1])
#         # 않넣는다
#         ncr(i+1, N, v, c)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    # DP
    lst = [[0] * K for _ in range(N)]
    for i in range(N):
        v, c = map(int, input().split())
        # i번째 열의 j번을 위에꺼랑 비교했을 때 큰값으로 다 채운다.
        if i == 0:
            for j in range(K):
                if v <= j:
                    lst[i][j] = c
        for j in range(K):
            lst[i][j] = max(lst[i-1][j], c)

    # 재귀
    # maxV = 0
    # cnt = 0
    # ncr(0, N, 0, 0)
    # print('#{} {}'.format(tc, maxV))
    # print(cnt)


    # 비트연산자
    # maxV = 0
    # cnt = 0
    # for i in range(1, 1 << N):
    #     volume = 0
    #     cost = 0
    #     res = 0
    #     for j in range(N):
    #         cnt += 1
    #         if i & (1 << j) != 0:
    #             volume += bag[j][0]
    #             cost += bag[j][1]
    #             if volume > K:
    #                 res = 1
    #                 break
    #     if res == 0:
    #         if maxV < cost:
    #             maxV = cost
    # print('#{} {}'.format(tc, maxV))
    # print(cnt)