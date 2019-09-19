import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    s1, s2, s3 = 0, 0, 0
    res = 0
    if N % 2:
        s1 = N//2+1 + (N+1) * (N//2)
    else:
        s1 = (N+1) * (N//2)
    if N % 2:
        s2 = N + (N*2) * (N//2)
    else:
        s2 = (N * 2) * (N//2)
    if N % 2:
        s3 = (N+1) + (N*2+2) * (N//2)
    else:
        s3 = (N*2+2) * (N//2)

    print('#{} {} {} {}'.format(tc, s1, s2, s3))