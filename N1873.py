import sys
sys.stdin = open('input.txt', 'r')

def move(a):
    global field, di, dj, si, sj, H, W

    if a == 'U':
        # 바라보는 방향을 위로 바꾼다
        field[si][sj] = '^'
        #범위 안에 있고
        if 0 <= si+di[0] < H and 0 <= sj+dj[0] < W:
        # 만약 한칸 위에 칸이 평지라면
            if field[si+di[0]][sj+dj[0]] == '.':
                # 위 칸으로 이동
                field[si][sj] = '.'
                si += di[0]
                sj += dj[0]
                field[si][sj] = '^'
        return
    elif a == 'D':
        field[si][sj] = 'v'
        if 0 <= si+di[1] < H and 0 <= sj+dj[1] < W:
            if field[si+di[1]][sj+dj[1]] == '.':
                field[si][sj] = '.'
                si += di[1]
                sj += dj[1]
                field[si][sj] = 'v'
        return
    elif a == 'L':
        field[si][sj] = '<'
        if 0 <= si+di[2] < H and 0 <= sj+dj[2] < W:
            if field[si+di[2]][sj+dj[2]] == '.':
                field[si][sj] = '.'
                si += di[2]
                sj += dj[2]
                field[si][sj] = '<'
        return
    elif a == 'R':
        field[si][sj] = '>'
        if 0 <= si+di[3] < H and 0 <= sj+dj[3] < W:
            if field[si+di[3]][sj+dj[3]] == '.':
                field[si][sj] = '.'
                si += di[3]
                sj += dj[3]
                field[si][sj] = '>'
        return

def shoot(a):
    global field, di, dj, si, sj, H, W
    ni = si
    nj = sj

    # 바라보는 방향으로 탐색해서
    if field[si][sj] == '^':
        # 위로 쭉 쏜다
        while 1:
            ni += di[0]
            if ni < 0:
                break
            # 돌벽을 만나면 벽을 평지로 바꾸고 종료
            if field[ni][sj] == '*':
                field[ni][sj] = '.'
                break
            # 철벽을 만나면 종료
            if field[ni][sj] == '#':
                break

    elif field[si][sj] == 'v':
        # 밑으로 쭉 쏜다
        while 1:
            ni += di[1]
            if ni >= H:
                break

            if field[ni][sj] == '*':
                field[ni][sj] = '.'
                break

            if field[ni][sj] == '#':
                break
    # 왼쪽으로 쭉 쏜다
    elif field[si][sj] == '<':
        while 1:
            nj += dj[2]
            if nj < 0:
                break
            if field[si][nj] == '*':
                field[si][nj] = '.'
                break

            if field[si][nj] == '#':
                break
    # 오른쪽으로 쭉 쏜다
    elif field[si][sj] == '>':
        while 1:
            nj += dj[3]
            if nj >= W:
                break
            if field[si][nj] == '*':
                field[si][nj] = '.'
                break

            if field[si][nj] == '#':
                break

    return
    # 철벽을 만나면 아무일도 잃어나지 않고 종료

T = int(input())
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
for tc in range(T):
    # H * W 크기
    H, W = map(int, input().split())
    field = [(" ".join(input())).split() for i in range(H)]
    # for i in range(len(field)):
    #     print(field[i])
    N = int(input())
    cmd = input()

    for i in range(H):
        for j in range(W):
            if field[i][j] == '^' or field[i][j] == 'v' or field[i][j] == '<' or field[i][j] == '>':
                si, sj = i, j
                break
    ni, nj = i, j

    for i in cmd:
        if i == 'S':
            shoot(i)
        else:
            move(i)

    # for i in range(len(field)):
    #     print(field[i])
    print('#{} '.format(tc+1), end="")
    for q in range(len(field)):
        print("".join(field[q]))