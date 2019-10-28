import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    c = list(map(int, input().split()))
    c.sort()
    res = sum(c)
    for i in range(N//3):
        res -= c[i*3]
    print('# {} {}'.format(tc, res))