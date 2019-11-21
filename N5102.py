import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[0] * V for _ in range(V)]
    for i in range(E):
        v, e = map(int, input().split())
        arr[v-1][e-1] = 1
    go = 1
    while go:
        go = 0
        for i in range(V):
            for j in range(V):
                if arr[i][j] == 1:
                    for k in range(V):
                        go = 1
                        if arr[j][k] == 1:
                            arr[i][k] = 1
            
    start_node, last_node = map(int, input().split())

    print()