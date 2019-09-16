T = int(input())
for tc in range(1, T+1):
    N = input()
    num = float(N)
    res = []
    i = 1
    while num != 0:
        if num*2 >= 1:
            res.append('1')
            num = num * 2 - 1
        else:
            res.append('0')
            num = num * 2
        i += 1
    if len(res) > 12:
        print('#{} overflow'.format(tc))
    else:
        print('#{} {}'.format(tc, "".join(res)))