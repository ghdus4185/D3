import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
d = [[1, 0], [-1, 0], [0, -1], [0, 1]]
for tc in range(1, T+1):
    N = int(input())
    atoms = [list(map(int, input().split())) for _ in range(N)]
    res = 0

    # 부딪힐 리스트를 만들어준다.
    # 나를 제외한 원소들 중에 내가 바라보는 방향쪽에 있으면서 방향이 3가지 중 하나 이면서
    # xi-yi == xj-yj길이가 같은것
    N = len(atoms)
    li = []
    while 1:
        for i in range(N):
            for j in range(N):
                if i != j:
                    if atoms[i][2] == 0: # 방향이 상일때
                        if atoms[i][0] > atoms[j][0]: # 나보다 i가 작으면
                            if atoms[j][2] == 1: # 방향이 반대일때
                                li.append(atoms[i][0] - atoms[j][0])
                            elif atoms[j][2] == 2:
                                if abs(atoms[i][0] - atoms[j][0]) == abs(atoms[i][1] - atoms[j][1]):
                                    li.append(abs(atoms[i][0] - atoms[j][0]))
                            elif atoms[j][2] == 3:
                                if abs(atoms[i][0] - atoms[j][0]) == abs(atoms[i][1] - atoms[j][1]):
                                    li.append(abs(atoms[i][0] - atoms[j][0]))

                    elif atoms[i][2] == 1: # 방향이 하일때
                        if atoms[i][0] > atoms[j][0]: # 나보다 i가 작으면
                            if atoms[j][2] == 0: # 방향이 반대일때
                                li.append(atoms[i][0] - atoms[j][0])
                            elif atoms[j][2] == 2:
                                if abs(atoms[i][0] - atoms[j][0]) == abs(atoms[i][1] - atoms[j][1]):
                                    li.append(abs(atoms[i][0] - atoms[j][0]))
                            elif atoms[j][2] == 3:
                                if abs(atoms[i][0] - atoms[j][0]) == abs(atoms[i][1] - atoms[j][1]):
                                    li.append(abs(atoms[i][0] - atoms[j][0]))

                    elif atoms[i][2] == 2: # 방향이 좌일때
                        if atoms[i][0] > atoms[j][0]: # 나보다 i가 작으면
                            if atoms[j][2] == 3: # 방향이 반대일때
                                li.append(atoms[i][0] - atoms[j][0])
                            elif atoms[j][2] == 1:
                                if abs(atoms[i][0] - atoms[j][0]) == abs(atoms[i][1] - atoms[j][1]):
                                    li.append(abs(atoms[i][0] - atoms[j][0]))
                            elif atoms[j][2] == 2:
                                if abs(atoms[i][0] - atoms[j][0]) == abs(atoms[i][1] - atoms[j][1]):
                                    li.append(abs(atoms[i][0] - atoms[j][0]))

                    elif atoms[i][2] == 3: # 방향이 우일때
                        if atoms[i][0] > atoms[j][0]: # 나보다 i가 작으면
                            if atoms[j][2] == 2: # 방향이 반대일때
                                li.append(atoms[i][0] - atoms[j][0])
                            elif atoms[j][2] == 1:
                                if abs(atoms[i][0] - atoms[j][0]) == abs(atoms[i][1] - atoms[j][1]):
                                    li.append(abs(atoms[i][0] - atoms[j][0]))
                            elif atoms[j][2] == 0:
                                if abs(atoms[i][0] - atoms[j][0]) == abs(atoms[i][1] - atoms[j][1]):
                                    li.append(abs(atoms[i][0] - atoms[j][0]))
    if li != []:
        print(sorted(li))
        atoms.pop()
    else:
        break
    print('#{} {}'.format(tc, res))