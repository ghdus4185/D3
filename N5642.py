import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    seq = list(map(int, input().split()))
    # 첫번째부터 끝까지 더해서 최대 값
    maxV = -100000000000000000000
    for i in range(len(seq)):
        for j in range(len(seq)-i):
            x = sum(seq[i:i+j+1])
            if maxV < x:
                maxV = x
    print('#{} {}'.format(tc, maxV))