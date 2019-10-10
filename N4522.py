import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    word = input()
    # ?는 와일드카드 아무거나 대체 가능하다
    p = 1
    for i in range(len(word)//2):
        if word[i] == '?' or word[-(i+1)] == '?':
            pass
        else:
            if word[i] != word[-(i+1)]:
                p = 0
                break
    if p == 0:
        print('#{} Not exist'.format(tc))
    else:
        print('#{} Exist'.format(tc))