# 트리는 1차원 배열로 구현
# 높이 순서대로 번호를 붙이면 왼쪽자식은 2로 나눈거 오른쪽 자식은 2로 나눈거 +1
# 트리를 만드는데 사용한 시간은 O(n)
# 리프 개수가 2의 제곱수가 아닐 때 남는 칸에
# 합을 구할 땐 0을 넣고
# 최대값을 구할 땐 마이너스 무한대
# 최소값을 구할 땐 무한대를 넣는다.

# 단말노드에서 원하는 값을 찾고 left가 홀수면, left ++
# right가 짝수면, right --
# 해당 사항이 없으면 아무행동도 하지않고 left를 한칸 오른쪽으로
# right를 한칸 왼쪽으로 본다.
# 그게 끝나면 나누기 2해서 한번 더 반복
# left 인덱스 번호가 right 인덱스 번호보다 크면 다 한거라서 종료

# 원소 개수의 2배를 한게 단말의 크기이고
# 단말의 크기의 2배를 한게 트리의 크기이다.
# 패딩 넘버, 단말크기 - 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    print('#{}'.format(tc), end="")
    for i in range(M):
        C, X, Y = map(int, input().split())
        res = 0
        if C == 2:
            print(' {}'.format(res), end="")