import sys
sys.stdin = open('GNS_test_input.txt', 'r')

T = int(input())
for tc in range(T):
    N = input()
    string = input().split()
    change = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
    rechange = {0: 'ZRO', 1: 'ONE', 2: 'TWO', 3: 'THR', 4: 'FOR', 5: 'FIV', 6: 'SIX', 7: 'SVN', 8: 'EGT', 9: 'NIN'}
    res = []
    for i in string:
        res.append(change.get(i))
        res.sort()
    real = []
    for j in res:
        real.append(rechange.get(j))
    print('#{}'.format(tc+1))
    print(" ".join(real))