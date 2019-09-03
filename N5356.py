import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(T):
    ware = []
    string = ''
    for i in range(5):
       ware.append(list(input()))
    s = 0
    for i in range(5):
        s += len(ware[i])
    # print(s)

    j = 0
    while 1:
        #만약 0번째 값이 존재 하면 그걸로 더한다
        for i in range(len(ware)):
            if len(ware[i]) > j:
            # 존재하지 않으면 패스
                if ware[i][j]:
                    string += ware[i][j]

        j += 1

        if len(string) == s:
            break

    print('#{} {}'.format(tc+1, string))
