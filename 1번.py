import sys
sys.stdin = open('input.txt', 'r')

# 입력을 q에 모두 저장
# q에 메세지가 없을 때까지 돈다.
# q의 첫번째꺼를 빼서 while문을 돌릴때마다 1초씩 늘어난다.
# 만약 컨슈머가 일을 안하고 있을 시 하나 더 빼서 일안하고 있는 컨슈머가 일하도록한다.
a, b = map(int, input().strip().split(' ')) # 메세지 수, 컨슈머 수
time = [int(input()) for _ in range(a)] # time에 있는거를 하나 빼서 처리 하나 빼서 처리
# 모든 생산자 리스트를 만든다.
matrix = []
for i in range(b):
    matrix.append([0]*100000)
# 하나 하나 확인해서 그 생산자 리스트가 일을 하고 있는지 확인한다.
# 일을 하고 있지 않으면
sec = 1
maxV = 0
while time != []:
    # 일하고 있지 않은 만큼 팝한다.
    for i in range(b):
        if matrix[i][sec] == 0:
            a = time.pop(0) # 첫 메세지 수행시간
            for j in range(a):
                matrix[i][sec+j] += 1 # 메세지 수행 시간만큼 컨슈머의 체크 리스트를 1로 채운다.
    sec += 1
for k in range(b):
    res = matrix[k].count(1)
    if maxV < res:
        maxV = res
print(matrix)
print(maxV)