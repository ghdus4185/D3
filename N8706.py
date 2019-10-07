import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 수레 용량 M
    carrot = list(map(int, input().split()))
    # 0번 자리에 수확한 당근을 모으고 수레 보관 장소
    # 총 이동거리
    # 당근을 찾을때까지 움직임
    # 당근을 찾으면
    # 한칸움직이고 총용량까지 채우고 다 찼으면 돌아간다.
    # 다시 당근을 찾을 때까지 반복한다
    # 마지막 인덱스의 당근이 0이면
    d = 0
    while carrot[-1] != 0:
        temp = 0
        for i in range(N):
            if carrot[i] != 0:
                if carrot[i] <= M - temp: # 당근 개수가 (용량 - 수레에 있는개수) 보다 작으면
                    temp += carrot[i]
                    carrot[i] = 0
                else:
                    a = (M - temp)
                    temp += (M - temp)
                    carrot[i] -= a
            if temp == M:
                d += (i + 1) * 2
                break
            if i == N-1:
                if carrot[-1] == 0:
                    d += (i + 1) * 2
                    break
    print(d)



