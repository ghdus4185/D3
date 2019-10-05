import sys
sys.stdin = open('input.txt', 'r')

#다익스트라
'''
1)D는 노드 인접행렬(A)의 행을 들고온 것
2)U에 확정된 노드를 넣는다.
3)D에서 U에 있는 노드를 제외한 나머지 중 최솟값을 본다.(w)
4)w에 인접한 모든 정점 v를 본다.
5)D[v] = min(D[v], D[w]+A[w][v]
'''

inf = float('INF')
for t in range(int(input())):
    N, E = map(int, input().split())

    # 무한대 값 저장
    arr = [[inf]*(N+1) for i in range(N+1)]

    # 자신으로 가는 값은 0
    for i in range(N+1):
        arr[i][i] = 0

    # 가중치
    for i in range(E):
        x,y,d = map(int, input().split())
        arr[x][y] = d

    # 정점들
    V = [i for i in range(N+1)]

    # 선택한 정점 추가
    U = [0]

    # 시작 정점의 행
    D = []
    for i in range(N+1):
        D.append(arr[0][i])

    # 선택한 정점들이 모든 정점을 본 것이 아니라면
    while sorted(U) != V:
        s = float('INF')

        # 보지않은 정점 중에서 짧은 거리
        for i in range(N+1):
            if not i in U:
                if D[i] != 0 and D[i] < s:
                    s = D[i]
                    w = i
        U.append(w)

        for v in range(N+1):
            if arr[w][v] != 0 and arr[w][v] != inf:
                D[v] = min(D[v], D[w]+arr[w][v])
                print(D)

    for i in range(N+1):
        print(arr[i])

    print('#{} {}'.format(t+1, D[-1]))