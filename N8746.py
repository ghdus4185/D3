import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    carrot = [list(map(int, input().split())) for _ in range(N)]
    minV = 1000 * 1000
    for i in range(N):
        for j in range(M):
            p1, p2, p3 = 0, 0, 0
            for k in range(i+1):
                p1 += sum(carrot[k][:j+1])
                p2 += sum(carrot[k][j+1:])
            for k in range(N-1-i):
                p3 += sum(carrot[k+i+1])
            if minV > (abs(p1-p2)+abs(p2-p3)+abs(p3-p1))//2:
                minV = (abs(p1-p2)+abs(p2-p3)+abs(p3-p1))//2
    print('#{} {}'.format(tc, minV))