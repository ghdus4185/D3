import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr[0]
    new = [arr[(N*i)+1:(N*i)+(N+1)] for i in range(N)]

    for i in range(N):
        for j in range(N):
            if new[i][j] == 0:
                new[i][j] = 1001
    # 갱신
    for i in range(N):
        for j in range(N):
            if i != j:
                for k in range(N):
                    if k != i and k != j:
                        if new[j][k] > new[j][i] + new[i][k]:
                            new[j][k] = new[j][i] + new[i][k]
    minV = 100000
    for i in range(N):
        s = 0
        for j in range(N):
            if new[i][j] != 1001:
                s += new[i][j]
        if minV > s:
            minV = s

    print('#{} {}'.format(tc, minV))

