# 처음 파이프는 (1,1) - (1,2) 가로로 있다.
# (N,N)에 도착하는 방법의 수는 ?
import sys
sys.stdin = open('파이프.txt', 'r')

def direction(i,j,N,start_Direction):
    global cnt

    if i == N-1 and j == N-1 and arr[N-1][N-1] == 0:
        cnt += 1

        # k = 0 이면 오른쪽. k = 1이면 대각선. k = 2이면 아래
    elif start_Direction == 0:
        for k in range(2):
            ni = i + di0[k]
            nj = j + dj0[k]
            if ni >= 0 and nj >= 0 and ni < N and nj < N:
                if arr[ni][nj] == 0:
                    if k == 1 and arr[i+1][j] == 0:
                        direction(ni,nj,N,k)
                    elif k == 0:
                        direction(ni,nj,N,k)

    elif start_Direction == 1:
        for k in range(3):
            ni = i + di1[k]
            nj = j + dj1[k]
            if ni >= 0 and nj >= 0 and ni < N and nj <N and arr[ni][nj] == 0:
                if i+1 != N and arr[i+1][j] == 0:
                    direction(ni,nj,N,k)
                elif i+1 == N:
                    direction(ni,nj,N,k)

    elif start_Direction == 2:
        for k in range(2):
            ni = i + di2[k]
            nj = j + dj2[k]
            if ni >= 0 and nj >= 0 and ni < N and nj <N and arr[ni][nj] == 0 and arr[i+1][j] == 0:
                direction(ni, nj, N, k+1)


# → ↘ ↓ 순서
di0 = [0,1]
dj0 = [1,1]

di1 = [0,1,1]
dj1 = [1,1,0]

di2 = [1,1]
dj2 = [1,0]


N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
cnt = 0

direction(0,1,N,0)
print(cnt)