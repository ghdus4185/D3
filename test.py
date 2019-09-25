# def npr(n, r, N):
#     if n == r:
#         print(p)
#     else:
#         for i in range(N):
#             if used[i] == 0:
#                 used[i] = 1
#                 p[n] = a[i]
#                 npr(n+1, r, N)
#                 used[i] = 0

def ncr(n, r):
    if r == 0:
        print(p)
    elif n < r:
        return
    else:
        p[r-1] = a[n-1]
        ncr(n-1, r-1)
        ncr(n-1, r)

def ncr(n, r):
    if r == 0:
        print(p)
    elif n < r:
        return
    else:
        p[r-1] = a[n-1]
        ncr(n-1, r-1)
        ncr(n-1, r)


a = [1, 2, 3, 4, 5]
N = 5
r = 2
p = [0] * r
used = [0] * N
# npr(0, r, N)
ncr(N,r)