import sys
sys.stdin = open('input.txt', 'r')

# 최적의 BC를 선택하는 알고리즘

# 전체 뒤져서 최소값 찾고
# 한번 더 뒤져서 왼쪽 위를 탐색

T = int(input())
for tc in range(1, T+1):
    M, A = map(int, input().split()) # 움직이는 동작 M, 충전소 개수 A
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ap = [list(map(int, input().split())) for _ in range(A)]
    # 10x10맵을 만든다.
    # 각 맵을 0으로 채운다.
    # 충전소 위치를 기록
    sa = [1, 1]
    sb = [10, 10]
    # 이동정보에 따라서 들어갈 수 있는 충전소를 기록한다.
    for i in range(M):
        p_a = []
        p_b = []
        if a[i] == 0:
            for j in range(A):
                if abs(sa[0]-ap[j][0])+abs(sa[0]-ap[j][1]) <= ap[j][2]:
                    p_a += [j]
        elif a[i] == 1:
            sa[0] += -1
            for j in range(A):
                if abs(sa[0]-ap[j][0])+abs(sa[0]-ap[j][1]) <= ap[j][2]:
                    p_a += [j]
        elif a[i] == 2:
            sa[1] += 1
            for j in range(A):
                if abs(sa[0]-ap[j][0])+abs(sa[0]-ap[j][1]) <= ap[j][2]:
                    p_a += [j]
        elif a[i] == 3:
            sa[0] += 1
            for j in range(A):
                if abs(sa[0]-ap[j][0])+abs(sa[0]-ap[j][1]) <= ap[j][2]:
                    p_a += [j]
        elif a[i] == 4:
            sa[1] += -1
            for j in range(A):
                if abs(sa[0]-ap[j][0])+abs(sa[0]-ap[j][1]) <= ap[j][2]:
                    p_a += [j]

        # if b[0] == 0:
        #     for j in range(A):
        #         abs(sb[0]-ap[j][0])+abs(sb[0]-ap[j][1])
        # elif b[0] == 1:
        #     for j in range(A):
        #         abs(sb[0]-ap[j][0])+abs(sb[0]-ap[j][1])
        # elif b[0] == 2:
        #     for j in range(A):
        #         abs(sb[0]-ap[j][0])+abs(sb[0]-ap[j][1])
        # elif b[0] == 3:
        #     for j in range(A):
        #         abs(sb[0]-ap[j][0])+abs(sb[0]-ap[j][1])
        # elif b[0] == 4:
        #     for j in range(A):
        #         abs(sb[0]-ap[j][0])+abs(sb[0]-ap[j][1])

        print(p_a)
    # a,b의 충전소가 같으면 같은곳을 이용하는데 다른곳을 이용할수 있으면
    # 다른곳을 이용한게 큰지 같은곳을 이용하는게 큰지 판단해서 큰걸 선택한다.