import sys
sys.stdin = open('input.txt', 'r')

# 피봇보다 작은 값을 왼쪽 큰 값을 오른쪽에 둔다. 자기는 왼쪽과 오른쪽 사이에 둔다.
# 피봇값은 정렬된 상태일 때 자기가 있어야 할 위치에 놓임
# 피봇값은 다음 정렬에서 제외
def quicksort(a, l, r):
    if l < r:
        s = partition(a, l, r)
        quicksort(a, l, s-1)
        quicksort(a, s+1, r)
    return a

def partition(a, p, r):
    x = a[r]
    i = p - 1

    for j in range(p, r):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i+1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    arr = quicksort(arr, 0, N-1)
    print('#{} {}'.format(tc, arr[N//2]))