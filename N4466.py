import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    score = list(map(int, input().split()))

    a = sorted(score)
    add = 0
    for i in range(K):
        add += a[N-1-i]
    print('#{} {}'.format(tc+1, add))
