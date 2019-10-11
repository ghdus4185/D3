import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    word1 = input().split()
    word2 = input().split()
    print('#{} {}'.format(tc, len(word1 + word2) - len(set(word1 + word2))))