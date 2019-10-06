import sys
sys.stdin = open('input.txt', 'r')
# A, B에서 한번 이동할 때 마다 각 충전소랑 거리를 잰다
# pa,pb = [0] * M을 만들고 거리 <= C 이면 pa[i],pb[i]에 가능한 충전소 저장
# for문 2개로 저장된거 모든 경우의 수를 돌리고 가장 큰 값을 선택한다.
def best_choice(x, y):
    global res, maxV
    possible_A, possible_B = [], []
    for i in range(A):
        if abs(x[0]-ap[i][0]) + abs(x[1]-ap[i][1]) <= ap[i][2]:
            possible_A.append(i+1)
        if abs(y[0]-ap[i][0]) + abs(y[1]-ap[i][1]) <= ap[i][2]:
            possible_B.append(i+1)
    if len(possible_A) == 0 and len(possible_B) == 0:
        return
    if len(possible_A) == 0 or len(possible_B) == 0: # 하나라도 충전 가능한게 충전가능한게 없으면
        for i in range(len(possible_A)):
           if maxV < ap[possible_A[i]-1][3]:
               maxV = ap[possible_A[i]-1][3]
        res += maxV
        maxV = 0
        for i in range(len(possible_B)):
           if maxV < ap[possible_B[i]-1][3]:
               maxV = ap[possible_B[i]-1][3]
        res += maxV
        maxV = 0
    else:
        for i in range(len(possible_A)):
            for j in range(len(possible_B)):
                if possible_A[i] == possible_B[j]:
                    if (ap[possible_A[i]-1][3] + ap[possible_B[j]-1][3]) //2 > maxV:
                        maxV = ap[possible_A[i]-1][3]//2 + ap[possible_B[j]-1][3]//2
                else:
                    if ap[possible_A[i]-1][3] + ap[possible_B[j]-1][3] > maxV:
                        maxV = ap[possible_A[i]-1][3] + ap[possible_B[j]-1][3]
        res += maxV
        maxV = 0

T = int(input())
for tc in range(1, T+1):
    M, A = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    b = [0] + list(map(int, input().split()))
    ap = [list(map(int, input().split())) for _ in range(A)]
    loc_a = [1, 1]
    loc_b = [10, 10]
    d = [[0, 0], [0, -1], [1, 0], [0, 1], [-1, 0]]
    # A, B에서 한번 이동할 때 마다 각 충전소랑 거리를 잰다
    res = 0
    for i in range(M+1):
        loc_a[0] += d[a[i]][0]
        loc_a[1] += d[a[i]][1]
        loc_b[0] += d[b[i]][0]
        loc_b[1] += d[b[i]][1]
        maxV = 0
        best_choice(loc_a, loc_b)
    print('#{} {}'.format(tc, res))