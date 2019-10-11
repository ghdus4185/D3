T = int(input())
res = []
for tc in range(1, T+1):
    N, R = map(int, input().split())
    x, y = 1, 1
    for i in range(R):
        x *= (N-i)
        y *= (i+1)
    res.append(x//y)
for tc in range(1, T+1):
    print('#{} {}'.format(tc, res[tc-1]))