# 첫번째 줄 첫번째 칸에 둔다.
# 2번째줄 가능한 칸 모두 둔다.
# 쭉 내려가다가 둘 수 없는 줄이 나오면 return
def q(i, N):
    global cnt

    if i == N:
        cnt += 1
    else:
        for j in range(N):
            if col[j] == 0 and right[i+j] == 0 and left[i-j+N-1] == 0:
            # 다른 줄에 j번 열에 퀸이 없어야 하고
            # 왼쪽 대각선과 오른쪽 대각선에 퀸이 없어야 한다.
                board[i][j] = 1 # 같은 줄에 퀸이 없어야 하고
                col[j] = 1 # 현재 줄에서 j열을 사용함으로 표시
                right[i+j] = 1
                left[i-j+N-1] = 1
                q(i+1, N) # j열에 놓을 수 있으면 다음 줄로 이동
                board[i][j] = 0  # 같은 줄에 퀸이 없어야 하고
                col[j] = 0  # 현재 줄에서 j열을 사용함으로 표시
                right[i + j] = 0
                left[i - j + N - 1] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [[0]*N for i in range(N)]
    col = [0] * N
    right = [0] * (N * 2-1)
    left = [0] * (N * 2-1)
    cnt = 0
    q(0, N)
    print('#{} {}'.format(tc, cnt))