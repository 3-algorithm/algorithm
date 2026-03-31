from collections import deque

n = int(input())

dq = deque()

for _ in range(n):
    cmd = input().split()

    if cmd[0] == 'push':
        dq.append(cmd[1])
    elif cmd[0] == 'pop':
        if not dq:
            print(-1)
            continue
        print(dq.popleft())
    elif cmd[0] == 'size':
        print(len(dq))
    elif cmd[0] == 'empty':
        if not dq:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if not dq:
            print(-1)
            continue
        x = dq.popleft()
        dq.appendleft(x)
        print(x)
    elif cmd[0] == 'back':
        if not dq:
            print(-1)
            continue
        x = dq.pop()
        dq.append(x)
        print(x)
