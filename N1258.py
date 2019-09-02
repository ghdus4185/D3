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

# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#
#     matrix = [list(map(int, input().split())) for _ in range(N)]
#     idx = []
#     for i in range(N):
#         for j in range(N):
#             save_i, save_j = 0, 0
#             if matrix[i][j] != 0:
#                 for k in range(N):
#                     if matrix[i + k][j] != 0:
#                         save_i += 1
#                     else:
#                         break
#                 for k in range(N):
#                     if matrix[i][j + k] != 0:
#                         save_j += 1
#                     else:
#                         break
#                 for k in range(save_i):
#                     for m in range(save_j):
#                         matrix[i + k][j + m] = 0
#                 idx.append([save_i, save_j, save_i * save_j])
#     count = len(idx)
#     idx.sort(key=lambda x: [x[2], x[0]])
#     print('#{} {}'.format(tc, count), end=' ')
#     for i in range(count):
#         idx[i] = ' '.join(list(map(str, idx[i][:2])))
#         print(idx[i], end=' ')
#     print()
#
# for T in range(int(input())):
#     N = int(input())
#     boxes = [list(map(int, input().split())) for _ in range(N)]
#
#     dangers = []
#     for i in range(N):
#         for j in range(N):
#             if boxes[i][j] != 0:
#                 start, end = [i, j], [i, j]
#                 while True:
#                     ti, tj = end[0], end[1]
#                     ni = ti + 1
#                     if ni < N and boxes[ni][tj] != 0:
#                         end[0] = ni
#                     else:
#                         break
#                 while True:
#                     ti, tj = end[0], end[1]
#                     nj = tj + 1
#                     if nj < N and boxes[ti][nj] != 0:
#                         end[1] = nj
#                     else:
#                         break
#                 for k in range(start[0], end[0] + 1):
#                     boxes[k][start[1]:end[1] + 1] = [0] * (end[1] - start[1] + 1)
#                 dangers.append((end[0] - start[0] + 1, end[1] - start[1] + 1))
#
#     res = []
#     while len(dangers) != 0:
#         danger = dangers.pop(0)
#         if not res:
#             res.append(danger)
#         else:
#             dgsize = int(danger[0]) * int(danger[-1])
#             for re in res:
#                 resize = int(re[0]) * int(re[-1])
#                 if dgsize < resize:
#                     res.insert(res.index(re), danger)
#                     break
#                 elif dgsize == resize:
#                     if int(danger[0]) < int(re[0]):
#                         res.insert(res.index(re), danger)
#                         break
#                 elif re == res[-1]:
#                     res.append(danger)
#                     break
#
#     print('#{} {}'.format(T + 1, len(res)), end=' ')
#     for re in res:
#         print('{} {}'.format(re[0], re[1]), end=' ')
#     print()
#     if matrix[i][j+x] == 0 or i+x == n-1:
#         b = j+x-1
#         break
