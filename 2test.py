def f(i, N):
    global L
    if i > N:
        print(L)
        for i in range(1, i):
            if L[i] == 1:
                print(i, end=" ")
        print()
    else:
        L[i] = 0
        f(i+1, N)
        L[i] = 1
        f(i+1, N)

N = 5
L = [0] * N
f(0,N)