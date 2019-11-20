import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    num = list(map(int, input().split())) # 2n
    x = sorted(num)
    print('#{} {}'.format(tc, x))
