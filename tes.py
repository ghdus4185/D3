import sys
sys.stdin = open('input.txt', 'r')

def dfs(x, y, d, c):
    global minV, location
    if d >= minV:
        return
    else:
        if 0 not in c:
            last = abs(location[2]-x) + abs(location[3]-y)
            a = d + last
            if minV > a:
                minV = a
        else:
            cnt = 0
            for i in c:
                if i == 0:
                    c[cnt] = 1
                    di = abs(x - location[4+(2*cnt)]) + abs(y - location[4+(2*cnt)+1])
                    dfs(location[4+(2*cnt)], location[4+(2*cnt)+1], d+di, c)
                    c[cnt] = 0
                cnt += 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    location = list(map(int, input().split()))
    cx, cy = location[0], location[1]
    hx, hy = location[2], location[3]
    distance = 0
    minV = 10000
    check = [0] * N
    dfs(cx, cy, distance, check)
    print('#{} {}'.format(tc, minV))