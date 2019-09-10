# A형 1번 문제

# 두 그룹으로 나누기
N = 5
for i in range(1, (1 << N) - 1):
    A = []
    B = []
    for j in range(N):
        if i & (1 << j) != 0:
            A.append(j+1)
        else:
            B.append(j+1)
    print(A, B)

# 두 그룹이 유효한지 확인해서 두 그룹이 유효한 경우만 나누기