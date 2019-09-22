T = int(input())
for tc in range(1, T+1):
    binary = input()
    ternary = input()
    res = []
    #이진수의 한자리씩 바꾼다
    #바꾼이진수를 십진수로 바꾼다
    #res에 저장한다
    for i in range(len(binary)):
        if binary[i] == '0':
            worng = binary[:i]+'1'+binary[i+1:]
        else:
            worng = binary[:i]+'0'+binary[i+1:]
        s = 0
        for j in range(len(worng)):
            s += int(worng[-1-j]) * (2 ** j)
        res.append(s)
    #삼진수를 한자리씩 바꾼다
    #바꾼삼진수가 res에 있으면 멈추고 출력
    for i in range(len(ternary)):
        if ternary[i] == '0':
            for k in range(2):
                worng = ternary[:i]+str(k+1)+ternary[i+1:]
                s = 0
                for j in range(len(worng)):
                    s += int(worng[-1 - j]) * (3 ** j)

                if s in res:
                    print('#{} {}'.format(tc, s))
                    break
        elif ternary[i] == '1':
            for k in range(2):
                if k == 0:
                    worng = ternary[:i]+str(k)+ternary[i+1:]
                else:
                    worng = ternary[:i]+str(k+1)+ternary[i+1:]
                s = 0
                for j in range(len(worng)):
                    s += int(worng[-1 - j]) * (3 ** j)

                if s in res:
                    print('#{} {}'.format(tc, s))
                    break
        elif ternary[i] == '2':
            for k in range(2):
                worng = ternary[:i]+str(k)+ternary[i+1:]
                s = 0
                for j in range(len(worng)):
                    s += int(worng[-1 - j]) * (3 ** j)

                if s in res:
                    print('#{} {}'.format(tc, s))
                    break
        if s in res:
            break