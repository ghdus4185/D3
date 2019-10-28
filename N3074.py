import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N개 심사대, M 고객
    t = [int(input()) for _ in range(N)]
    check = [0] * N
    R = [0] * N
    # 0초에 비어있는거 중에 이용시간이 작은거로 채운다.
    # 다 차있으면 이용시간 + 남은시간중 가장 작은거에 가서 기다린다.
    for i in range(N):
        R[i] = check[i] + t[i]
