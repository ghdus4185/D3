import sys
sys.stdin = open('input.txt', 'r')
#조합
def f(n, k, cnt, arr):
    global finish, result
    if cnt == i:
        # print(arr)
        L = len(arr)
        ndpr(0, L, [0] * L, arr) # 중복순열 만들고 바꾼다.
        return
    if n == k:
        return
    if finish == 0:
        f(n+1, k, cnt+1, arr+[nums[n]])
        f(n+1, k, cnt, arr)
    else:
        return

# 바꿀 열들을 만들고 그 열을 중복순열로 바꾼다.
def ndpr(n, k, R, arr):
    global finish
    if n == k:
        if finish == 0:
            # print(R)
            fake = [film[_][:] for _ in range(D)]
            for i in range(k):
                fake[arr[i]] = [R[i]] * W
            # 검사
            test(fake, arr)
        return
    else:
        if finish == 0:
            for i in range(2):
                R[n] = i
                ndpr(n+1, k, R, arr)
        else:
             return
# 검사
def test(fake, arr):
    global result, finish
    ok = 0
    for j in range(W):
        x = 0
        res = 0
        while x + 1 != D:
            a = 1
            if fake[x][j] == fake[x + 1][j]:
                a += 1
                if a == K:
                    ok += 1
                    res = 1
                    break
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
        result = len(arr)
        finish = 1
        return

T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    nums = list(range(D))
    finish = 0
    result = 0
    test(film, [])

    if finish == 0:
        for i in range(1, K+1):
            f(0, D, 0, [])
            if finish == 1:
                break
    print('#{} {}'.format(tc, result))