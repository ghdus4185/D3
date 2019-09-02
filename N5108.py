T = int(input())
for tc in range(T):
    N, M, L = map(int, input().split()) # N 수열길이 M 추가횟수 L 인덱스번호
    matrix = list(map(int, input().split()))

    for i in range(M):
        a = list(map(int, input().split()))
        matrix.insert(a[0], a[1])
    print('#{} {}'.format(tc+1, matrix[L]))