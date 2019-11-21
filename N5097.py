import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    # 맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 반복
    for i in range(M):
        x = nums[0]

        for i in range(N-1):
            nums[i] = nums[i+1]
        nums[-1] = x
    print('#{} {}'.format(tc, nums[0]))