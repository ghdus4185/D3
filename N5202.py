import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 끝나는 시간 기준으로 정렬한다. lambda 사용
    apply = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda s: s[1])
    time_table = []
    cnt = 0
    for i in apply:
        if time_table == []:
            time_table.append(i)
            cnt += 1
        if i[0] >= time_table[-1][1]:
            time_table.append(i)
            cnt += 1
    print('#{} {}'.format(tc, cnt))