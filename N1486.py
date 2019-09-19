import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    h = list(map(int, input().split()))

    subset_list = []
    minV = 10000000
    for i in range(1, 2**N):
        res = 0
        for j in range(N):
            if i & (1 << j) != 0:
                res += h[j]
            if res >= B:
                if minV > res:
                    minV = res

    print('#{} {}'.format(tc, minV - B))