def wave(n):
    global d
    # 딕셔너리에 값이 없으면 만들어준다.
    # N까지 만든다.
    if n > 6:
        d[n] = d[n-1] + d[n-5]
    else:
        wave(n+1)
    if n == N+1:
        return



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    d = [0] + [1, 1, 1, 2, 2] + [0] * N
    wave(1)
    print('#{} {}'.format(tc, d[N]))