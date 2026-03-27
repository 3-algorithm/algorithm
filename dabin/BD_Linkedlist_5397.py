T = int(input())

for tc in range(1, T+1):
    input_key = input()
    stack = []

    cursor = 0
    for item in input_key:
        if item == '<':
            if cursor-1 >= 0 and stack:
                cursor -= 1

        elif item == '>':
            if cursor < len(stack):
                cursor += 1

        elif item == '-':
            if cursor > 0:
                stack.pop(cursor-1)
                
        else:
            stack.insert(cursor, item)
            cursor += 1

    print(''.join(stack))