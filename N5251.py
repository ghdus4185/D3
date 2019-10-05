import sys
sys.stdin = open('input.txt', 'r')

inf = float('INF')

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())

    # 무한대 값 저장
    arr = [[inf]*(N+1) for i in range(N+1)]

    # 자신으로 가는 값은 0
    for i in range(N+1):
        arr[i][i] = 0

    # 가중치
    for i in range(E):
        x, y, d = map(int, input().split())
        arr[x][y] = d

    # 정점들
    V = [i for i in range(N+1)]

    # 선택한 정점 추가
    U = [0]

    D = []
    for i in range(N+1):
        D.append(arr[0][i])

    while sorted(U) != V:
        s = float('INF')

        for i in range(N+1):
            if not i in U:
                if D[i] != 0 and D[i] < s:
                    s = D[i]
                    w = i
        U.append(w)

        for v in range(N+1):
            if arr[w][v] != 0 and arr[w][v] != inf:
                D[v] = min(D[v], D[w]+arr[w][v])
    for i in range(N+1):
        print(arr[i])
    print('#{} {}'.format(tc, D[-1]))