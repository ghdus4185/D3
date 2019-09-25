import sys
sys.stdin = open('input.txt', 'r')

def find(n, k, c):
    global maxV, minV
    if c == 0 or n == k:
        s = 0
        for i in range(k):
            s = s*10 + int(card[i])
        if maxV <= 0:
            maxV = s
            if minV > c:
                minV = c
    else:
        lst = list(str(card))
        for i in range(k):
            card[n], card[i] = card[i], card[n]
            cnt 1 if n != i else 0
            find(n+1, k, c-cnt)
            card[n], card[i] = card[i], card[n]


T = int(input())
for tc in range(1, T+1):
    a, b = input().split()
