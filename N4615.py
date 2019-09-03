# import sys
# sys.stdin = open('sample_input(1).txt', 'r')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())

    board = []
    for i in range(N):
        board.append([0] * N)
        if i == (N//2) - 1:
            board[(N//2)-1][(N//2)-1] = 2
            board[(N//2)-1][(N//2)] = 1
        elif i == N//2:
            board[(N//2)][(N//2)-1] = 1
            board[(N//2)][(N//2)] = 2
    di = [-1, -1, 0, 1, 1, 1, 0, -1]
    dj = [0, 1, 1, 1, 0, -1, -1, -1]
    for i in range(M):
        cmd = list(map(int, input().split()))
        if cmd[-1] == 1:
            board[cmd[1]-1][cmd[0]-1] = 1
        elif cmd[-1] == 2:
            board[cmd[1]-1][cmd[0]-1] = 2

        # 시작점
        i = cmd[1] - 1
        j = cmd[0] - 1

        # 8방향으로 탐색
        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]
            # 탐색하는 곳이 board 범위 체크
            if 0 <= ni < N and 0 <= nj < N:
                # board
                if board[ni][nj] == 0 or board[ni][nj] == cmd[-1]:
                    pass
                else: # 다른거면 같은 방향으로 계속 탐색 시작
                    check = []
                    while 1:
                        # 다음 탐색이 board 범위 인지 체크
                        if 0 <= ni < N and 0 <= nj < N:
                            # 같은 숫자면 표시한거 뒤집기
                            if board[ni][nj] == cmd[-1]:
                                for x in range(len(check)):
                                    board[check[x][0]][check[x][1]] = cmd[-1]
                                break
                            # 다른 숫자면 방문 표시
                            elif board[ni][nj] != cmd[-1]:
                                check.append([ni, nj])

                        if (ni == N or ni == -1) or (nj == -1 or nj == N):
                            break
                        # elif nj == N or nj == -1:
                        #     break

                        if board[ni][nj] == 0:
                            break

                        ni += di[k]
                        nj += dj[k]

    black = 0
    white = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1

    print('#{} {} {}'.format(tc+1, black, white))