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

N = int(input())

used = [0] * N
k = 3
p = [0] * k
npr(0, k, N)