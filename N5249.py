import sys
sys.stdin = open('input.txt', 'r')

#kruscal
def rep(n):
    while p[n] != n:
        n = p[n]
    return n

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(E)]
    edge.sort(key=lambda x:x[2]) # 가중치를 기준으로 정렬

    p = [i for i in range(V+1)] # 대표원소 배열
    cnt = 0
    s = 0
    for x in edge:# N개의 노드 V+1가 있는 경우 N-1개의 간선을 선택(V)
        n0 = rep(x[0])
        n1 = rep(x[1])
        if n0 != n1: # 두 노드의 대표 원소가 다르면 mst에 추가
            p[n1] = n0
            cnt += 1
            s += x[2]
            if cnt == V:
                break
    print('#{} {}'.format(tc, s))

# 프림알고리즘은 mst에 포함되지 않으면서 비용이 최소인걸 찾아서 넣는다.
# 그 다음에 포함된거를 하나로 보고 하나에서 인접한 노드들을 찾아서
# mst에 포함되지 않은 것 중에 최소 비용인걸 찾아서 넣는다.