from collections import deque
import sys
input = sys.stdin.readline
N=int(input())
deq=deque()

for _ in range(N):
    command = input().split()
    if command[0]=='push_back':
        deq.append(command[1])
    elif command[0]=='push_front':
        deq.appendleft(command[1])
    elif command[0]=='pop_back':
        if len(deq)==0:
            print(-1)
        else:
            print(deq.pop())
    elif command[0]=='pop_front':
        if len(deq)==0:
            print(-1)
        else:
            print(deq.popleft())
    elif command[0]=='size':
        print(len(deq))
    elif command[0]=='empty':
        if len(deq)==0:
            print(1)
        else:
            print(0)
    elif command[0]=='front':
        if len(deq)==0:
            print(-1)
        else:
            print(deq[0])
    elif command[0]=='back': 
        if len(deq)==0:
            print(-1)
        else:
            print(deq[-1])