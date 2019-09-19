import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
cap = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'O', 'P',
       'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for tc in range(1, T+1):
    N = int(input())
    a = ['.', '?', '!']
    sentence = input()
    # print(sentence)

    cnt = 0
    res = []
    n = 0
    for i in range(len(sentence)):
        if i == 0:
            if sentence[i] in cap:
                for j in range(1,100):
                    if sentence[i+j] in cap:
                        break
                    if sentence[i+j] == ' ':
                        cnt += 1
                        break
        else:
            if sentence[i] in cap:
                if sentence[i-1] == ' ':
                    cnt += 1

        if sentence[i] in a:
            res.append(cnt-n)
            cnt = 0
            n += 1
    print(res)