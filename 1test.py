import sys
sys.stdin = open('input.txt', 'r')
# 재귀로 만드는 부분집합
# 순열

N, M = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]
# h는 1부터 30까지
minV = 100000000000000000000
# minV가 갱신될 때 h값 기록
res = []
for k in range(1, 30):
    for i in range(N):
        for j in range(M):
            a = abs(sum(mat[i]) - (k*M))
            s = 0
            for x in range(N):
                s += mat[x][j]
            s = abs(s - (k*N))
            if minV > a + s:
                minV = a + s
                res.append(k)
print(minV, res[-1])
