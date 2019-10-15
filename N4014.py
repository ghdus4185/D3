import sys
sys.stdin = open('input.txt', 'r')

def row(r):
    global way
    # 앞에서부터 연결되어있는지 확인하다가
    # 연결이 안되어있는점이 나오면 다리를 놓아서 연결이 가능한지 확인
    # 다리를 놓은점은 CHECK로 확인
    check = [0] * N
    linked = [0] * (N-1)
    possible = 0
    for i in range(N-1):
        if r[i] == r[i+1]:
            linked[i] = 1
        else: # 다리를 놓아서 연결이 가능한지 확인
            if r[i] - r[i + 1] == 1:
                pass
            for j in range(1, X+1):
                if 0 <= i+j <= N-1:
                    if r[i+1] == r[i+j]:
                        pass
                else:
                    return
            else:
                possible = 1

            if possible == 1:
                linked[i] =1
                pass
            else:
                return
    way += 1
def col(c):
    global way
    pass

T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split()) # N*N행렬, X 경사로 길이
    land = [list(map(int, input().split())) for _ in range(N)]
    way = 0
    # 가로 한 줄 활주로 건설할 수 있는지 확인
    for i in range(N):
        row(land[i])
    # 세로 한 줄
    for i in range(N):
        column = []
        for j in range(N):
            column += [land[j][i]]
        col(column)
    print(way)