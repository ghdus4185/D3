import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = [int(input()) for _ in range(N)]
    avg = sum(a) // N
    cnt = 0
    while 1:
        if max(a) > avg:
            x = a[a.index(max(a))]
            y = a[a.index(min(a))]
            if x - avg < avg - y:
                cnt += x - avg
                a[a.index(max(a))] -= x - avg
                a[a.index(min(a))] += x - avg
            else:
                cnt += avg - y
                a[a.index(max(a))] -= avg - y
                a[a.index(min(a))] += avg - y

        if max(a) == avg:
            break
    print('#{} {}'.format(tc, cnt))