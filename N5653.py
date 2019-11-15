import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    A = 2 * K + max(N, M)
    cell = [[0] * A for _ in range(A)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                cell[A//2+i][A//2+j] = arr[i][j]

    ori = [[0] for _ in range(A)]
    for i in range(A):
        ori[i] = cell[i][:]

    # X시간동안 비활성화상태 X시간이 지나는 순간 활성 상태
    # 활성 상태가 되면 X시간 살아있을 수 있고 X시간 지나면 세포는 죽는다.
    # 죽은자리에는 복제를 할 수 없다
    # 활성화되면 상하좌우에 번식할 수 있는데 그 자리가 죽은셀이 아니고
    # 세포가 존재하면 안되고 번식하는 생명력 수치가 나보다 낮아야 한다.
    check = [[0] * A for _ in range(A)]
    active = []
    act, num, rn = [], 0, 0
    cnt = 0
    while cnt < K:
        visited = [[0] * A for _ in range(A)]
        q = [] # 모든점에서 복제할 수 있는 곳을 저장
        # 활성화 된게 있으면
        # 4방향으로 옮겨준다.
        for i in range(num):
            if act[i] > 0:
                act[i] -= 1
                if act[i] == 0:
                    rn -= 1
        while active:
            i, j, l = active.pop(0)
            for k in range(4):
                ni = i + d[k][0]
                nj = j + d[k][1]
                if 0 <= ni < A and 0 <= nj < A:
                    # 죽은자리가 아니고 cell이 -1비어있으면
                    if check[ni][nj] == 0 and cell[ni][nj] == 0:
                        # 복제가능 q에 넣는다.
                        q.append([ni, nj, i, j])

        for i in range(A):
            for j in range(A):
                # 1초당 생명력을 하나씩 깎는다
                if cell[i][j] != 0:
                    cell[i][j] -= 1
                    # 생명력이 0이 되면 활성상태로 들어간다.
                    if cell[i][j] == 0 and check[i][j] == 0:
                        check[i][j] = 1
                        active.append([i, j, ori[i][j]])
                        if ori[i][j] >= 2:
                            act.append(ori[i][j])
                            num += 1
                            rn += 1

        # 복제해야 할 모든 것들을 복제
        while q:
            x = q.pop()
            # 복제할 곳의 값과 복제시킬 세포의 생명력중에 큰거를 복제한다.
            if cell[x[0]][x[1]] < ori[x[2]][x[3]]:
                cell[x[0]][x[1]] = ori[x[2]][x[3]]
                ori[x[0]][x[1]] = cell[x[0]][x[1]]

        cnt += 1
    alive = 0
    for i in range(A):
        for j in range(A):
            if cell[i][j] > 0:
                alive += 1
    p = len(active)
    y = 0
    for i in range(p):
        if active[i][2] >= 2:
            y += 1
    # 답 = 비활성화 + 현재 활성화에 들어간것 + 활성화된거중에 아직 살아있는거 - 현재 활성화에 들어간것 중에 생명력이 2이상인것
    res = alive + len(active) + rn - y
    print('#{} {}'.format(tc, res))