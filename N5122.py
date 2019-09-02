import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(T):
    N, M, L = map(int, input().split())
    nums = list(map(int, input().split()))
    for i in range(M):
        cmd = input().split()
        if cmd[0] == 'I':
            nums.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == 'D':
            nums.pop(int(cmd[1]))
        elif cmd[0] == 'C':
            nums[int(cmd[1])] = int(cmd[2])

    if L < len(nums):
        print('#{} {}'.format(tc+1, nums[L]))
    else:
        print('#{} -1'.format(tc + 1))
