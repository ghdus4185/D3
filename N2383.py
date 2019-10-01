import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)] # 1은 사람 2는 계단 입구
    # 계단, 사람 위치 저장
    stair = []
    people = []
    for i in range(N):
        for j in range(N):
            if mat[i][j] >= 2:
                stair += [[i, j, mat[i][j]]]
            elif mat[i][j] == 1:
                people += [[i, j]]
    length = []
    # 사람과 가까운 계단과의 거리 저장
    for i in range(len(people)):
        length += [min(abs(people[i][0]-stair[0][0]) + abs(people[i][1]-stair[0][1]), abs(people[i][0]-stair[1][0]) + abs(people[i][1]-stair[1][1]))]
    length.sort()
    print(length)

    # while문으로 1분씩 돌면서
    # 계단에 도착하면 check를 확인해서 0이면 계단 내려갈 수 있음 1이면 계단 못내려감
    check = [0] * 10000000000