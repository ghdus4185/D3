import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    A, B =map(int, input().split())
    res = (A//B)**2
    print('#{} {}'.format(tc, res))