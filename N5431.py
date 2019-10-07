import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    num = list(map(int, input().split()))
    check = [0] * (N+1)
    for i in num:
        check[i] = 1
    print('#{}'.format(tc), end=' ')
    for i in range(1, len(check)):
        if check[i] == 0:
            print(i, end=' ')
    print()