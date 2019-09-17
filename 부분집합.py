N = 5
a = [1, 2, 3, 4, 5]
for i in range(2**N):
    temp = []
    for j in range(N):
        if i & (1 << j) != 0:
            temp.append(a[j])