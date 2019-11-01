H, W = map(int, input().split())
arr = [(' '.join(input())).split() for _ in range(H)]
c = []
res = [[-1]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if arr[i][j] == 'c':
            res[i][j] = 0
            c.append([i, j])

cnt = 1
while cnt <= W:
    memory = []
    for i in range(H):
        for j in range(W):
            if arr[i][j] != '.':
                nj = j + 1
                if [i, nj] not in c:
                    if nj < W:
                        memory.append([[i, j], [i, nj]])
                    else:
                        arr[i][j] = '.'
    for i in memory:
        arr[i[0][0]][i[0][1]] = '.'
        arr[i[1][0]][i[1][1]] = 'c'
        res[i[1][0]][i[1][1]] = cnt
    cnt += 1
for i in range(H):
    print(' '.join(map(str, res[i][:])))
