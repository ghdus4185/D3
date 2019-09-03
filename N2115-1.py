# 수도코드

# M개의 원소에서 1개 이상 최대 M개를 고르는 방법
M = 3
arr = [6, 1, 9]

# 비트연산을 활용한 부분집합 만들기
maxV = 0
for i in range(1, 2 ** M):  # 이진수 생성
    for j in range(M):  # 0, 1, 2번 비트
        s = 0 # 부분집합의 합
        ss = 0
        if i & (1 << j) != 0 and s + arr[j] <= c:  # i 의 j번 비트가 1이고, 제한량 이하면
            s += arr[j]
            ss += arr[i] * arr[j] # 채취한 벌꿀의 가치

    if maxV < ss:
        maxV = ss

return maxV # 결국 부분집합 합의 최대 값을 구하는 것
#첫째줄을 한사람이 고르고 두번째 사람은 그 아후줄에서 구함