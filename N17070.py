import sys
sys.stdin = open('input.txt' , 'r')

# r은 행번호 c는 열번호 각 번호는 1부터 시작한다.
def bfs(i, j, status):
    global matrix, N, case

    # 도착점에 닿으면
    if i == N-1 and j == N-1:
        case += 1
        return

    else:# status가 가로일때
        if status == 0:
            for k in range(2):
                ni = i + di1[k]
                nj = j + di1[k]
                if ni < N and nj < N: # 범위에 벗어나지 않고
                    # 우측이 벽이면 갈 수 없음
                    if k == 0 and matrix[ni][nj] == 1:
                        return
                    # staus j + 1 이 벽이면 갈 수 없음
                    elif k == 1 and matrix[i + 1][j] == 1:
                        return
                    # 위에 둘 다 안되고 탐색위치가 0이면
                    # 탐색위치로 이동하고 다시 이동
                    elif matrix[ni][nj] == 0:
                        bfs(ni, nj, status)

        # status가 세로일때
        elif status == 1:
            for k in range(2):
                ni = i + di2[k]
                nj = j + dj2[k]
                if ni < N and nj < N:
                    if k == 0 and matrix[ni][nj] == 1:
                        return
                    elif k == 1 and matrix[i][j+1] == 1:
                        return
                    elif matrix[ni][nj] == 0:
                        bfs(ni, nj, status)

        # status가 대각선일때
        elif status == 2:
            for k in range(3):
                ni = i + di3[k]
                nj = j + dj3[k]
                if ni < N and nj < N:
                    if k == 0 and matrix[ni][nj] == 1:
                        return
                    elif matrix[ni][nj] == 0:
                        bfs(ni, nj, status)






# 갈 수 있는 곳을 숫자로 채운다.
# 진행 상태에 따라
# 가로
di1 = [0, 1]
dj1 = [1, 1]
# 세로
di2 = [1, 1]
dj2 = [0, 1]
# 대각선
di3 = [1, 1, 0]
dj3 = [1, 0, 1]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split()) for _ in range(N))]
# 재귀를 다 써주는데 진입 방향에 따라 갈 수 있는곳을 탐색하고
# 또한 벽이면 가지 못하는걸 고려해준다.
    case = 0
    bfs(0, 1, 0) # 파이프 끝 부분 좌표랑 현재 상태
    print('#{} {}'.format(tc, case))