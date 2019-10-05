# 순열
def npr(n, k, N):
    if n == k:
        print(p)
    else:
        for i in range(N):
            if used[i] == 0:
                used[i] = 1
                p[n] = i + 1
                npr(n + 1, k, N)
                used[i] = 0
<<<<<<< HEAD
a = ['+', '+', '-', '/']
used = [0] * 3
p = [0] * 3
npr(0, 3, 3)
=======

N = 5
used = [0] * N
k = 2
p = [0] * k
npr(0, k, N)
>>>>>>> 4ee2d411400f7fd5d8fe2c48e2315d94543ab0fa

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