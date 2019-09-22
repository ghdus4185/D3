import sys
sys.stdin = open('input.txt', 'r')

def perm(n, k, N, t):
    global s

    if n == k:
        if p[0] == p[1] == p[2]:
            s += 1
        if p[0] + 2 == p[1] + 1 == p[2]:
            s += 1

    else:
        for i in range(N):
            if used[i] == 0:
                used[i] = 1
                if t == 1:
                    p[n] = p1[i]
                if t == 2:
                    p[n] = p2[i]
                perm(n+1, k, N, t)
                used[i] = 0

T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    p1 = []
    p2 = []
    k = 3
    p = [0] * k

    for i in range(12):
        if i % 2 == 0:
            s = 0
            p1.append(cards[i])
            if len(p1) >= 3:
                N = len(p1)
                used = [0] * N
                perm(0, 3, N, 1)
                if s > 0:
                    print('#{} 1'.format(tc))
                    break
        else:
            s = 0
            p2.append(cards[i])
            if len(p2) >= 3:
                N = len(p2)
                used = [0] * N
                perm(0, 3, N, 2)
                if s > 0:
                    print('#{} 2'.format(tc))
                    break
    if s == 0:
        print('#{} 0'.format(tc))