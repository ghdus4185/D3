# index 번호를 맞춰주기
check = [(0, 0)]
n = 1
while n < 300:
    x = 1
    y = n
    for i in range(n):
        check.append((x, y))
        x += 1
        y -= 1
        if y <= 0:
            n += 1
            break

T = int(input())
for tc in range(T):
    p, q = map(int, input().split())
    # 두 수를 좌표값으로 바꾸기
    pi, pj = check[p][0], check[p][1]
    qi, qj = check[q][0], check[q][1]
    # 두 좌표값의 x,y좌표끼리 계산
    ni, nj = pi+qi, pj+qj

    # n번째 들어있는 ni, nj
    result = check.index((ni, nj))
    print('#{} {}'.format(tc+1, result))