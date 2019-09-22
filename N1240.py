import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 인풋을 받아서 뒤에서부터 읽다가 1을 만나면 시작
    # 7글자씩 끊어서 읽는다
    # 끊어서 읽은걸 숫자로 바꾼다.
    code = [input() for _ in range(N)]
    res = 0
    for i in range(N):
        for j in range(M-1, 0, -1):
            if code[i][j] == '1':
                idx = j
                res = 1
                break
        if res == 1:
            break
    res = []

    for j in range(8):
        # print(code[i][idx-(j*7):idx-7-(j*7):-1])
        if code[i][idx-(j*7):idx-7-(j*7):-1] == '1011000':
            res.append('0')
        elif code[i][idx-(j*7):idx-7-(j*7):-1] == '1001100':
            res.append('1')
        elif code[i][idx-(j*7):idx-7-(j*7):-1] == '1100100':
            res.append('2')
        elif code[i][idx-(j*7):idx-7-(j*7):-1] == '1011110':
            res.append('3')
        elif code[i][idx-(j*7):idx-7-(j*7):-1] == '1100010':
            res.append('4')
        elif code[i][idx-(j*7):idx-7-(j*7):-1] == '1000110':
            res.append('5')
        elif code[i][idx-(j*7):idx-7-(j*7):-1] == '1111010':
            res.append('6')
        elif code[i][idx-(j*7):idx-7-(j*7):-1] == '1101110':
            res.append('7')
        elif code[i][idx-(j*7):idx-7-(j*7):-1] == '1110110':
            res.append('8')
        elif code[i][idx-(j*7):idx-7-(j*7):-1] == '1101000':
            res.append('9')
    res.reverse()
    res =list(map(int, ' '.join(res).split()))
    o = 0
    e = 0
    for i in range(len(res)):
        if i % 2 == 0:
            o += res[i]
        else:
            e += res[i]
    result = o*3 + e
    if result % 10 == 0:
        print('#{} {}'.format(tc, sum(res)))
    else:
        # 0
        print('#{} 0'.format(tc))