import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(T):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    res = []
    final = []
    cnt = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                end_i, end_j = 0, 0
                if matrix[i][j] != 0:
                    for x in range(n):
                        if matrix[i+x][j] != 0:
                            end_i += 1
                        else:
                            break
                    for k in range(n):
                        if matrix[i][j + k] != 0:
                            end_j += 1
                        else:
                            break

                    for k in range(end_i):
                        for m in range(end_j):
                            matrix[i + k][j + m] = 0
                    res.append([end_i, end_j, end_i * end_j])

    count = len(res)
    res.sort(key=lambda x: [x[2], x[0]])
    print('#{} {}'.format(tc+1, count), end=' ')
    for i in range(count):
        res[i] = ' '.join(list(map(str, res[i][:2])))
        print(res[i], end=' ')
    print()
