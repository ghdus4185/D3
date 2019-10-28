# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split()))
    maxS, maxV = 0, 0
    i = 0
    S = 0
    while i < N - 1:
        s = 1
        p = 0
        if C[i] < C[i+1]:
            s += 1
            S += 1
            p += C[i] + C[i+1]
            k = 1
            while 1:
                if i+1+k < N:
                    if C[i+k] < C[i+1+k]:
                        s += 1
                        p += C[i+1+k]
                    else:
                        break
                else:
                    break
                k += 1
            i += k+1
        else:
            i += 1

        if maxS < s:
            maxS = s
            maxV = p
        if maxS == s:
            if maxV <= p:
                maxV = p
    print('#{} {} {}'.format(tc, S, maxV))