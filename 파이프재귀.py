import sys
sys.stdin = open('input.txt', 'r')

"""
TastCase 16 번까지는 정답 확인
백준에서는 시간초과 뜸
"""

def f(r, c, direction):
    global cnt, base, N

    if r == N - 1 and c == N - 1:
        cnt += 1
        return

    else:
        if direction == 0: # 가로로 놓여져 있는 경우
            for k in 0, 2: # 가로 일때 탐색
                nr = r + dr[k]
                nc = c + dc[k]
                if nr < N and nc < N: # 탐색한 곳이 범위 안이면
                    if k == 0 and base[nr][nc] == 1:
                        return
                    elif k == 2 and base[r + 1][c] == 1:
                        return
                    elif base[nr][nc] == 0:
                        f(nr, nc, k)
        elif direction == 1: # 세로로 놓여져 있는 경우
            for k in 1, 2:
                nr = r + dr[k]
                nc = c + dc[k]
                if nr < N and nc < N:
                    if k == 1 and base[nr][nc] == 1:
                        return
                    elif k == 2 and base[r][c + 1] == 1:
                        return
                    elif base[nr][nc] == 0:
                        f(nr, nc, k)
        elif direction == 2: # 대각선으로 놓여져 있는 경우
            for k in range(2, -1, -1):
                nr = r + dr[k]
                nc = c + dc[k]
                if nr < N and nc < N:
                    if k == 2 and base[nr][nc] == 1:
                        return
                    elif base[nr][nc] == 0:
                        f(nr, nc, k)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    base = [list(map(int, input().split())) for _ in range(N)]
    # 밀수 있는 방향 가로(0), 세로(1), 대각선(2)
    # 초기 조건 무조건 가로로 놓여져 있음
    dr = [0, 1, 1]
    dc = [1, 0, 1]
    cnt = 0 # 파이프 이동 가능 경로를 저장할 변수
    # 밀수 있는 방향 가로(0), 세로(1), 대각선(2)
    # 초기 조건 무조건 가로로 놓여져 있음
    f(0, 1, 0) # 파이프 끝, 놓여져 있는 방향
    print('#{} {}'.format(tc, cnt))