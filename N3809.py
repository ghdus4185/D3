import sys
sys.stdin = open('input.txt', 'r')

def f(n, k):
    global res
    if n == k:
        a = ' '.join(arr)
        res += arr
    else:
        for i in range(N):
            if used[i] == 0:
                used[i] = 1
                arr[n] = d[i]
                f(n+1, k)
                used[i] = 0
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    d = list(map(int, input().split()))
# 여기 나오는 모든 수로 한자리부터 N자리까지 순열을 만든다
    stop = 0
    for i in range(1, N+1):
        res = []
        used = [0] * N
        arr = [0] * i
        f(0, i)
        res.sort()
        print(res)
        for j in range(1, len(res)):
            if res[j] != res[j-1]+1 and res[j] != res[j-1]:
                stop = 1
                break
        if stop == 1:
            break
    print(j)