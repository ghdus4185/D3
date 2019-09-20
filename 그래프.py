import sys
sys.stdin = open('input.txt', 'r')

# n번 노드에 방문하면서,
# n을 방문한 노드로 표시
# 모든 노드 i에 대해
# n에 인접이고 방문하지 않은 노드면
# i로 이동

def dfs(n, V):
    print(n, end = ' ') # 방문 노드 출력
    visited[n] = 1 # n번 노드에 방문 표시
    for i in range(1, V+1): # 모든 노드 i에 대해
        if adj[n][i] == 1 and visited[i] == 0: # 인접하고 미방문이면
            dfs(i, V) # i로 이동

def dfs2(n, k, V):
    if n == k: # 찾는 노드에 도착한 경우
         return 1 # 목적지를 찾아서 중단하는 경우
    else:
        visited[n] = 1 # n번 노드에 방문 표시
        for i in range(1, V+1): # 모든 노드 i에 대해
            if adj[n][i] ==1 and visited[i] == 0: # 인접하고 미방문이면
                if dfs2(i, k, V) == 1: # i로 이동, 목적지를 찾은경우
                    print(i, end=' ')
                    return 1
        return 0 # 목적지를 못찾은 경우

def dfs3(n, V):
    # 초기화
    stack = [0] * (V + 1) # 방문 표시용
    top = -1
    top += 1
    stack[top] = n
    visited[n] = 1
    while top >= 0: # 스택이 비어있지 않으면
        n = stack[top] # pop()
        top -= 1
        print(n, end= ' ')
        for i in range(1, V+1):
            if adj[n][i] == 1 and visited[i] == 0:
                top += 1
                stack[top] = i
                visited[i] = 1

def bfs(n, V):
    q = [0]*V # 큐 생성
    f = -1
    r = -1
    visited = [0]*(V+1) # 방문표시 배열
    # 시작점 인큐 + 방문표시
    r += 1
    q[r] = n
    visited[n] = 1
    while(f != r): # 큐가 비어있지 않으면 반복
        f += 1 # 디큐
        n = q[f]
        print(n)
        # n에 인접하고 미방문인 노드 i를 인큐 + 방문표시
        for i in range(1, V+1):
            if adj[n][i]==1 and visited[i]==0:
                r += 1
                q[r] = i
                visited[i] = 1


V, E = map(int, input().split())
adj = [[0]*(V+1) for _ in range(V+1)]

# visited = [0] * (V+1)

edge = list(map(int, input().split()))
for i in range(E):
    n1, n2 = edge[i*2], edge[i*2+1]
    adj[n1][n2] = 1
    adj[n1][n2] = 1 # 이걸 빼먹으면 방향성이 없는 그래프가 된다.
                    # 방향성이 없는 그래프가 되면 출력 결과가 바뀐다.
                    # 예시에서는 방향성이 있던 없던 답이 맞을 수도 있지만
                    # 제출해 봤을 땐 답이 틀리는 경우가 있다.
# dfs(1, V)
# dfs2(1, 7, V)
# dfs3(1, V)
bfs(1, V)