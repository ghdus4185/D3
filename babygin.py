# 순열 생성 (재귀)
def perm(n, k):
    if k == n:
        run = 0
        tri = 0
        if p[0] == p[1] == p[2]:
            tri += 1
        if p[3] == p[4] == p[5]:
            tri += 1
        if int(p[0]) + 2 == int(p[1]) + 1 == int(p[2]):
            run += 1
        if int(p[3]) + 2 == int(p[4]) + 1 == int(p[5]):
            run += 1

        if run + tri == 2:
            print('babygin')

    else:
        for i in range(n, k):
            p[n], p[i] = p[i], p[n]
            perm(n+1, k)
            p[n], p[i] = p[i], p[n]
p = list(input())
perm(0, 6)