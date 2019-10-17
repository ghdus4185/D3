import sys
sys.stdin = open('input.txt', 'r')

def ndpr(n,k):
    global minV
    if n == k:
        print(dp)
        length = [0] * p
        for i in range(p):
            length[i] = [(abs(people[i][0] - stair[dp[i]-1][0]) + abs(people[i][1] - stair[dp[i]-1][1])), dp[i], stair[dp[i]-1][2]]
        length.sort()
        # while문으로 1분씩 돌면서
        # 한번에 3명 내려가고 있으면 체크를 1로 바꿈
        # 계단에 도착하면 check를 확인해서 0이면 계단 내려갈 수 있음 1이면 계단 못내려감
        check = [0] * 2
        # 모든사람이 계단을 다 내려가면 종료
        finish = [0] * p
        sec = 1
        wait1, wait2 = [], [] # 큐
        w1, w2 = [0]*3, [0]*3
        c1, c2 = 0, 0
        f = 0
        while f < 6:
            for i in range(3):
                if w1[i] != 0:
                    w1[i] -= 1
                    if w1[i] == 0:
                        c1 -= 1
                        check[0] = 0
                        f += 1
                if w2[i] != 0:
                    w2[i] -= 1
                    if w2[i] == 0:
                        c2 -= 1
                        check[1] = 0

            for i in range(p): # 사람 수 만큼
                if length[i][0] >= 2: # 계단까지거리가 2보다 크면
                    length[i][0] -= 1
                elif length[i][0] == 1:
                    length[i][0] -= 1
                    if length[i][1] == 1:
                        wait1.append(length[i][2])
                    else:
                        wait2.append(length[i][2])
            if wait1: # 첫번째 계단에 기다리는사람이있으면
                for i in range(len(wait1)):
                    if check[0] == 0: # 계단 확인
                        for i in range(3):
                            if not wait1:
                                break
                            if w1[i] == 0:
                                w1[i] = wait1.pop(0)
                        c1 += 1
                        if c1 == 3:
                            check[0] = 1
                            break
                    else:
                        break
            if wait2: # 두번째 계단에 기다리는사람이있으면
                for i in range(len(wait2)):
                    if check[1] == 0: # 계단 확인
                        for i in range(3):
                            if not wait2:
                                break
                            if w2[i] == 0:
                                w2[i] = wait2.pop(0)
                        c2 += 1
                        if c2 == 3:
                            check[0] = 1
                            break
                    else:
                        break
            sec += 1
        if minV > sec - 1:
            minV = sec - 1

    else:
        for i in range(2):
            dp[n] = a[i]
            ndpr(n+1, k)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)] # 1은 사람 2는 계단 입구
    # 계단, 사람 위치 저장
    stair, people, length = [], [], []
    p = 0
    minV = 1000000000000000000
    for i in range(N):
        for j in range(N):
            if mat[i][j] >= 2:
                stair += [[i, j, mat[i][j]]]
            elif mat[i][j] == 1:
                people += [[i, j]]
                p += 1
    a = [1, 2]
    dp = [0] * p
    ndpr(0, p)
    print(minV)
    # 사람과 모든 계단거리를 비교해서 가장 가까운 거리랑 그 계단번호 저장
    # for i in range(p):
    #     min_length = 10000
    #     for j in range(len(stair)):
    #         if min_length > abs(people[i][0] - stair[j][0]) + abs(people[i][1] - stair[j][1]):
    #             min_length = abs(people[i][0] - stair[j][0]) + abs(people[i][1] - stair[j][1])
    #             idx = stair[j][3] # 계단 번호
    #     length.append([min_length, idx])
    # length.sort()
    # print(length)

