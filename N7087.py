import sys
sys.stdin = open('input.txt', 'r')

alpa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    first = []
    for i in range(N):
        title = input()
        first.append(title[0])

    possible = []
    while 1:
        a = len(possible)
        for i in first:
            if possible == []:
                if i == 'A':
                    possible.append(i)
            if i not in possible and possible:
                if len(i) == alpa.index(i):
                    possible.append(i)
        if a == len(possible):
            break
    print('#{} {}'.format(tc, len(possible)))