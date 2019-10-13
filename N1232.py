op = ['+', '-', '*', '/']
def f(n, last):
    if tree[n] in op:
        r1 = f(ch1[n], last)
        r2 = f(ch2[n], last)
        if tree[n] == '+':
            return r1 + r2
        elif tree[n] == '-':
            return r1 - r2
        elif tree[n] == '*':
            return r1 * r2
        elif tree[n] == '/':
            return r1 / r2
    else:
        return int(tree[n])

for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N + 1)
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    for i in range(N):
        node = list(input().split())
        if len(node) > 2:
            tree[int(node[0])] = node[1]
            ch1[int(node[0])] = int(node[2])
            ch2[int(node[0])] = int(node[3])
        else:
            tree[int(node[0])] = node[1]

    r = f(1,N)
    print('#{} {}'.format(tc, int(r)))