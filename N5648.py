import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
d = [[1, 0], [-1, 0], [0, -1], [0, 1]]
for tc in range(1, T+1):
    N = int(input())
    atoms = [] # y, x, 방향, 에너지
    for i in range(N):
        x, y, dir, e = map(int, input().split())
        atoms.append([2*x, 2*y, dir, e])
    res = 0
    while 1:
        # 이동
        i = 0
        while i != N:
            atoms[i][1] += d[atoms[i][2]][0] #원자가 가지고 있는 방향으로 이동
            atoms[i][0] += d[atoms[i][2]][1]
            # 벗어나면 pop
            if not -2000 <= atoms[i][1] <= 2000 or not -2000 <= atoms[i][0] <= 2000:
                atoms.pop(i)
                N -= 1
            else:
                i += 1

        # 모든 원자가 이동한 다음에 같은 좌표에 있는 원자를 검사
        used = [0] * N
        for i in range(N):
            if used[i] == 0:
                for j in range(i+1, N):
                    if atoms[i][0] == atoms[j][0] and atoms[i][1] == atoms[j][1]:
                        if used[i] == 0:
                            res += atoms[i][3]
                            used[i] = 1
                        if used[j] == 0:
                            res += atoms[j][3]
                            used[j] = 1

        # 같은 좌표에 있는 원자들을 pop
        i = N-1
        while i != -1:
            if used[i] == 1:
                atoms.pop(i)
                N -= 1
            i -= 1
        if atoms == []:
            break

    print('#{} {}'.format(tc, res))