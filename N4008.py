import sys
sys.stdin = open('input.txt', 'r')

def npr(n, N):
    global minV, maxV
    if n == N:
        if p not in check:
            check.append(p[:])
            res = num[:]
            for i in range(len(p)):
                if p[i] == "+":
                    res[i+1] = res[i] + res[i+1]
                elif p[i] == "-":
                    res[i+1] = res[i] - res[i+1]
                elif p[i] == "*":
                    res[i+1] = res[i] * res[i+1]
                elif p[i] == "/":
                    res[i+1] = int(res[i] / res[i+1])
            if res[-1] < minV:
                minV = res[-1]
            if res[-1] > maxV:
                maxV = res[-1]
    else:
        for i in range(N):
            if used[i] == 0:
                used[i] = 1
                p[n] = oper_lst[i]
                npr(n+1, N)
                used[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    operation = list(map(int, input().split()))
    num = list(map(int, input().split()))
    oper_lst = []
    for i in range(N-1):
        if i == 0:
            for i in range(operation[i]):
                oper_lst += ['+']
        elif i == 1:
            for i in range(operation[i]):
                oper_lst += ['-']
        elif i == 2:
            for i in range(operation[i]):
                oper_lst += ['*']
        elif i == 3:
            for i in range(operation[i]):
                oper_lst += ['/']
    minV, maxV = 1000*1000, -100000000000
    used = [0] * (N-1)
    p = [0] * (N-1)
    check = []
    npr(0, N-1)
    print('#{} {}'.format(tc, maxV - minV))