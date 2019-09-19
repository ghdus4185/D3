import sys

sys.stdin = open('input.txt', 'r')


def check(t, c):
    global maxV, cnt
    if t >= N:
        return

    for i in range(1, c + 1):
        if maxV < t + i + charge[t + i - 1]:
            a = i

    cnt += 1
    if maxV >= N:
        return
    else:
        check(t+a, charge[t+a-1])


T = int(input())
for tc in range(1, T + 1):
    bus = list(map(int, input().split()))
    N = bus[0]
    charge = bus[1:]
    maxV = 0
    cnt = 0
    check(1, charge[0])
    print('#{} {}'.format(tc, cnt))