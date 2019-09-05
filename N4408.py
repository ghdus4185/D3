import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())

    room = []
    for i in range(3):
        if i == 0:
            room.append([1 + (i*2) for i in range(200)])
        if i == 1:
            room.append([0 for i in range(200)])
        if i == 2:
            room.append([2 + (i*2) for i in range(200)])

    for i in range(N):
        sr, dr = map(int, input().split())

        # 홀수일때 인덱스
        if sr % 2 == 1:
            sr = sr // 2
        else:
            sr = sr // 2 - 1
        if dr % 2 == 1:
            dr = dr // 2
        else:
            dr = dr // 2 - 1

        if sr <= dr:
            for i in range(sr, dr+1):
                room[1][i] += 1
        else:
            for i in range(dr,sr+1):
                room[1][i] += 1
    print('#{} {}'.format(tc+1, max(room[1])))