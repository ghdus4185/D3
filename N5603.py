import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = [int(input()) for _ in range(N)]
    avg = sum(a) // N
    s = 0
    for i in range(N):
        s += abs(avg - a[i])
    print('#{} {}'.format(tc, s//2))