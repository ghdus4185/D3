import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split()) # 점원수, 선반의 높이
    h = list(map(int, input().split()))

    # height의 모든 경우의 수를 만든다.
    # 모든 경우의 수의 합 중에 B보다 큰 걸 저장
    # 가장 작은걸 출력한다.
    subset_list = []
    for i in range(1, 2**N):
        res = 0
        for j in range(N):
            if i & (1 << j) != 0:
                res += h[j]
            if res >= B:
                subset_list.append(res)

    subset_list.sort()
    # print(subset_list)
    print('#{} {}'.format(tc, subset_list[0] - B))