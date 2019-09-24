import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    a, b = input().split()

    a = ' '.join(a)
    a = list(map(int, a.split()))

    x = sorted(a)

    n = 0
    c = 0
    while n != int(b) or  n != len(a)//2:
        idx = 0
        for i in a:
            if x[-(n+1)] != i:
                if int(b) > len(a):
                    a[-int(b)+len(a)+n] = i
                    a[idx] = x[-(n+1)]
                    n += 1
                    break
                else:
                    a[-int(b)+n] = i
                    a[idx] = x[-(n+1)]
                    n += 1
                    break
            idx += 1
    if n != int(b):
        if int(b)-n % 2 == 1:
            a[-1], a[-2] = a[-2], a[-1]
    
    print(a, n)