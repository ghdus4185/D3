# 순열
# def npr(n, k, N):
#     if n == k:
#         print(p)
#     else:
#         for i in range(N):
#             if used[i] == 0:
#                 used[i] = 1
#                 p[n] = i + 1
#                 npr(n + 1, k, N)
#                 used[i] = 0
#
# N = int(input())
#
# used = [0] * N
# k = 2
# p = [0] * k
# npr(0, k, N)

# def npr(n, k, N):
#     if n == k:
#         print(p)
#     else:
#         for i in range(N):
#             if used[i] == 0:
#                 used[i] = 1
#                 p[n] = i+1
#                 npr(n+1, k, N)
#                 used[i] = 0
# N = 5
# k = 2
# used = [0] * N
# p = [0] * k
# npr(0, k, N)



def npr(n, k, N):
    if n == k:
        print(p)
    else:
        for i in range(N):
            if used[i] == 0:
                used[i] = 1
                p[n] = i+1
                npr(n+1, k, N)
                used[i] = 0
a = ['+', '+', '-', '/']
used = [0] * 3
p = [0] * 3
npr(0, 3, 3)

# h = [1, 2, 3, 4, 5]
# sub_list = []
# for i in range(2**N):
#     res = []
#     for j in range(N):
#         if i & (1 << j) != 0:
#             res += [h[j]]
#             # print(res)
#     if len(res) == k:
#         sub_list.append(res)
#         res = []
# print(sub_list)
