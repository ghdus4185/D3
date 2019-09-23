import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
seat = list(map(int, input().split()))
maxV = 0
for i in range(N):
    d = 0
    if seat[i] == 0:
        seat[i] = 1
        for j in range(1, N):
            if 0 <= i-j and i+j < N:
                if seat[i-j] == 0 and seat[i+j] == 0:
                    d += 1
                elif seat[i-j] == 1 or seat[i+j] == 1:
                    d += 1
                    break
            elif 0 <= i - j:
                if seat[i-j] == 0:
                    d += 1
                elif seat[i-j] == 1:
                    d += 1
                    break
            elif i+j < N and d != 0:
                if seat[i+j] == 0:
                    d += 1
                elif seat[i+j] == 1:
                    d += 1
                    break
        seat[i] = 0
    if seat[0] == 0:
        d += 1
    if maxV < d:
        maxV = d
print(maxV)