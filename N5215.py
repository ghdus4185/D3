import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    ingredient = [list(map(int, input().split())) for _ in range(N)] # 점수, 칼로리
    maxV = 0
    for i in range(1 << N):
        temp = []
        for j in range(N):
            if i & (1 << j) != 0:
                temp.append(j)
        cal = 0
        score = 0
        for j in temp:
            cal += ingredient[j][1]
            score += ingredient[j][0]
            if cal > L:
                break
        else:
            if maxV < score:
                maxV = score
    print('#{} {}'.format(tc, maxV))