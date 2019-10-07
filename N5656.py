import sys
sys.stdin = open('input.txt', 'r')

def ndpr(n, k, N):
    global minV
    if n == k:
        fake = [brick[_][:] for _ in range(H)]
        q = []
        for i in range(k):
            for j in range(H):
                if fake[j][p[i]] != 0:
                    q.append([j, p[i]]) # 구슬에 맞은 벽돌위치부터 시작
                    break
        while q: # 더 깰께 있으면
            a = q.pop(0)
            for i in range(4):
                for j in range(fake[a[0]][a[1]]-1):
                    if fake[a[0]+d[j][0]][a[1]+d[j][1]] != 0:
                        q.append(a[0]+d[j][0], a[1]+d[j][1]) # 그부분에서 다시 깰꺼
                        fake[a[0] + d[j][0]][a[1] + d[j][1]] = 0 # 0으로 바꾼다.
                        if fake[a[0] + d[j][0] - 1][a[1] + d[j][1]] != 0:
                            for m in range(1, H):
                                if a[0] + d[j][0] - 1 - m == 0:
                                    break
                                if fake[a[0] + d[j][0] - 1 - m][a[1] + d[j][1]] == 0:
                                    break
                                else:
                                    fake[a[0] + d[j][0] - m][a[1] + d[j][1]] = fake[a[0] + d[j][0] - 1 - m][a[1] + d[j][1]]
                                    fake[a[0] + d[j][0] - 1 - m][a[1] + d[j][1]] = 0
        res = 0
        for i in range(H):
            for j in range(W):
                if fake[i][j] != 0:
                    res += 1
        if minV > res:
            minV = res

    else:
        for i in range(N):
            # if used[i] == 0:
            #     used[i] = 1
            p[n] = num[i]
            ndpr(n+1, k, N)

d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split()) # N번 쏠 수 있음
    brick = [list(map(int, input().split())) for _ in range(H)] # W * H 배열
    fake = [brick[_][:]for _ in range(H)]
    # for i in range(H):
    #     print(fake[i])
    # 벽돌에 맞으면 적혀있는 칸 만큼 상하좌우로 제거
    # 2이상이면 상하좌우로 n-1칸 제거
    num = [_ for _ in range(W)]
    p = [0] * N
    minV = 1000000000000000000000000000000
    ndpr(0, N, W)
    # 뽑은 중복순열의 모든 결과를 돌리고
    # 부순 갯수가 최대보다 크면 maxV에 넣는다.
    print('#{} {}'.format(tc, minV))
