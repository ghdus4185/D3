import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())

    bug = []
    for i in range(K):
        I, J, n, d = (map(int, input().split()))
        bug.append([I, J, n, d])

    hour = 0
    while hour < M:
        for i in range(len(bug)):
            I, J, n, d = bug[i][0], bug[i][1], bug[i][2], bug[i][3]
            # 상
            if d == 1:
                # 약품을 만나면
                if I - 1 == 0:
                    # 미생물 수를 반으로 줄이고 방향 바꿈
                    bug[i][2] = bug[i][2] // 2
                    bug[i][3] = 2
                #만나지 않으면 위로 이동
                bug[i][0] -= 1

            # 하
            elif d == 2:
                if I + 1 == N - 1:
                    bug[i][2] = bug[i][2] // 2
                    bug[i][3] = 1
                bug[i][0] += 1
            #좌
            elif d == 3:
                if J - 1 == 0:
                    bug[i][2] = bug[i][2] // 2
                    bug[i][3] = 4
                bug[i][1] -= 1
            #우
            elif d == 4:
                if J + 1 == N - 1:
                    bug[i][2] = bug[i][2] // 2
                    bug[i][3] = 3
                bug[i][1] += 1

        bug.sort() # 좌표가 같을 때 미생물 수가 큰거에 합치기 위함
        i = 0
        while i < len(bug) - 1:
            if bug[i][0] == bug[i+1][0] and bug[i][1] == bug[i+1][1]:
                bug[i+1][2] += bug[i][2]
                bug.pop(i)
                i = i
                # i += 1 을 안하는 이유는 pop하면서 index가 i+1번째 index가 i번째 index로 옮겨짐
                # 다시 i번째 부터 같은게 있는지 검사
            else:
                i += 1

        hour += 1

    res = 0
    for k in range(len(bug)):
        res += bug[k][2]
    print('#{} {}'.format(tc+1, res))