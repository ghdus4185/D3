# 조합 앞에서부터
def f(n, k, cnt, arr):
    if cnt < k:
        print(arr[:])
    if cnt == k:
        return

    if n >= N:
        return

    f(n+1, k, cnt+1, arr+[nums[n]])
    f(n+1, k, cnt, arr)


nums = list(range(10))
N = 10
f(0, 3, 0, [])
