import sys 
from collections import deque

N = int(input())
stack = deque()
for i in range(N):
    x = sys.stdin.readline().split()
    if x[0] == 'push':
        stack.append(x[1])
    if x[0] == 'pop':
        if stack:
            print(stack.popleft())
        else:
            print(-1)

    if x[0] == 'size':
        print(len(stack))
    if x[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    if x[0] == 'front':
        if stack:
            print(stack[0])
        else:
            print(-1)
    if x[0] == 'back':
        if stack:
            print(stack[-1])
        else:
            print(-1)
