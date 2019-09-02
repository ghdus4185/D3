T = int(input())
for tc in range(T):
    A, B, C = map(int, input().split())
    if A > B:
        res = C//B
    else:
        res = C//A
    print('#{} {}'.format(tc+1, res))