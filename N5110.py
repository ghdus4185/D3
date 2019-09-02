T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    for i in range(M):
        res = 0
        if i > 0:
            b = list(map(int, input().split()))
            for j in a:
                if j > b[0]:
                    idx = a.index(j)
                    res = 1
                    break
            if res == 1:
                a[idx:idx] = b
                # a = a[:idx] + b + a[idx:]
            else:
                # a + b
                a.extend(b)
                # a[-1:-1] = b
        else:
            a = list(map(int, input().split()))
    final = list(map(str, a))
    print('#{} {}'.format(tc+1, " ".join(final[-1:-11:-1])))