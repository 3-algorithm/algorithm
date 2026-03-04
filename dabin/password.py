import sys
sys.stdin = open("input_password.txt")

T = 10

for tc in range(1, T+1):
    N, pwd = input().split()
    stack = []

    stack.append(pwd[0])
    for i in range(1, int(N)):
        if stack:
            top = stack.pop()

            if pwd[i] != top:
                stack.append(top)
                stack.append(pwd[i])

        else:
            stack.append(pwd[i])

    if stack:
        print(f"#{tc} {''.join(stack)}")

    elif len(stack) == 0:
        print(f"#{tc} {pwd}")

