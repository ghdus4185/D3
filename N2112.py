import sys
sys.stdin = open('input.txt', 'r')

def f(n, k, cnt, arr):
    global check, result
    if cnt == i:
        fake = [film[_][:] for _ in range(D)]
        for s in range(2):
            for j in range(i):
                fake[arr[j]] = [s] * W
            ok = 0
            for j in range(W):
                x = 0
                res = 0
                while x+1 != D-1:
                    if fake[x][j] == fake[x+1][j]:
                        a = 2
                        q = 1
                        while x+1+q != D:
                            if fake[x+1][j] == fake[x+1+q][j]:
                                a += 1
                            else:
                                break
                            if a == K:
                                ok += 1
                                res = 1
                                break
                            q += 1
                    if res == 1:
                        break
                    x += 1
                if res == 0:
                    break
            if ok == W:
                if len(arr) != 1:
                    result = len(arr)
                    check = 1
                return
        return
    if n == k:
        return
    if check == 0:
        f(n+1, k, cnt+1, arr+[nums[n]])
        f(n+1, k, cnt, arr)

T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    nums = list(range(D))
    res = 0
    check = 0
    finish = 0
    result = 0
    go = 0
    fake = [film[_][:] for _ in range(D)]
    ok = 0
    for j in range(W):
        x = 0
        res = 0
        while x + 1 != D - 1:
            if fake[x][j] == fake[x + 1][j]:
                a = 2
                q = 1
                while x + 1 + q != D:
                    if fake[x + 1][j] == fake[x + 1 + q][j]:
                        a += 1
                    else:
                        break
                    if a == K:
                        ok += 1
                        res = 1
                        break
                    q += 1
            if res == 1:
                break
            x += 1
        if res == 0:
            break
    if ok == W:
        result = 0
        go = 1
    if go == 0:
        for i in range(1, K+1):
            f(0, D, 0, [])
            if finish == 1:
                break
    print('#{} {}'.format(tc, result))