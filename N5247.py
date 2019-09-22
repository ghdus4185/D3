import sys
sys.stdin = open('input.txt', 'r')

def bfs(n, V):
    q = [0] * 1000001
    check = [0] * 1000001
    r, f = -1, -1
    r += 1
    q[r] = n
    # q.append(n)
    while f != r:
        f += 1
        temp = q[f]
        # temp = q.pop(0)
        if temp == V:
            return check[temp]
        else:
            for i in (temp+1, temp-1, temp*2, temp-10):
                if 0 < i < 1000001:
                    if check[i] == 0:
                        r += 1
                        q[r] = i
                        # q.append(i)
                        check[i] = check[temp] + 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    res = bfs(N, M)
    print('#{} {}'.format(tc, res))