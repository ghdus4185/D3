T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    a = 0
    while (2 * a) + (M-a) != N:
        (2 * a) + (M-a) == N
        a += 1
    print('#{} {} {}'.format(tc+1, M-a, a))