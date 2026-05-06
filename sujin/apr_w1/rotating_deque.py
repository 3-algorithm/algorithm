from collections import deque
N, M = map(int, input().split())
target = deque(map(int, input().split()))
stack = deque()
for i in range(1, N+1):
    stack.append(i)

count = 0
while target:
    if stack[0] == target[0]:
        stack.popleft()
        target.popleft()
    else:
        if stack.index(target[0]) <= len(stack)//2:
            stack.append(stack.popleft())
            count += 1
        else:
            stack.appendleft(stack.pop())
            count += 1

print(count)