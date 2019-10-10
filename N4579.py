import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    word = input()
    p = 0
    ny = 0
    for i in range(len(word)//2):
        if word[i] == '*' or word[-(i+1)] == '*':
            ny = 1
        if ny == 0 and word[i] != word[-(i+1)]:
            print('#{} Not exist'.format(tc))
            break
    else:
        print('#{} Exist'.format(tc))