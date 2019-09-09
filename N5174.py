# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

import sys
sys.stdin = open('sample_input.txt', 'r')

def inorder(n):
    global cnt

    if n > 0:
        inorder(ch1[n])
        # print(n, end=' ')
        cnt += 1
        inorder(ch2[n])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split()) # 간선 개수 E, 노드 수 N
    t = list(map(int, input().split()))

    ch1 = [0] * (E+2) # 부모를 인덱스로 자식 저장
    ch2 = [0] * (E+2)
    for i in range(E):
        p = t[2*i]
        c = t[2*i + 1]
        if ch1[p] == 0: # 아직 자식이 없으면
            ch1[p] = c
        else:
            ch2[p] = c
    cnt = 0
    inorder(N)
    print('#{} {}'.format(tc, cnt))
    print(ch1)
    print(ch2)