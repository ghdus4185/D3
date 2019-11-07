import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for tc in range(1, T+1):
    N = int(input())
    atoms = [list(map(int, input().split())) for _ in range(N)] # y, x, dir, e
    # 1초 마다 가지고 있는 방향으로 움직인다.
    # 다 움직이고 만약에 같은 위치가 있는것들은 pop하면서 에너지를 res에 더한다.
    cnt = 0
    res = 0
    while cnt < 2000:
        for atom in atoms:
            atom[0] += d[atom[2]][0]
            atom[1] += d[atom[2]][1]
        memory = []
        for atom in atoms:
            check = 0
            for at in atoms:
                if atom != at:
                    if atom[0] == at[0] and atom[1] == at[1]:
                        res += at[3]
                        atoms.pop(atoms.index(at))
                        check = 1
            if check == 1:
                res += atom[3]
                atoms.pop(atoms.index(atom))
        cnt += 1
    # x, y, 방향, 에너지
    # 0상, 1하, 2좌, 3우
    # 오른쪽으로 움직이다가 가장 먼저 만나는 원자랑 충돌한다.
    # 0.5초씩 움직이면서
    print('#{} {}'.format(tc, res))