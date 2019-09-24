def dij(n):
    D = [99999999999]*(n+1)
    D[0] = 0
    for x in adj[0]:
        D[x] = adj[0][x]
    V = [0] * (n+1)
    V[0] = 1
    c = 0
    while c < n:
        minV = 9999999
        minidx = 0
        for i in range(n+1):
            if V[i] == 0 and D[i] < minV:
                minidx = i
                minV = D[i]
        V[minidx] = 1
        for x in adj[minidx]:
            if D[x] > D[minidx]+adj[minidx][]