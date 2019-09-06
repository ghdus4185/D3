import sys
sys.stdin = open('input.txt', 'r')

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, - 1, -1]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mine = [' '.join(input()).split() for _ in range(N)]

    click = 0
    for i in range(N):
        for j in range(N):
            res = 0
            # 그 자리가 지뢰가 아니라면
            if mine[i][j] != '*':
                # 8방향 탐색해서
                for k in range(8):
                    ni = i + di[k]
                    nj = j + dj[k]
                    # 탐색한 곳이 범위 안인지
                    if 0 <= ni < N and 0 <= nj < N:
                        # 만약 지뢰가 있다면 지뢰가 있다는 표시 res = 1
                        if mine[ni][nj] == '*':
                            res = 1
                            break
                # 8방향에 지뢰가 없다면
                if res == 0 and mine[i][j] == '.':
                    # 0을 표시
                    mine[i][j] = '0'
                    click += 1
                    # 다시 그 기준 8방향의 8방향을 탐색
                    for m in range(8):
                        ni = i + di[m]
                        nj = j + dj[m]
                        if 0 <= ni < N and 0 <= nj < N:
                            num_mine = 0
                            for n in range(8):
                                nni = ni + di[n]
                                nnj = nj + dj[n]
                                if 0 <= nni < N and 0 <= nnj < N:
                                    if mine[nni][nnj] == '*':
                                        num_mine += 1
                                mine[ni][nj] = num_mine
    for a in range(N):
        print(mine[a])

    for i in range(N):
        for j in range(N):
            if mine[i][j] == '.':
                click += 1
    print('#{} {}'.format(tc, click))
# 각 칸에 대해 범위를 넘지 않는 8방향 탐색해서 지뢰가 없고
# 가장 많은 칸을 인접하고 있는 순서대로 click을 한다.
# 나는 숫자 0 으로 표시하고 8방향에 대해 또 8방향 탐색해서 지뢰 개수를 표시한다. count + 1

# 그 다음 많이 인접해 있는 칸을 click


# 8방향에 지뢰가 없는 칸을 다 체크하고
# 남아있는 . 갯수를 count 해서 답에 제출한다.