import sys
input=sys.stdin.readline

left_stack = list(sys.stdin.readline().rstrip())
right_stack = []

# 명령어의 개수
m = int(sys.stdin.readline())

for _ in range(m):
    command = sys.stdin.readline().split()
    
    if command[0] == 'L':
        # 커서를 왼쪽으로 이동
        if left_stack:
            right_stack.append(left_stack.pop())
            
    elif command[0] == 'D':
        # 커서를 오른쪽으로 이동
        if right_stack:
            left_stack.append(right_stack.pop())
            
    elif command[0] == 'B':
        # 커서 왼쪽 문자 삭제
        if left_stack:
            left_stack.pop()
            
    elif command[0] == 'P':
        # 커서 왼쪽에 문자 추가
        left_stack.append(command[1])

# 왼쪽 스택과 뒤집은 오른쪽 스택을 합쳐서 출력
print("".join(left_stack + right_stack[::-1]))