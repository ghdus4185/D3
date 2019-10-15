import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M, K, A, B = map(int, input().split()) # 접수, 정비, 고객, 이용접수, 이용정비
    a = list(map(int, input().split())) # 고장접수시간
    b = list(map(int, input().split())) # 정비시간
    t = list(map(int, input().split())) # 정비소 방문시간
    register = [[0, 0, 0] for _ in range(N)]
    repair = [[0, 0, 0] for _ in range(M)]
    check = [0] * K
    wait_register = []
    wait_repair = []
    res = []
    result = []
    p1, p2 = [0]*N, [0]*M
    # 0초부터 1000초까지
    for tk in range(10000):
        # 접수 시간 감소
        for i in range(N):
            if 1 not in p1:
                break
            if register[i][0] != 0:
                register[i][0] -= 1
                # 접수처리가 끝난사람은 wait_repair에 저장.
                if register[i][0] == 0: # 같은 시간에 동시에 끝나면 접수창구번호가 작은 순으로 정비
                    wait_repair.append([register[i][1], i+1, tk]) # n번사람, 몇번 창구 이용했는지 저장
                    sorted(wait_repair, key=lambda x: (x[2], x[1])) # 창구 기준으로 오름차순 정렬
                    p1[i] = 0

        # 정비 시간 감소
        for i in range(M):
            if 1 not in p2:
                break
            if repair[i][0] != 0:
                repair[i][0] -= 1
                if repair[i][0] == 0:
                    p2[i] = 0

        # 시간초보다 같거나 작은데 아직 처리 안했으면
        for i in range(K):
            if tk >= t[i] and check[i] == 0:
                check[i] = 1
                wait_register.append(i+1) # n번째 사람을 넣는다.

        # 기다리는사람이 있고 접수하는사람이 비어있으면 접수시키고 처리 시간만큼 준다.
        while wait_register:
            if 0 not in p1:
                break
            for i in range(N): # i 번째 register
                if register[i][0] == 0 and p1[i] == 0:
                    # 시간, n번째사람, 이용칸
                    register[i][0], register[i][1], register[i][2] = [a[i], wait_register.pop(0), i+1]
                    if i == A-1:
                        if register[i][1] not in res:
                            res.append(register[i][1])
                    p1[i] = 1
                    if wait_register == []:
                        break
                    if 0 not in p1:
                        break

        while wait_repair:
            if 0 not in p2:
                break
            for i in range(M):
                if repair[i][0] == 0 and p2[i] == 0:
                    repair[i][0], repair[i][1], repair[i][2] = [b[i], wait_repair.pop(0)[0], i+1]
                    if i == B-1:
                        if repair[i][1] in res:
                            if repair[i][1] not in result:
                                result.append(repair[i][1])
                    p2[i] = 1
                    if wait_repair == []:
                        break
                    if 0 not in p2:
                        break
    if result == []:
        print('#{} {}'.format(tc, -1))
    else:
        print('#{} {}'.format(tc, sum(result)))