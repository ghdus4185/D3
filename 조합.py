#n 개에서 어떤 1개를 포함하는 경우와 포함하지 않는 경우로 나눠서 생각
def comb(n, r):
    if r == 0:
        print(tr)
    elif n < r:
        return
    else:
        tr[r-1] = an[n-1]
        comb(n-1, r-1)
        comb(n-1, r)

n = 5
r = 2
an = [1, 2, 3, 4, 5]
tr = [0] * r
comb(n, r)

# 앞에서 부터 인덱스 계산하는 것 보다 뒤에서 보다 계산하는게 좋다.
# 특정원소를 포함하는 경우와 포함하지 않는 경우
# 지울 필요가 없는게 덮어쓰면 된다.