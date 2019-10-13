import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    desert = [list(map(int, input().split())) for _ in range(N)]
    # 카페는 대각선끼리 움직일 수 있다.
    # 랜덤 한 카페에서 출발해서 사각형 모양을 그리고 돌아온다
    # 투어 중 같은 종류를 먹으면 안된다.
    # 투어 길이는 1개일 수 없다.
    # 왔던 길을 돌아갈 수 없다.
    # 디저트를 가장 많이 먹을 수 있는 경로를 찾고
    # 디저트의 수 출력
    # 만약 디저트를 먹을 수 없는 경우는 -1을 출력
    d = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
    maxV = 0
    end = 0
    # N*N 행렬을 3*3~N*N행렬로 나눠서 푼다.
    for k in range(N-3, -1, -1):
        for i in range(N-2-k):
            for j in range(N-2-k):
                fake = [desert[_+i][j:j+3+k] for _ in range(3+k)]

                # 이렇게 만든 fake로 최대한 길게 사각형 검사를 해본다.
                for m in range(1+k): # 3+k 행렬
                    res = []
                    x = 0
                    y = 1 + m
                    res.append(fake[x][y])
                    # 한점에서 시작해서 4방향으로 가장 멀리 보내본다
                    # res 안에 있는게 나오면 모두 break
                    #
                    for p in range(4):
                        all = 0
                        while 1:
                            x += d[p][0]
                            y += d[p][1]
                            if 0 <= x <= k+2 and 0 <= y <= k+2:
                                if x == 0 and y == 1 + m:
                                    all = 1
                                    break
                                if fake[x][y] not in res:
                                    res.append(fake[x][y])
                                else: # 만약 res안에 있으면
                                    all = 1
                                    res = []
                                    break
                            else:
                                x -= d[p][0]
                                y -= d[p][1]
                                break

                        if all == 1:
                            break
                    # 최대인지 확인
                    if maxV < len(res):
                        maxV = len(res)
                        end = 1
                        break
                if end == 1:
                    break
            if end == 1:
                break
        if end == 1:
            break
    if maxV == 0:
        maxV = -1
    print('#{} {}'.format(tc, maxV))