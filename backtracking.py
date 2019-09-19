# DFS 검사 실시
# 각 검사 결과를 계속 해야할 필요가 있는지 확인
# 계속할 필요가 없으면 부모 노드로 돌아감

# 양의 정수만 주어지는 경우
# k 부분집합 원소 개수
# n 주어진 원소의 개수
# s n-1까지의 원소 중 부분집합에 포함된 원소의 합
# m 찾고자 하는 부분집합의 합

def subset(k, n, s, m, t):
    global cnt, cnt2
    cnt2 += 1

    # if s > m: # 백트래킹
    #     return

    if s == m:  # 현재까지의 부분집합의 합이 찾고자 하는 합과 같은 경우
        print(res)
        cnt += 1 # 이후의 어떤 원소를 선택해도 10보다 크다
        return

    if n == k: # 하나의 부분집합이 완성된 경우
        return

    elif s > m: # 백트래킹
        return

    elif s+t < m: # 백트래킹
        return

    else: # 고려할 원소가 남아있는 경우
        res.append(a[k])
        subset(k+1, n, s+a[k], m, t-a[k]) # 부분집합에 포함시키는 경우
        res.pop()
        subset(k+1, n, s, m, t-a[k]) # n번 원소를 부분집합에 포함시키지 않는 경우

res = []
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cnt = 0
cnt2 = 0
subset(0, len(a), 0, 10, sum(a))
print(cnt, cnt2)


# 비트연산자 방식

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# N = 10
# res = []
# cnt = 0
# for i in range(2**N):
#     temp = []
#     for j in range(N):
#         if i & (1 << j) != 0:
#             temp.append(a[j])
#             if sum(temp) == 10:
#                 if temp not in res:
#                     cnt += 1
#                     res.append(temp)
# print(cnt, res)