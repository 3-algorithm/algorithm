import sys
sys.stdin = open("input_bracket.txt")

T = 10

for tc in range(1, T+1):
    N = int(input())
    statement = input()
    stack = []
    success = True

    for i in range(len(statement)):
        if statement[i] == '(' or statement[i] == '{' or statement[i] == '<':
            stack.append(statement[i])

        elif statement[i] == ')' or statement[i] == '}' or statement[i] == '>':

            if len(stack) == 0:
                success = False
                break

            else:
                top = stack.pop()

                if statement[i] == ')' and top != '(':
                    success = False
                    break
                elif statement[i] == '}' and top != '{':
                    success = False
                    break
                elif statement[i] == '>' and top != '<':
                    success = False
                    break

    if len(stack) == 0 and success is True:
        print(f"#{tc} {int(success)}")
    else:
        print(f"#{tc} {int(success)}")

