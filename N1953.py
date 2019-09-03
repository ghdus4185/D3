import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
di1 = [-1, 0, 1, 0]
dj1 = [0, 1, 0, -1]

di2 = [-1, 1]
dj2 = [0, 0]

di3 = [0, 0]
dj3 = [-1, 1]

di4 = [-1, 0]
dj4 = [0, 1]

di5 = [1, 0]
dj5 = [0, 1]

di6 = [1, 0]
dj6 = [0, -1]

di7 = [-1, 0]
dj7 = [0, -1]

for tc in range(T):
    # N * M 행렬 맨홀뚜껑 세로 : J 가로 : I 탈출 소요 시간: L
    N, M, J, I, L = map(int, input().split())

    tunnel = []
    for i in range(N):
        tunnel.append(list(map(int, input().split())))
    # for j in range(len(tunnel)):
    #     print(tunnel[j])

    # 다른 터널을 만들어준다.
    check = [[0] * M for i in range(N)]
    # 시작점을 빨간색으로 바꿈
    check[I][J] = 'R'

    hour = 0
    cnt = 0
    while hour <= L:
        if tunnel[I][J] == 1:
            for k in range(4):
                ni = I + di1[k]
                nj = J + dj1[k]
                if 0 <= ni < N and 0 <= nj < M:
                    if k == 0:
                        if tunnel[ni][nj] != 0 and tunnel[ni][nj] != 3 and tunnel[ni][nj] != 4 and tunnel[ni][nj] != 7:
                            cnt += 1
                    elif k == 1:
                        if tunnel[ni][nj] != 0 and tunnel[ni][nj] != 2 and tunnel[ni][nj] != 4 and tunnel[ni][nj] != 5:
                            cnt += 1
                            # I = ni
                            # J = nj
                    elif k == 2:
                        if tunnel[ni][nj] != 0 and tunnel[ni][nj] != 3 and tunnel[ni][nj] != 5 and tunnel[ni][nj] != 6:
                            cnt += 1
                            # I = ni
                            # J = nj
                    elif k == 3:
                        if tunnel[ni][nj] != 0 and tunnel[ni][nj] != 2 and tunnel[ni][nj] != 6 and tunnel[ni][nj] != 7:
                            cnt += 1
                        I = ni
                        J = nj

        elif tunnel[I][J] == 2:
            for k in range(2):
                ni = I + di2[k]
                nj = J + dj2[k]
                if 0 <= ni < N and 0 <= nj < M:
                    if k == 0:
                        if tunnel[ni][nj] != 0 and tunnel[ni][nj] != 3 and tunnel[ni][nj] != 4 and tunnel[ni][nj] != 7:
                            cnt += 1
                            # I = ni
                            # J = nj
                    elif k == 1:
                        if tunnel[ni][nj] != 0 and tunnel[ni][nj] != 3 and tunnel[ni][nj] != 5 and tunnel[ni][nj] != 6:
                            cnt += 1
                        I = ni
                        J = nj

        elif tunnel[I][J] == 3:
            for k in range(2):
                ni = I + di3[k]
                nj = J + dj3[k]
                if 0 <= ni < N and 0 <= nj < M:
                    if k == 0:
                        if tunnel[ni][nj] != 0 and tunnel[ni][nj] != 2 and tunnel[ni][nj] != 6 and tunnel[ni][nj] != 7:
                            cnt += 1
                            # I = ni
                            # J = nj
                    elif k == 1:
                        if tunnel[ni][nj] != 0 and tunnel[ni][nj] != 2 and tunnel[ni][nj] != 4 and tunnel[ni][nj] != 5:
                            cnt += 1
                        I = ni
                        J = nj

        elif tunnel[I][J] == 4:
            for k in range(2):
                ni = I + di4[k]
                nj = J + dj4[k]
                if 0 <= ni < N and 0 <= nj < M:
                    if k == 0:
                        if tunnel[ni][nj] != 0 and tunnel[ni][nj] != 3 and tunnel[ni][nj] != 7:
                            cnt += 1
                            # I = ni
                            # J = nj
                    elif k == 1:
                        if tunnel[ni][nj] != 0 and tunnel[ni][nj] != 2 and tunnel[ni][nj] != 5:
                            cnt += 1
                        I = ni
                        J = nj

        elif tunnel[I][J] == 5:
            for k in range(2):
                ni = I + di5[k]
                nj = J + dj5[k]
                if 0 <= ni < N and 0 <= nj < M:
                    if k == 0:
                        if tunnel[ni][nj] != 0 and tunnel[ni][nj] != 3 and tunnel[ni][nj] != 6:
                            cnt += 1
                            # I = ni
                            # J = nj
                    elif k == 1:
                        if tunnel[ni][nj] != 0 and tunnel[ni][nj] != 2 and tunnel[ni][nj] != 4:
                            cnt += 1
                        I = ni
                        J = nj

        elif tunnel[I][J] == 6:
            for k in range(2):
                ni = I + di6[k]
                nj = J + dj6[k]
                if 0 <= ni < N and 0 <= nj < M:
                    if k == 0:
                        if tunnel[ni][nj] != 0 and tunnel[ni][nj] != 3 and tunnel[ni][nj] != 5:
                            cnt += 1
                            # I = ni
                            # J = nj
                    elif k == 1:
                        if tunnel[ni][nj] != 0 and tunnel[ni][nj] != 2 and tunnel[ni][nj] != 7:
                            cnt += 1
                        I = ni
                        J = nj

        elif tunnel[I][J] == 7:
            for k in range(2):
                ni = I + di7[k]
                nj = J + dj7[k]
                if 0 <= ni < N and 0 <= nj < M:
                    if k == 0:
                        if tunnel[ni][nj] != 0 and tunnel[ni][nj] != 3 and tunnel[ni][nj] != 4:
                            cnt += 1
                            # I = ni
                            # J = nj
                    elif k == 1:
                        if tunnel[ni][nj] != 0 and tunnel[ni][nj] != 2 and tunnel[ni][nj] != 6:
                            cnt += 1
                        I = ni
                        J = nj

        hour += 1

    print('#{} {}'.format(tc+1, cnt+1))