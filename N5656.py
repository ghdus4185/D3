import sys
sys.stdin = open('input.txt', 'r')

def ndpr(n, k, N):
    global minV

    if minV == 0:
        return

    if n == k:
        fake = [brick[_][:] for _ in range(H)]
        q = []
        for i in range(k):
            for j in range(H):
                if fake[j][p[i]] != 0:
                    q.append([j, p[i], fake[j][p[i]]])
                    break
            # 뿌시기
            while q:
                a = q.pop(0)
                for i in range(4):
                    fake[a[0]][a[1]] = 0
                    for j in range(1, a[2]):
                        x = a[0]+(d[i][0])*j
                        y = a[1]+(d[i][1])*j
                        if 0 <= x < H and 0 <= y < W:
                            if fake[x][y] != 0:
                                q.append([x, y, fake[x][y]])
                                fake[x][y] = 0
            # 내리기
            for w in range(H-1, -1, -1):
                for r in range(W-1, -1, -1):
                    if fake[w][r] == 0:
                        u = 1
                        while w-u >= 0:
                            if fake[w-u][r] != 0:
                                fake[w][r] = fake[w-u][r]
                                fake[w - u][r] = 0
                                break
                            u += 1
        res = 0
        for i in range(H):
            for j in range(W):
                if fake[i][j] != 0:
                    res += 1
        if minV > res:
            minV = res

    else:
        for i in range(N):
            p[n] = num[i]
            ndpr(n+1, k, N)

d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    brick = [list(map(int, input().split())) for _ in range(H)]
    fake = [brick[_][:]for _ in range(H)]

    num = [_ for _ in range(W)]
    p = [0] * N
    minV = 1000000000000000000000000000000
    ndpr(0, N, W)
    print('#{} {}'.format(tc, minV))