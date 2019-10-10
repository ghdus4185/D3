T = int(input())
calender = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for tc in range(1, T+1):
    M, D = map(int, input().split())
    d = 0
    if M == 1:
        print('#{} {}'.format(tc, (D % 7) + 3))
    else:
        for i in range(1, M):
            d += calender[i]
        if ((d + D - 1) % 7) + 4 >= 7:
            print('#{} {}'.format(tc, ((d + D - 1) % 7) + 4)-7)
        else:
            print('#{} {}'.format(tc, ((d + D - 1) % 7) + 4))
