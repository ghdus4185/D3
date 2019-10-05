import sys
sys.stdin = open('input.txt', 'r')

def rep(n):
    while p[n] != n:
        n = p[n]
    return n
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    p = [i for i in range(N+1)]
    for i in range(M):
        s, e = map(int, input().split()) # 두 노드가 연결되어있다.
        p[rep(e)] = rep(s)

    cnt = 0
    for i in range(1, N+1):
        if p[i] == i:
            cnt += 1
    print('#{} {}'.format(tc, cnt))