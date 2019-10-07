# def wave(n):
#     global d
#     # 딕셔너리에 값이 없으면 만들어준다.
#     # N까지 만든다.
#     if n > 5:
#         d[n] = d[n-1] + d[n-5]
#         wave(n+1)
#     else:
#         wave(n+1)
#     if n == N:
#         return



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    d = {1:1, 2:1, 3:1, 4:2, 5:2}
    d = [0] + [1, 1, 1, 2, 2] + [0] * N
    # d의 n번째는 n-5번째랑 n-1번째를 더한다.
    # n까지 d를 만들고 n번째꺼를 출력
    for i in range(6, N+1):
        d[i] = d[i-1] + d[i-5]
    # print(d[N])
    # wave(1)
    print('#{} {}'.format(tc, d[N]))