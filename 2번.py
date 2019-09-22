import sys
sys.stdin = open('input.txt', 'r')

def npr(n,k,N):
    global res

    if n == k:
        res.append(p[:])
    else:
        for i in range(N):
            if used[i] == 0:
                used[i] = 1
                p[n] = nums[i]
                npr(n+1, k, N)
                used[i] = 0

nums = list(map(int, input().strip().split(' ')))
N = len(nums)
b = int(input())
p = [0] * N
used = [0] * N
res = []
npr(0, N, N)
res.sort()
print(''.join(list(map(str, res[b-1]))))