import sys
sys.stdin = open('sample_input.txt', 'r')

def inorder(node):
    global N, ch1, ch2, res
    if node <= N:
        inorder(node * 2)
        res += str(tree[node])
        inorder(node * 2 + 1)

for tc in range(1,11):
    N = int(input())
    ch1 = [0] * (N+1)
    ch2 = [0] * (N+1)
    for k in range(1, N+1):
        t = input().split()
        # t[0] 노드에 t[1]을 저장

        for i in range(N-1):
            p = int(t[0])
            c = t[1]
            if ch1[p] == 0:
                ch1[p] = c
            else:
                ch2[p] = c
    inorder(1)
    print('#{} {}'.format(tc, res))