import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    word = input()
    H = int(input())
    location = list(map(int, input().split()))
    for i in range(H):
        word = word[:location[i]] + '-' + word[location[i]:]
        for j in range(H-i):
            if location[i] < location[i+j]:
                location[i+j] += 1
    print('#{} {}'.format(tc, word))