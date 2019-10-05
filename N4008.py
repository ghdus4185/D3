# 각 연사자 자리를 사용해서 모든 순열을 만들고
# 만들어진 모든 순열을 연산자 자리에 넣고 계산해서 최대값과 최소값을 동시에 구한다
# 모든 순열을 다 확인한 다음에 최대값 빼기 최소값을 계산한다.
import sys
sys.stdin = open('input.txt', 'r')

def npr(n, N):
    global open_lst, maxV, minV, num
    if n == N:
        print(p)
        res = num
        for i in range(N):
            if p[i] == '+':
                res[i+1] = res[i] + res[i+1]
            elif p[i] == '-':
                res[i+1] = res[i] - res[i+1]
            elif p[i] == '*':
                res[i+1] = res[i] * res[i+1]
            elif p[i] == '/':
                res[i+1] = res[i] // res[i+1]
        if res[i+1] > maxV:
            maxV = res[i+1]
        if res[i+1] < minV:
            minV = res[i+1]

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
    operator = list(map(int, input().split()))
    num = list(map(int, input().split()))
    oper_lst = []
    for i in range(len(operator)):
        if i == 0:
            for i in range(operator[i]):
                oper_lst += ['+']
        elif i == 1:
            for i in range(operator[i]):
                oper_lst += ['-']
        elif i == 2:
            for i in range(operator[i]):
                oper_lst += ['*']
        elif i == 3:
            for i in range(operator[i]):
                oper_lst += ['/']
    print(oper_lst)
    maxV, minV = 0, 1000*1000
    used = [0] * (N-1)
    p = [0] * (N-1)
    npr(0,N-1)
    print(maxV,minV)