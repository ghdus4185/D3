import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    num.sort()

    res = []
    n = 1
    while n != 11:
        if n % 2 == 1:
            res.append(num[-((n//2)+1)])
        else:
            res.append(num[(n//2)-1])
        n += 1
    print('#{} {}'.format(tc, ' '.join(map(str, res))))