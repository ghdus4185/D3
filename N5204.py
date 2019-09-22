import sys
sys.stdin = open('input.txt', 'r')

def merge_sort(m):
    if len(m) == 1:
        return m
    a = len(m)

    left = m[:a//2]
    right = m[a//2:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(L, R):
    global c

    result = []
    if L[-1] > R[-1]:
        c += 1
    while len(L) > 0 or len(R) > 0:
        if len(L) > 0 and len(R) > 0:
            if L[0] <= R[0]:
                result.append(L.pop(0))
            else:
                result.append(R.pop(0))
        elif len(L) > 0:
            result.append(L.pop(0))
        elif len(R) > 0:
            result.append(R.pop(0))
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    # 정렬 후 N//2번째 원소, 오른쪽 원소가 더 큰 경우
    c = 0
    print('#{} {} {}'.format(tc, merge_sort(a)[N//2], c))