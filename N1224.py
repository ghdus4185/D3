for tc in range(1, 11):
    N = int(input())
    cal = input()
    # 괄호를 만나면 닫힌 괄호를 만날때까지 stack에 쭉 모아서 계산
    res = 0
    for i in range(N):
        if cal[i] == "*":
            res += int(cal[i-1]) * int(cal[i+1])

    for i in range(N):
        if cal[i] == "+":
            res += cal[i-1] * cal[i+1]