# 모든 노드에서 1번 노드에 도착하는 최소 비용
# D[] 생성
# 모든 i에 대해 1에 도착하는 초기 비용
#   D[i] = adj[i][j]
# V[] 생성
# V[1] = 1
# 모든 노드가 경유지로 고려될 때까지 반복
#   V[w]가 0이고, D[w]가 최소인 w선택
#   w로 진입하는 모든 노드 i에 대해
#           w를 거쳐 1로 가는 비용과 기존의 비용 중 작은 쪽을 선택
#           D[i] = min(D[i], adj[i][w] + D[w])
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split()) # 집 N, 단방향간선 M, 목적지 X
    for i in range(M):
        x, y, c = map(int, input().split())