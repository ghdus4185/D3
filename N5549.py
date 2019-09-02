T = int(input())
for tc in range(T):
    N = int(input())
    if N % 2 == 1:
        print('#{} Odd'.format(tc+1))
    else:
        print('#{} Even'.format(tc+1))
