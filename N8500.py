import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    seat = [0]*A[0]+[1]+[0]*A[0]
    for i in range(N-1):
        seat += [1] + [0] * A[i+1]
    print('#{} {}'.format(tc, len(seat)))