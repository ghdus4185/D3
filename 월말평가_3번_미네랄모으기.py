import sys, time
sys.stdin = open('input.txt', 'r')

def f(n, k, s, e, r):
    global maxV
    if s + r < maxV:
        return

    if e >= 0:
        if maxV < s:
            maxV = s
    else:
        return

    if n == k:
        return
    else:
        f(n+1, k, s+mineral[n][2], e-2*loc[n], r - mineral[n][2])
        f(n+1, k, s, e, r - mineral[n][2])


T = int(input())
for tc in range(1, T+1):
    stime = time.time()
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0

    # 각 미네랄과 로봇의 위치 저장
    mineral = []
    r = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 1:
                mineral.append([i, j, arr[i][j]])
                r += arr[i][j]
            elif arr[i][j] == 1:
                robot = [i, j]

    loc = []
    # 로봇과 각 미네랄과의 거리를 저장
    for mi in mineral:
        loc.append(abs(robot[0] - mi[0]) + abs(robot[1] - mi[1]))

    f(0, len(loc), 0, C, r)
    print(maxV)
    print('걸린시간: %.18f'%(time.time()-stime))