import sys
sys.stdin = open("input_stack.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    stack = []

    for i in range(N):
        if arr[i][0] == 'push':
            stack.append(arr[i][1])
        elif arr[i][0] == 'top':
            if stack:
                print(stack[-1])
            else:
                print(-1)
        elif arr[i][0] == 'pop':
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif arr[i][0] == 'size':
            print(len(stack))
        elif arr[i][0] == 'empty':
            if stack:
                print(0)
            else:
                print(1)