T = int(input())
for tc in range(1, T+1):
    nums = input().split()
    N = int(nums[0])
    hax = nums[1]
    print('#{}'.format(tc), end=' ')
    for i in range(N):
        if '0' <= hax[i] <= '9':
            digit = ord(hax[i]) - ord('0')
        else:
            digit = ord(hax[i]) - ord('A') + 10
        for j in range(3, -1, -1):  # 3번 비트부터 0번 비트까지
            if digit & (1 << j) == 0:
                print('0', end='')
            else:
                print('1', end='')
    print('')