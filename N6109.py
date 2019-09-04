import sys
sys.stdin = open('s_input.txt', 'r')

T = int(input())
for tc in range(T):
    N, cmd = input().split()
    N = int(N)
    board = [list(map(int, input().split())) for _ in range(N)]

    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    if cmd == 'left':
        for j in range(N):
            for i in range(N):
                if board[i][j] != 0:
                    ni = i
                    nj = j
                    while 1:
                        nj += 1
                        if 0 <= ni < N and 0 <= nj < N:
                            # 오른쪽에 숫자가 나랑 같으면 합침
                            if board[i][j] == board[ni][nj]:
                                board[i][j] += board[ni][nj]
                                board[ni][nj] = 0
                                break

                            # 다른게 있으면 break
                            if board[i][j] != board[ni][nj] and board[ni][nj] != 0:
                                break
                        else:
                            break

                    #오른쪽 밀기
                    nj = j
                    while 1:
                        nj -= 1
                        if nj < 0 or board[ni][nj] != 0:
                            board[i][j], board[ni][nj+1] = board[ni][nj+1], board[i][j]
                            break

    elif cmd == 'right':
        for j in range(N-1,-1,-1):
            for i in range(N-1,-1,-1):
                if board[i][j] != 0:
                    ni = i
                    nj = j
                    while 1:
                        nj -= 1
                        if 0 <= ni < N and 0 <= nj < N:
                            # 왼쪽에 숫자가 나랑 같으면 합침
                            if board[i][j] == board[ni][nj]:
                                board[i][j] += board[ni][nj]
                                board[ni][nj] = 0
                                break

                            # 다른게 있으면 break
                            if board[i][j] != board[ni][nj] and board[ni][nj] != 0:
                                break
                        else:
                            break

                    #오른쪽 밀기
                    nj = j
                    while 1:
                        nj += 1
                        if nj >= N or board[ni][nj] != 0:
                            board[i][j], board[ni][nj-1] = board[ni][nj-1], board[i][j]
                            break

    elif cmd == 'up':
        for i in range(N): # 행
            for j in range(N): # 열
                if board[i][j] != 0:
                    ni = i
                    nj = j
                    while 1:
                        ni += 1
                        if 0 <= ni < N and 0 <= nj < N:
                            # 밑에 숫자가 나랑 같으면 합침
                            if board[i][j] == board[ni][nj]:
                                board[i][j] += board[ni][nj]
                                board[ni][nj] = 0
                                break

                            # 다른게 있으면 break
                            if board[i][j] != board[ni][nj] and board[ni][nj] != 0:
                                break
                        else:
                            break

                    #올리기
                    ni = i
                    while 1:
                        ni -= 1
                        if ni < 0 or board[ni][nj] != 0:
                            board[i][j], board[ni+1][nj] = board[ni+1][nj], board[i][j]
                            break
    elif cmd == 'down':
        for j in range(N-1,-1,-1): # 행
            for i in range(N-1,-1,-1): # 열
                if board[i][j] != 0:
                    ni = i
                    nj = j
                    while 1:
                        ni -= 1
                        if 0 <= ni < N and 0 <= nj < N:
                            # 위에 숫자가 나랑 같으면 합침
                            if board[i][j] == board[ni][nj]:
                                board[i][j] += board[ni][nj]
                                board[ni][nj] = 0
                                break

                            # 다른게 있으면 break
                            if board[i][j] != board[ni][nj] and board[ni][nj] != 0:
                                break
                        else:
                            break

                    # 내리기
                    ni = i
                    while 1:
                        ni += 1
                        if ni >= N or board[ni][nj] != 0:
                            board[i][j], board[ni-1][nj] = board[ni-1][nj], board[i][j]
                            break

    print('#{}'.format(tc+1))
    result = list(map(str, board))
    " ".join(result)
    for _ in range(N):
        a = board[_]
        result = list(map(str, a))
        res = " ".join(result)
        print(res)