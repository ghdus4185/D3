T = int(input())
for tc in range(T):
    N = int(input())

    s = 0
    for i in range(N):
        p, x = map(float, input().split())
        s += (p * x)
    print('#{} {}'.format(tc+1, s))