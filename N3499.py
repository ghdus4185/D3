T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = input().split()
    res = ''
    # 왼쪽에서 하나 뽑아서 두고
    # 오른쪽에서 하나 뽑아서 두고
    if N % 2 == 0:
        L = card[:N//2]
        R = card[N//2:]
        for i in range(N):
            if i % 2 == 0:
                res += L[i // 2] + ' '
            else:
                res += R[i // 2] + ' '
    else:
        L = card[:N//2]
        R = card[N//2+1:]
        for i in range(N-1):
            if i % 2 == 0:
                res += L[(i // 2)] + ' '
            else:
                res += R[(i // 2)] + ' '
        res += card[N//2]
    print('#{} {}'.format(tc, res))