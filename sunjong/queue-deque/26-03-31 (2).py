# https://www.acmicpc.net/problem/18258

from collections import deque

n = int(input())

dq = deque()

for _ in range(n):
    cmd = input().split()

    if cmd[0] == 'push':
        dq.append(cmd[1])
    elif cmd[0] == 'pop':
        print(dq.popleft() if dq else -1)
    elif cmd[0] == 'size':
        print(len(dq))
    elif cmd[0] == 'empty':
        print(1 if not dq else 0)
    elif cmd[0] == 'front':
        print(dq[0] if dq else -1)
    elif cmd[0] == 'back':
        print(dq[-1] if dq else -1)
