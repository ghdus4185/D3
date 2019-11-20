import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    K = int(input())
    word = input()
    N = len(word)
    res = [word[i:] for i in range(N)]
    answer = sorted(res)
    print('#{} {}'.format(tc, answer[K-1]))