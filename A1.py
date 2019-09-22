import sys
sys.stdin = open('input.txt', 'r')

def check(lst):
    global mat

    if len(lst) == 1:
        return 1
    else:
        linked = []
        for l in lst:
            for ll in lst:
                if ll not in linked: # 만약 연결되어 있지 않으면
                    if l != ll and mat[l][ll] == 1: #
                        linked.append(ll)

    if set(lst) == set(linked):
        return 1
    else:
        return 0

for T in range(int(input())):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    people = list(map(int, input().split()))

    loc1, loc2 = [], [] # 지역구 나누기
    for i in range(1 << N):
        temp1, temp2 = [], []
        for j in range(N):
            if i & (1 << j):
                temp1.append(j) # 부분집합 원소 temp1
            else:
                temp2.append(j) # 부분집합 원소에 포함되지 않은 원소 temp2
        loc1.append(temp1) # temp1은 지역구1에 저장
        loc2.append(temp2) # temp2은 지역구2에 저장

    minV = sum(people) # people의 총합을 최대로 잡음
    loc1, loc2 = loc1[1:-1], loc2[1:-1]

    while loc1 and loc2:
        l1, l2 = loc1.pop(0), loc2.pop(0)

        if check(l1) and check(l2):
            t1, t2 = 0, 0
            for l in l1:
                t1 += people[l]
            for l in l2:
                t2 += people[l]
            if minV > abs(t1 - t2):
                minV = abs(t1 - t2)
    print('#{} {}'.format(T + 1, minV))