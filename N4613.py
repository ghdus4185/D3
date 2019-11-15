import sys
sys.stdin = open('input.txt', 'r')

d = [[-1, 0], [1, 0]] # 상 하
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)] # W는 맨위로 R은 다 아래로
    for i in range(N):
        print(arr[i])
    # 맨 위랑 맨 아래는 무조건 W
    res = 0
    turn = 'W'
    memory = [0]*N
    for i in range(N):
        wc, bc, rc = 0, 0, 0
        for j in range(M):
            # 파랑이 가장 많은 열을 B로 칠한다.
            if arr[i][j] == 'B':
                bc += 1
        memory[i] = [bc, wc, rc]
    print(memory)
    max(memory)
    # 그 위는 다 화이트로 칠하고
    # 그 밑은 다 레드로 칠한다.
    max()