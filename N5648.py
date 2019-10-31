import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*2000 for _ in range(2000)]
    for i in range(N):
        y, x, dir, e = map(int, input().split())
        arr[x][y] = [dir, e]
    cnt = 0
    while 1:
        cnt += 0.5
    # x, y, 방향, 에너지
    # 0상, 1하, 2좌, 3우
    # 오른쪽으로 움직이다가 가장 먼저 만나는 원자랑 충돌한다.
    # 0.5초씩 움직이면서
    print(arr)