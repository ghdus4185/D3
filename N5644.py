import sys
sys.stdin = open('input.txt', 'r')
# A, B에서 한번 이동할 때 마다 각 충전소랑 거리를 잰다
# pa,pb = [0] * M을 만들고 거리 <= C 이면 pa[i],pb[i]에 가능한 충전소 저장
# for문 2개로 저장된거 모든 경우의 수를 돌리고 가장 큰 값을 선택한다.

T = int(input())
for tc in range(1, T+1):
    M, A = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ap = [list(map(int, input().split())) for _ in range(A)]
    start_a = [1, 1]
    start_b = [10, 10]
    pa, pb = [], []
    temp = []
    d = [[0, 0], [0, -1], [1, 0], [0, 1], [-1, 0]]
    # 시작점에서 충전가능한 충전소를 저장
    for j in range(A):
        if abs(start_a[0] - ap[j][0]) + abs(start_a[1] - ap[j][1]) <= ap[j][2]:
            temp.append(j + 1)
        if abs(start_b[0] - ap[j][0]) + abs(start_b[1] - ap[j][1]) <= ap[j][2]:
            temp.append(j + 1)
    pb.append(temp)
    pa.append(temp)
    # A, B에서 한번 이동할 때 마다 각 충전소랑 거리를 잰다
    for i in range(M):
        temp = []
        if a[i] == 0:
            for j in range(A):
                if abs(start_a[0] - ap[j][0]) + abs(start_a[1] - ap[j][1]) <= ap[j][2]:
                    temp.append(j+1)
            pa.append(temp)
        elif a[i] == 1:
            start_a[1] -= 1
            for j in range(A):
                if abs(start_a[0] - ap[j][0]) + abs(start_a[1] - ap[j][1]) <= ap[j][2]:
                    temp.append(j+1)
            pa.append(temp)
        elif a[i] == 2:
            start_a[0] += 1
            for j in range(A):
                if abs(start_a[0] - ap[j][0]) + abs(start_a[1] - ap[j][1]) <= ap[j][2]:
                    temp.append(j+1)
            pa.append(temp)
        elif a[i] == 3:
            start_a[1] += 1
            for j in range(A):
                if abs(start_a[0] - ap[j][0]) + abs(start_a[1] - ap[j][1]) <= ap[j][2]:
                    temp.append(j+1)
            pa.append(temp)
        elif a[i] == 4:
            start_a[0] -= 1
            for j in range(A):
                if abs(start_a[0] - ap[j][0]) + abs(start_a[1] - ap[j][1]) <= ap[j][2]:
                    temp.append(j+1)
            pa.append(temp)

        temp = []
        if b[i] == 0:
            for j in range(A):
                if abs(start_b[0] - ap[j][0]) + abs(start_b[1] - ap[j][1]) <= ap[j][2]:
                    temp.append(j+1)
            pb.append(temp)
        elif b[i] == 1:
            start_b[1] += -1
            for j in range(A):
                if abs(start_b[0] - ap[j][0]) + abs(start_b[1] - ap[j][1]) <= ap[j][2]:
                    temp.append(j+1)
            pb.append(temp)
        elif b[i] == 2:
            start_b[0] += 1
            for j in range(A):
                if abs(start_b[0] - ap[j][0]) + abs(start_b[1] - ap[j][1]) <= ap[j][2]:
                    temp.append(j+1)
            pb.append(temp)
        elif b[i] == 3:
            start_b[1] += 1
            for j in range(A):
                if abs(start_b[0] - ap[j][0]) + abs(start_b[1] - ap[j][1]) <= ap[j][2]:
                    temp.append(j+1)
            pb.append(temp)
        elif b[i] == 4:
            start_b[0] += -1
            for j in range(A):
                if abs(start_b[0] - ap[j][0]) + abs(start_b[1] - ap[j][1]) <= ap[j][2]:
                    temp.append(j+1)
            pb.append(temp)

    res = 0
    for i in range(M+1):
        maxV = 0
        if len(pa[i]) >= 1 and len(pb[i]) == 0: # a가 접속할 수 있는 게 1개 이상 b는 없을 때
            for j in range(len(pa[i])):
                if maxV < ap[pa[i][j]-1][3]:
                    maxV = ap[pa[i][j]-1][3]
        elif len(pb[i]) >= 1 and len(pa[i]) == 0: # b가 접속 할 수 있는 게 1개 이상이고 a는 없을 때
            for j in range(len(pb[i])):
                if maxV < ap[pb[i][j]-1][3]:
                    maxV = ap[pb[i][0]-1][3]
        elif len(pa[i]) == len(pb[i]): # a랑, b의 접속 가능한게 충전소 갯수가 같으면
            for j in range(len(pb[i])):
                for x in range(len(pa[i])):
                    if pb[i][j] == pa[i][x]: # 같은걸 고르면
                        if maxV < (ap[pb[i][j] - 1][3] + ap[pa[i][x] - 1][3]) // 2:
                            maxV = (ap[pb[i][j] - 1][3] + ap[pa[i][x] - 1][3]) // 2
                    else: # 다른걸 고르면
                        if maxV < (ap[pb[i][j] - 1][3] + ap[pa[i][x] - 1][3]):
                            maxV = ap[pb[i][j] - 1][3] + ap[pa[i][x] - 1][3]
        elif len(pa[i]) >= 2 or len(pb[i]) >= 2: # a랑 b의 접속 가능 갯수가 하나라도 2보다 크면
            if len(pa[i]) > len(pb[i]):
                for j in range(len(pb[i])):
                    for x in range(len(pa[i])):
                        if pb[i][j] == pa[i][x]:
                            if maxV < (ap[pb[i][j] - 1][3] + ap[pa[i][x] - 1][3]) // 2:
                                maxV = (ap[pb[i][j] - 1][3] + ap[pa[i][x] - 1][3]) // 2
                        else:
                            if maxV < (ap[pb[i][j] - 1][3] + ap[pa[i][x] - 1][3]):
                                maxV = ap[pb[i][j] - 1][3] + ap[pa[i][x] - 1][3]
            if len(pa[i]) < len(pb[i]):
                for j in range(len(pa[i])):
                    for x in range(len(pb[i])):
                        if pa[i][j] == pb[i][x]:
                            if maxV < (ap[pa[i][j]-1][3] + ap[pb[i][x]-1][3]) // 2:
                                maxV = (ap[pa[i][j] - 1][3] + ap[pb[i][x] - 1][3]) // 2
                        else:
                            if maxV < (ap[pa[i][j]-1][3] + ap[pb[i][x]-1][3]):
                                maxV = ap[pa[i][j]-1][3] + ap[pb[i][x]-1][3]
        res += maxV
    print('#{} {}'.format(tc, res))