def f(n, s, d, m, m3): # n월, s : n-1월 까지 사용 금액
    global minV, table

    if n >= 13: # 더이상 고려할 기간이 없으면
        if minV > s:
            minV = s
    else: # 1에서 12월 사이면
        f(n+1, s+d*table[n], d, m, m3) # n월에 1일권 구입
        f(n+1, s+m, d, m, m3) # n월에 1개월권 구입
        f(n+3, s+m3, d, m, m3) # n월에 3개월권 구입


T = int(input())
for tc in range(T):
    d, m, m3, y = map(int, input().split())
    table = [0] + list(map(int, input().split()))
    minV = y  # 최소값의 초기화는 1년권으로 하면 된다.

    f(1, 0, d, m, m3)
    print('#{} {}'.format(tc+1, minV))

#