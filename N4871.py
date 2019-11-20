import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    li = [[0] * V for _ in range(V)]
    for i in range(E):
        n1, n2 = map(int, input().split())
        li[n1-1][n2-1] = 1
    for i in range(V):
        for j in range(V):
            if li[i][j] == 1:
                for k in range(V):
                    if li[j][k] == 1:
                        li[i][k] = 1
    c1, c2 = map(int, input().split())

    print('#{} {}'.format(tc, li[c1-1][c2-1]))