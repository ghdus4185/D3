import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N개 심사대, M 고객
    t = [int(input()) for _ in range(N)] # 각 심사대의 소요시간
    avg = sum(t) / N
    desk = [0] * N

    # 초기값설정
    num = 0
    for i in range(N):
        if t[i] < avg:
            desk[i] = t[i]
            num += 1
    maxV = 0
    # 모든사람에 대해서 해야함
    for k in range(M-num):
        minT = [100000, 0]
        for i in range(N):
            # 가장 낮은거랑 가장 낮은거에서 2번째꺼를 알고있다가
            # 가장 낮은거에는 채워주고 다음께 들어오면 가장 낮은거+채운거, 가장 낮은거 2번째꺼
            if desk[i] + t[i] < minT[0]:
                minT = [desk[i] + t[i], i]
        desk[minT[1]] = minT[0]
        if maxV < minT[0]:
            maxV = minT[0]
    print('#{} {}'.format(tc, maxV))
