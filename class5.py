def find(N):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    D = [[100000000000000000000] * N for i in range(N)]
    D[0][0] = 0
    q = []
    q.append((0,0))
    while q:
        t = q.pop(0)
        for i in range(4):
            r = t[0] + dr[i]
            c = t[1] + dc[i]
            if r >= 0 and r < N and c >= 0 and c < N:
                diff = 0
                if H[r][c] > H[t[0]][t[1]]:
                    diff = H[r][c] - H[t[0]][t[1]]
                if D[r][c] > D[t[0]][t[1]] + diff + 1:
                    D[r][c]
