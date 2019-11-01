import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*2001 for _ in range(2001)]
    for i in range(N):
        y, x, dir, e = map(int, input().split())
        arr[x+1000][y+1000] = [dir, e]



    # 0이 아닌걸 찾으면 그 원자가 가지고 있는 방향으로 움직인다.
    # 만약 움직이는 자리가 0이 아니면 충돌해서 사라지게 만들고
    # 두 에너지의 합을 res에 더한다
    res = 0
    cnt = 0
    memory = []
    while cnt < 2000:
        for i in range(2000):
            for j in range(2000):
                if arr[i][j] != 0:
                    ni = i + d[arr[i][j][0]][0]
                    nj = j + d[arr[i][j][0]][1]
                    if 0 <= ni < 2000 and 0 <= nj < 2000:
                        if arr[ni][nj] == 0:
                            arr[ni][nj] = arr[i][j]
                            arr[i][j] = 0
                        else:
                            if [ni, nj] in memory:
                                res += arr[i][j][1] # 부딪히는 모든 원자값을 res에 넣는다.
                                res += arr[i][j][1]
                                memory.append([i, j])
                                arr[i][j] = 0
                                arr[i][j] = 0
                            else:
                                memory.append([i, j])
                                arr[ni][nj] = arr[i][j]
                                arr[i][j] = 0
                    else:
                        arr[i][j] = 0
        memory = []
        cnt += 1
    # x, y, 방향, 에너지
    # 0상, 1하, 2좌, 3우
    # 오른쪽으로 움직이다가 가장 먼저 만나는 원자랑 충돌한다.
    # 0.5초씩 움직이면서
    print('#{} {}'.format(tc, res))
