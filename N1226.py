import sys
sys.stdin = open('input.txt', 'r')

def find(x,y):
    global di, dj, maze, possible, check
    stack = []
    stack.append([x,y])
    while stack:
        n = stack.pop()
        for k in range(4):
            ni = n[0] + di[k]
            nj = n[1] + dj[k]
            # 범위 안에 있는지
            if 0 <= ni < 16 and 0 <= nj < 16:
                if maze[ni][nj] == 3:
                    possible = 1
                    return possible
                if maze[ni][nj] == 0:
                    stack.append([ni, nj])
                    maze[n[0]][n[1]] = 1
    return possible

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
for tc in range(1, 11):
    t = int(input())
    maze = [list(map(int, ' '.join(input()).split())) for _ in range(16)]

    # 시작점 찾기
    res = 0
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                res = 1
                break
        if res == 1:
            break

    check = [[0]*16 for _ in range(16)]
    possible = 0
    find(i, j)

    if possible == 1:
        print('#{} 1'.format(t))
    else:
        print('#{} 0'.format(t))
