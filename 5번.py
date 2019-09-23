import sys
sys.stdin = open('input.txt', 'r')

def fact(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

N, M = map(int, input().split())
x, y = map(int, input().split())
a = fact(x)
b = fact(y)
c = fact(x+y)
answer = c//(a*b)

if 0 <= x < N and 0 <= y < M:
    print(x+y)
    print(answer)
else:
    print('fail')