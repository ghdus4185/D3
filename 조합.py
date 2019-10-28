#n 개에서 어떤 1개를 포함하는 경우와 포함하지 않는 경우로 나눠서 생각

# def ncr(n, r):
#     if r == 0:
#         print(p)
#     elif n < r:
#         return
#     else:
#         p[r-1] = a[n-1]
#         ncr(n-1, r-1)
#         ncr(n-1, r)
# n = 5
# r = 2
# a = [1, 2, 3, 4, 5]
# p = [0] * r
# ncr(n, r)

# 앞에서 부터 인덱스 계산하는 것 보다 뒤에서 보다 계산하는게 좋다.
# 특정원소를 포함하는 경우와 포함하지 않는 경우
# 지울 필요가 없는게 덮어쓰면 된다

# 조합 앞에서부터
def f(n, k, cnt, arr):

    if cnt == k:
        print(arr[:])
        return

    if n >= N:
        return

    f(n+1, k, cnt+1, arr+[nums[n]])
    f(n+1, k, cnt, arr)


nums = list(range(10))
N = 10
f(0, 3, 0, [])

# 중복조합
# def comb(depth, limit, history, candidates, target, temp):
#     global answer
#     if depth != limit:
#         for i in range(0 if depth == 0 else history[depth-1], candidates):
#             if temp + i <= target:
#                 history.append(i)
#                 comb(depth + 1, limit, history, candidates, target, temp)
#                 history.pop()
#     else:
#         if sum(history) == target:
#             answer.append(history[:])
#
#
# answer = []
#
# comb(0, 4, [], 11, 10, 0)
#
# print(len(answer))
# print(answer)