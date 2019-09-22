# 그래프에 속한 모든 노드를 탐색
adj = [][]  # 인접행렬
visited = []
A = [1, 2, 4]  # 탐색전 생성
dfs(n)
    visit(n) # 방문한 노드에 대한 처리
    visited[n] = 1 # 방문 표시
    for i in range(1,N) # 인접하고 방문하지 않은 노드로 이동
        if i in A and adj[n][i] == 1 and visited[i] == 0:
            dfs(i)
# A에 속한 모든 노드를 방문했는지 확인