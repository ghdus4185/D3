# 순열 생성 (반복)
# for i1 in range(1, 4):
#     for i2 in range(1, 4):
#         if i2 != i1:
#             for i3 in range(1, 4):
#                 if i3 != i1 and i3 != i2:
#                     print(i1, i2, i3)

# 순열 생성 (재귀)
# def perm(n, k, m):
#     if k == n:
#         print(p[:6])
#     else:
#         for i in range(n, m):
#             p[n], p[i] = p[i], p[n]
#             perm(n+1, k, m)
#             p[n], p[i] = p[i], p[n]
# p = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# perm(0, 6, 9)

def perm(n, k, m):
    if k == n:
        print(p[:k])
    else:
        for i in range(n, m):
            p[n], p[i] = p[i], p[n]
            perm(n+1, k, m)
            p[n], p[i] = p[i], p[n]

p = [1,2,3,4,5]
perm(0, 3, 5)
