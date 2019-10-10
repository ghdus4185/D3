import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1, T+1):
    word = input()
    s1, s2, s3 = '', '', ''
    if len(word) == 1:
        print('..#..')
        print('.#.#.')
        print('#.'+word[0]+'.#')
        print('.#.#.')
        print('..#..')
    elif len(word) >= 2:
        for i in range(len(word)):
            s1 +='..#..'
            s2 +='.#.#.'
            s3 +='#.'+word[i]+'.'
        print(s1+'.')
        print(s2+'.')
        print(s3+'#')
        print(s2+'.')
        print(s1+'.')