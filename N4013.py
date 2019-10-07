# 옮기기 전에 오른쪽이 있으면 내꺼 3이랑 오른쪽 7을 확인한다.
# 왼쪽이 있으면 내꺼 7번 이랑 3번을 확인한다.
# 쭉~~~
# 숫자가 다르면 회전해야한다.


import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    K = int(input())
    gear = [list(map(int, input().split())) for _ in range(4)]
    # 왼쪽을 보고 왼쪽이 회전해야하면 내가 반시계방향 회전일때 왼쪽은 시계 방향 회전한다.
    # 시계 방향 회전이면 반시계방향 회전한다.
    # 오른쪽 : 기준이 반시계 방향 회전이면 오른쪽은 시계 방향
    # 기준이 시계 방향 회전이면 오른쪽은 반시계 방향
    # 시계 방향으로 회전하면 a[0] = a[n-1], a[1~n-1] = a[0~n-2]
    # 시계 반대 방향으로 회전하면 a[n-1] = a[0], a[0~n-2] = a[1~n-1]
    for i in range(K):
        N, C = map(int, input().split())
        t = N
        k = N
        checkr = [0] * 4
        checkl = [0] * 4
        while t < 4:
            if gear[t-1][2] != gear[t][6]:
                checkr[t] = 1
            else:
                break
            t += 1
        while 1 < k:
            if gear[k-1][6] != gear[k-2][2]:
                checkl[k-2] = 1
            else:
                break
            k -= 1
        print(checkr, checkl)
        if C == 1: # 시계 방향으로 회전하면 a[0] = a[n-1], a[1~n-1] = a[0~n-2]
            x = gear[N-1][-1]
            for i in range(1, len(gear[N-1])-1):
                gear[N-1][i] = gear[N-1][i-1]
            gear[N - 1][0] = x
            cnt = 0
            for i in range(len(checkr)):
                if checkr[i] == 1:
                    if cnt % 2 == 0:
                        x = gear[i][0]
                        for j in range(0, len(gear[i])-1):
                            gear[i][j] = gear[i][j+1]
                        gear[i][-1] = x
                    else:
                        x = gear[i][0]
                        for j in range(1, len(gear[i])-1):
                            gear[i][j] = gear[i][j+1]
                        gear[i][0] = x
                    cnt += 1
                if checkl[i] == 1:
                    if cnt % 2 == 0:
                        x = gear[i][0]
                        for j in range(0, len(gear[i])-1):
                            gear[i][j] = gear[i][j+1]
                        gear[i][-1] = x
                    else:
                        x = gear[i][0]
                        for j in range(1, len(gear[i])-1):
                            gear[i][j] = gear[i][j+1]
                        gear[i][0] = x
                    cnt += 1
        else: # 시계 반대 방향으로 회전하면 a[n-1] = a[0], a[0~n-2] = a[1~n-1]
            x = gear[N-1][0]
            for i in range(0, len(gear[N-1])-1):
                gear[N-1][i] = gear[N-1][i+1]
            gear[N-1][-1] = x
            cnt = 0
            for i in range(len(checkl)):
                if checkl[i] == 1:
                    if cnt % 2 == 0:
                        x = gear[i][0]
                        for j in range(1, len(gear[i])-1):
                            gear[i][j] = gear[i][j+1]
                        gear[i][0] = x
                    else:
                        x = gear[i][0]
                        for j in range(0, len(gear[i])-1):
                            gear[i][j] = gear[i][j+1]
                        gear[i][-1] = x
                if checkr[i] == 1:
                    if cnt % 2 == 0:
                        x = gear[i][0]
                        for j in range(1, len(gear[i])-1):
                            gear[i][j] = gear[i][j+1]
                        gear[i][0] = x
                    else:
                        x = gear[i][0]
                        for j in range(0, len(gear[i])-1):
                            gear[i][j] = gear[i][j+1]
                        gear[i][-1] = x

        print(gear)
    res = 0
    for i in range(len(gear)):
        if i == 0:
            if gear[i][0] == 0:
                res += 0
            else:
                res += 1
        elif i == 1:
            if gear[i][0] == 0:
                res += 0
            else:
                res += 2
        elif i == 2:
            if gear[i][0] == 0:
                res += 0
            else:
                res += 4
        elif i == 3:
            if gear[i][0] == 0:
                res += 0
            else:
                res += 8
    print(res)