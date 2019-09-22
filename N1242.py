import sys
sys.stdin = open('input.txt', 'r')

b = ['0000', '0001', '0010', '0011',
     '0100', '0101', '0111', '1000',
     '1001', '1010', '1011', '1111']

pat = [112, 122, 221, 114, 231, 132]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    a = [input() for _ in range(N)]
    s = ['']*N
    used = [[0]*M for _ in range(N)] # 확인된 암호 패턴 영역을 표시

    for i in range(N): # N개의 16진수 라인
        for j in range(N):
            s[i] += b[int(a[i][j], 16)] # 2진수의 문자열 형태로 저장

    total = 0
    for i in range(N):
        j = M*4-1
        cnt = [0]*3 # 1 0 1 의 각 개수 저장
        while j > 54:
            while j > 54 and s[i][j]=='0': # 1이 나올 때까지 0인 구간 스킵
                j -= 1
            while j >= 0 and s[i][j]=='1': # 1이 나오면 1인 구간의 길이 확인
                j -= 1
                cnt[0] += 1
            while j >= 0 and s[i][j]=='0': # 0인 구간의 길이
                j -= 1
                cnt[1] += 1
            while j >= 0 and s[i][j]=='1': # 1인 구간의 길이
                j -= 1
                cnt[2] += 1
    # (1) 16진수 -> 2진수
    # (2) 이진 문자열의 오른쪽부터 1,0,1,0 개수
