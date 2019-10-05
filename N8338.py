T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    res = a[0]
    for i in range(N-1):
        x = res + a[i+1]
        y = res * a[i+1]
        if x > y:
            res = x
        else:
            res = y
    print('#{} {}'.format(tc, res))