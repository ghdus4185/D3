# 1 자식을 인덱스로 부모 저장
# 2 N1의 조상 i를 배열 a에 표시 a[j] = 1
# 3 N2의 조상 j를 배열 a에서 확인 a[j] == 1 인 경우
# 4 a[j] == 1 인 최초의 경우가 N1, N2에서 가장 가까운 공통 조상
import sys
sys.stdin = open('sample_input.txt', 'r')

def ancestor(n1,n2):
    while par[n1] != 0: # 부모가 있으면
        a[par[n1]] = 1 # 체크
        n1 = par[n1] # 8의 부모 5로 다시 반복
    while a[n2] == 0: # 13의 부모가 8의 조상들 중에 없으면
        n2 = par[n2] # 13의 부모로 다시 체크
    return n2

def subtree(n):
    global cnt
    if n > 0:
        subtree(ch1[n])
        subtree(ch2[n])
        cnt += 1

T = int(input())
for tc in range(1, 2):
    V, E, X1, X2 = map(int, input().split())
    t = list(map(int, input().split()))

    a = [0] * (V + 1)
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)
    par = [0] * (V + 1)
    cnt = 0
    for i in range(V-1):
        p = t[2*i]
        c = t[2*i+1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c
        par[c] = p
    print(par)
    x = ancestor(X1, X2)
    subtree(x)
    print('#{} {} {}'.format(tc, x, cnt))
