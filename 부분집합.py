N = 5
a = [1, 2, 3, 4, 5]
res = []
for i in range(2**N):
    temp = []
    for j in range(N):
        if i & (1 << j) != 0:
            temp.append(a[j])
            if temp not in res:
                res.append(temp)
print(res)