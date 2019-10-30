import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    jump = list(map(int, input().split()))

    jump.sort(reverse=True)
    res1, res2 = [], []
    for i in range(N):
        if i % 2 == 0:
            res1.append(jump[i])
        else:
            res2.append(jump[i])
    res = res1 + res2[::-1]
    maxV = 0
    for i in range(N):
        if i == N-1:
            if maxV < abs(res[i] - res[0]):
                maxV = abs(res[i] - res[0])
        else:
            if maxV < abs(res[i] - res[i+1]):
                maxV = abs(res[i] - res[i + 1])
    print('#{} {}'.format(tc, maxV))