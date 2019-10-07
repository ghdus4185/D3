import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrot = list(map(int, input().split()))
    minV = 1000000000000
    first = 0
    second = 0
    for i in range(len(carrot)):
        first = sum(carrot[:i+1])
        second = sum(carrot[i+1:])
        if first >= second:
            if first-second < minV:
                idx = i
                minV = first-second
        else:
            if second-first < minV:
                idx = i
                minV = second-first
    print('#{} {} {}'.format(tc, idx+1, minV))