import sys
sys.stdin = open('input.txt', 'r')
# 지원자 수랑 화장실 간 시간 돌아온 시간

N = int(input())
table = [0] * 10000
for i in range(N):
    go, back = map(int, input().split())
    for j in range(go, back):
        table[j] += 1
table.sort()
print(table[-1])
