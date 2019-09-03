import sys
sys.stdin = open('GNS_test_input.txt', 'r')

T = int(input())
for tc in range(T):
    N = input()
    string = input()
    print(type(string))
    string.replace('ZRO', '0')
    string.replace('ONE', '1')
    string.replace('TWO', '2')
    string.replace('THR', '3')
    string.replace('FOR', '4')
    string.replace('FIVE', '5')
    string.replace('SIX', '6')
    string.replace('SVN', '7')
    string.replace('EGT', '8')
    string.replace('NIN', '9')
    print(string)