strings = list(input())
T = int(input())
cursor = len(strings)

for tc in range(1, T+1):
    input_list = list(input().split())
    N = input_list[0]

    if N == 'P':
        strings.insert(cursor, input_list[1])
        cursor += 1
    elif N == 'L' and cursor > 0:
        cursor -= 1
    elif N == 'D' and cursor < len(strings):
        cursor += 1
    elif N == 'B' and cursor > 0:
        strings.pop(cursor-1)
        cursor -= 1


print(''.join(strings))