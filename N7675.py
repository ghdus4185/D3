import sys
sys.stdin = open('input.txt', 'r')

cap = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
       'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
         'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
finish = ['.', '?', '!']

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    sentence = list(map(str, input().split()))

    temp = ''
    lst = []
    for i in sentence:
        temp += i
        if i in finish:
            lst.append(temp)
            temp = ''

    cnt = 0
    res = []
    for i in range(len(sentence)):
        if sentence[i][0] in cap:
            for j in sentence[i][1:]:
                if j not in finish:
                    if j not in small:
                        break
            else:
                cnt += 1
            if '!' in sentence[i] or '?' in sentence[i] or '.' in sentence[i]:
                res.append(cnt)
                cnt = 0
        else:
            if '!' in sentence[i] or '?' in sentence[i] or '.' in sentence[i]:
                res.append(cnt)
                cnt = 0
    print('#{} {}'.format(tc, ' '.join(map(str, res))))