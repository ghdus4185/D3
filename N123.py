import sys
sys.stdin = open('input.txt', 'r')


def mine_check(x,y):
    global di, dj, mine
    check = 0
    for k in range(8):
        ni = x + di[k]
        nj = y + dj[k]
        # 탐색한 곳이 범위 안인지
        if 0 <= ni < N and 0 <= nj < N:
            # 만약 지뢰가 있다면 지뢰가 있다는 표시 res = 1
            if mine[ni][nj] == '*':
                check += 1
    return check

def change(x,y):
    global di, dj, mine
    check = 0
    for k in range(8):
        ni = x + di[k]
        nj = y + dj[k]
        # 탐색한 곳이 범위 안인지
        if 0 <= ni < N and 0 <= nj < N:
            # 만약 지뢰가 있다면 지뢰가 있다는 표시 res = 1
            if mine[ni][nj] == '*':
                check += 1
    return check

def mine_check(x,y):
    global di, dj, mine
    check = 0
    for k in range(8):
        ni = x + di[k]
        nj = y + dj[k]
        # 탐색한 곳이 범위 안인지
        if 0 <= ni < N and 0 <= nj < N:
            # 만약 지뢰가 있다면 지뢰가 있다는 표시 res = 1
            if mine[ni][nj] == '*':
                check += 1
    return check
di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, - 1, -1]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mine = [' '.join(input()).split() for _ in range(N)]

    click = 0
    q = []
    for i in range(N):
        for j in range(N):
            res = 0
            # 그 자리가 '.'이고
            std = 0
            if mine[i][j] == '.':
                # 8방향 탐색해서
                for k in range(8):
                    ni = i + di[k]
                    nj = j + dj[k]
                    # 탐색한 곳이 범위 안인지
                    if 0 <= ni < N and 0 <= nj < N:
                        std += 1
                        # 만약 지뢰가 있다면 지뢰가 있다는 표시 res = 1
                        if mine[ni][nj] == '*':
                            res = 1
                            break

                # 8방향에 지뢰가 없다면
                if res == 0:
                    q.append([std, i, j])


    # def change(i, j):
    #     global board
    #     global N
    #     dc = [0, 1, 0, -1, 1, 1, -1, -1]
    #     dr = [1, 0, -1, 0, 1, -1, 1, -1]
    #     stack = [[i, j]]
    #     board[i][j] = 0  # 누른 곳 바꾸기
    #     while stack != []:
    #         # print(stack)
    #         col, row = stack.pop()
    #         for k in range(8):
    #             nc = col + dc[k]
    #             nr = row + dr[k]
    #             if 0 <= nc < N and 0 <= nr < N:
    #                 one = check(nc, nr)
    #                 if one == 0 and board[nc][nr] == '.':
    #                     board[nc][nr] = 0
    #                     stack.append([nc, nr])
    #                 else:
    #                     board[nc][nr] = one
    q.sort()
    q.reverse()
    click = 0
    while q:
        t = q.pop(0)
        x = t[1]
        y = t[2]
        if mine[x][y] == '.':
        # x랑 y를 0으로 바꾸고
            mine[x][y] = 0  # x,y를 0으로 바꾸기
            click += 1
            # 8방향 탐색
            for k in range(8):
                ni = x + di[k]
                nj = y + dj[k]
                # 범위 안
                if 0 <= ni < N and 0 <= nj < N:
                    # '.'이고 주변에 지뢰가 없다면 그 좌표로 한번 더 반복
                    sv = mine_check(ni,nj)
                    if mine_check(ni, nj) == 0 and mine[ni][nj] == '.':
                        mine[ni][nj] = 0 # 0 으로 바꾸고 그 좌표에서 다시 시작
                        q = [[0, ni, nj]] + q
                    else:
                        mine[ni][nj] = sv



    # for a in range(N):
    #     print(mine[a])

    dot = 0
    for i in range(N):
        for j in range(N):
            if mine[i][j] == '.':
                dot += 1
    print('#{} {}'.format(tc, click+dot))
# 각 칸에 대해 범위를 넘지 않는 8방향 탐색해서 지뢰가 없고
# 가장 많은 칸을 인접하고 있는 순서대로 click을 한다.
# 나는 숫자 0 으로 표시하고 8방향에 대해 또 8방향 탐색해서 지뢰 개수를 표시한다. count + 1

# 그 다음 많이 인접해 있는 칸을 click


# 8방향에 지뢰가 없는 칸을 다 체크하고
# 남아있는 . 갯수를 count 해서 답에 제출한다.