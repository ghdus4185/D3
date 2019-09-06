import sys
sys.stdin = open('input.txt', 'r')

# 시간 초과 뜸
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     res = set()
#     for i in range(2**N):
#         s = 0
#         for j in range(N):
#             if i & (1 << j) != 0:
#                 s += arr[j]
#             res.add(s)
#     print('#{} {}'.format(tc, len(res)))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    check = [0] * (sum(arr)+1)
    subset = [0]
    check[0] = 1
    for num in arr:
        temp = list(subset)
        for i in temp:
            if not check[i+num]:
                check[i+num] = 1
                subset += [i+num]
    print(check)
    print('#{} {}'.format(tc, sum(check)))

