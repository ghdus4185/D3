import sys
sys.stdin = open('input.txt', 'r')

# 각 연산자 별로 하나 씩 쭉~ 넣고 연산해서
# minV, maxV 값을 구한다
def f(n, N, temp):
    global minV, maxV
    if n == N:
        minV = min(minV, temp)
        maxV = max(maxV, temp)
    else:
        if operation[0] != 0:
            operation[0] -= 1
            f(n + 1, N, temp + num[n])
            operation[0] += 1
        if operation[1] != 0:
            operation[1] -= 1
            f(n + 1, N, temp - num[n])
            operation[1] += 1
        if operation[2] != 0:
            operation[2] -= 1
            f(n + 1, N, temp * num[n])
            operation[2] += 1
        if operation[3] != 0:
            operation[3] -= 1
            f(n + 1, N, int(temp / num[n]))
            operation[3] += 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    operation = list(map(int, input().split()))
    num = list(map(int, input().split()))
    minV, maxV = 1000*1000, -100000000000
    f(1, N, num[0])

    print('#{} {}'.format(tc, maxV - minV))