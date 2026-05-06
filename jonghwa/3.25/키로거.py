import sys

# 테스트 케이스의 개수 입력
t = int(sys.stdin.readline())

for _ in range(t):
    # 키로거 입력 문자열 (끝의 줄바꿈 문자 제거를 위해 rstrip 사용)
    keylog = sys.stdin.readline().rstrip()
    
    left_stack = []
    right_stack = []
    
    for char in keylog:
        if char == '<':
            # 커서를 왼쪽으로 이동
            if left_stack:
                right_stack.append(left_stack.pop())
                
        elif char == '>':
            # 커서를 오른쪽으로 이동
            if right_stack:
                left_stack.append(right_stack.pop())
                
        elif char == '-':
            # 백스페이스 (왼쪽 스택에서 삭제)
            if left_stack:
                left_stack.pop()
                
        else:
            # 일반 문자 입력 (왼쪽 스택에 추가)
            left_stack.append(char)
            
    # 최종 문자열 출력 (왼쪽 스택 + 순서를 뒤집은 오른쪽 스택)
    print("".join(left_stack + right_stack[::-1]))