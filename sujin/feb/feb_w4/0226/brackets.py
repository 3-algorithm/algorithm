import sys
sys.stdin = open("brackets_input.txt")

T = int(input())
for tc in range(1, T+1):
    arr = list(input())
    stack = []
    result = 1
# arr를 돌면서
    for char in arr:
# 여는 괄호가 나오면 스택에 넣음
        if char in '({':
            stack.append(char)
    # 스택 맨 위에꺼랑 세트인 닫는 괄호가 나오면 스택 맨 위에꺼 팝
        # 스택이 비어있지 않아야 함 (런타임 방지)
        elif char == ')':
            if not stack or stack.pop() != '(':
                result = 0
                break

        elif char == '}':
            if not stack or stack.pop() != '{':
                result = 0
                break
    if stack:
        result = 0
    # 마지막에 스택이 비어있으면 1, 아니면 0
    print(f'#{tc}', result)