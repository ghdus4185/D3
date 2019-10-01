import sys
sys.stdin = open('input.txt', 'r')

# 재귀
def f(i, N, B):
    global cnt
    if sum(B) > K:
        return

    if i == N:
        if sum(B) == K:
            cnt += 1
    else:
        # i 번째 원소를 선택하거나
        f(i + 1, N, B + [A[i]])
        # i 번째 원소를 선택하지 않거나
        f(i + 1, N, B)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    cnt = 0
    B = []
    f(0, N, B)
    print('#{} {}'.format(tc, cnt))

    # 비트연산자
    # cnt = 0
    # for i in range(1<<N):
    #     temp = []
    #     for j in range(N):
    #         if i & (1<<j) != 0:
    #             temp.append(A[j])
    #     if sum(temp) == K:
    #         cnt += 1
    # print('#{} {}'.format(tc, cnt))