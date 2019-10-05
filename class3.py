# 인덱스 값이랑 대표값이랑 같은 개수 세기
# 7 4
# 2 3 4 5 4 6 7 6
# 3 6 두 노드가 같은 트리에 속하는지 확인

def rep(n):
    while p[n] != n:
        n = p[n]
    return n
V, E = map(int, input().split()) # 정점, 선
edge = list(map(int, input().split()))
v1, v2  = map(int, input().split())
p = [i for i in range(V+1)]
print(p)
for i in range(E):
    n1, n2 = edge[i*2], edge[i*2+1]
    p[rep(n1)] = rep(n2) # union(n1, n2) 인 경우(n1이 대표 원소)
    # p[rep(n1)] = rep(n2) # union(n2, n1)
print(p)

# 트리의 수 구하기(상호배타집합의 개수)
cnt = 0
for i in range(1, V+1):
    if p[i] == i:
        cnt += 1

#같은 트리에 속하는지
r = 1 if rep(p[v1]) == rep(p[v2]) else 0
print(cnt, r)