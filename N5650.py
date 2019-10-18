T = int(input())
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for tc in range(1, T+1):
    N = int(input())
    pin_ball = [list(map(int, input().split())) for _ in range(N)]
    # 들어오는 방향과 벽의 종류에 따라서 이동방향을 바꾼다.
    # 범위를 벗어나면 이동방향을 움직이는 방향 반대 방향으로 바꾼다.
    # 웜홀을 만나면 숫자가 같은 다른 웜홀에서 나온다. (방향은 유지)
    # 블랙홀(-1)을 만나면 게임 끝
    # 벽(1~5)
    # 웜홀 (6~10)
    # score는 벽이나 블록에 부딪힌 횟수
    # 게임판에서 출발위치랑 진행 방향을 임의로 선정할 때
    # 게임에서 얻을 수 있는 최대값을 구하여라

    # 움직일 때 마다 좌표랑 현재 방향을 가지고 움직인다.

    # 웜홀의 위치랑 값을 저장
    check = [0]
    wormhole = []
    for i in range(N):
        for j in range(N):
            if 6 <= pin_ball[i][j] <= 10:
                wormhole.append([pin_ball[i][j], i, j])