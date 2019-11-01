import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    cell = [list(map(int, input().split())) for _ in range(N)]
    field = [[0] * 1000 for _ in range(1000)]
    r = 650//2
    for i in range(N):
        for j in range(M):
            if cell[i][j] != 0:
                field[i+500][j+500] = cell[i][j]
    # X시간동안 비활성화상태 X시간이 지나는 순간 활성 상태
    # 활성 상태가 되면 X시간 살아있을 수 있고 X시간 지나면 세포는 죽는다.
    # 죽은자리에는 복제를 할 수 없다
    # 활성화되면 상하좌우에 번식할 수 있는데 그 자리가 죽은셀이 아니고
    # 세포가 존재하면 안되고 번식하는 생명력 수치가 나보다 낮아야 한다.

    cnt = 0
    while cnt <= K:
        for i in range(K):
            pass
        cnt += 1