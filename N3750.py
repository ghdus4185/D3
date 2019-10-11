T = int(input())
result = []
for tc in range(1, T+1):
    n = int(input())
    while 1:
        res = 0
        for i in str(n):
            res += int(i)
        if res < 10:
            result.append(res)
            break
        n = res
for tc in range(1, T+1):
    print('#{} {}'.format(tc, result[tc-1]))