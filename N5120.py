# import sys
# sys.stdin = open('sample_input.txt', 'r')

def password(n):
    global temp
    if temp + n < len(nums)-1:
        temp += n
        nums.insert(temp, (nums[temp]+nums[temp-1]))

    elif temp + n == len(nums) - 1:
        temp += n
        nums.insert(temp, (nums[temp]+nums[temp-1]))

    elif temp + n == len(nums):
        temp += n
        nums.insert(temp, (nums[0]+nums[-1]))

    elif temp + n > len(nums):
        temp += n - len(nums)
        nums.insert(temp, nums[temp]+nums[temp-1])

    return nums

T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    nums = list(map(int, input().split()))
    temp = 0
    for _ in range(K):
        password(M)
    result = list(map(str, nums))

    a = result[-1:-11:-1]
    print('#{} {}'.format(tc+1, " ".join(a)))