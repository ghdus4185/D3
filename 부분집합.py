N = 5
# 원소가 1~N인 모든 부분집합
for i in range(2**N):
    A = []
    B = []
    for j in range(1, N+1):
        if i & (1 << j) != 0:
            A.append(j)
        else:
            B.append(j)

# 원소가 1~N인 부분집합 A, 부분집합에 속하지 않은원소 B로 나누기
for i in range(1, (1 << N)-1):
    A, B = [], []
    for j in range(N):
        if i & (1 << j) != 0:
            A.append(j+1)
        else:
            B.append(j+1)
    print(A, B)

# 길이가 k인 부분집합 출력하기
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

N = 10
k = 3
c = []

c = []
for i in range(1, 1<<N):
    b = []
    for j in range(N):
        if i & (1 << j) != 0:
            b.append(a[j])
        if len(b) > k:
            break
    else:
        if len(b) == k:
            c.append(b)
for i in range(len(c)):
    print(c[i])
print(len(c))

