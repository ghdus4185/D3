import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
d = [[1, 0], [-1, 0], [0, -1], [0, 1]]
for tc in range(1, T+1):
    N = int(input())
    atoms = [list(map(int, input().split())) for _ in range(N)]
    res = 0
    while 1:
        # 이동
        for atom in atoms:
            atom[1] += d[atom[2]][0]
            atom[0] += d[atom[2]][1]
            # 벗어나면 pop
            if not -2000 <= atom[1] <= 2000:
                atoms.pop(atoms.index(atom))
            if not -2000 <= atom[0] <= 2000:
                atoms.pop(atoms.index(atom))
        N = len(atoms)
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

        # 충돌한것들 pop
        for i in range(N-1, -1, -1):
            if used[i] == 1:
                atoms.pop(i)
        if atoms == []:
            break
    print('#{} {}'.format(tc, res))