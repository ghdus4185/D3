import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    w.sort()
    w.reverse()

    total = 0
    for i in range(M):
        for j in range(len(w)):
            # i번째 트럭의 적재 용량보다 작은거 중에 가장 무거운걸 싣는다.
            if t[i] >= w[j]:
                total += w[j]
                w.remove(w[j])
                break
    if total != 0:
        print('#{} {}'.format(tc, total))
    else:
        print('#{} 0'.format(tc))