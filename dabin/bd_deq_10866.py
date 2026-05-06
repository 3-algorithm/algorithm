from collections import deque
import sys

N = int(input())
dq = deque()
result = []
for _ in range(N):
    orders = input().split()
    order = orders[0]

    if order == 'push_back':
        dq.append(orders[1])

    elif order == 'push_front':
        dq.appendleft(orders[1])

    elif order == 'pop_front':
        if len(dq) > 0:
            result.append(str(dq.popleft()))
        else:
            result.append(str(-1))

    elif order == 'pop_back':
        if len(dq) > 0:
            result.append(str(dq.pop()))
        else:
            result.append(str(-1))

    elif order == 'front':
        if len(dq) > 0:
            result.append(str(dq[0]))
        else:
            result.append(str(-1))

    elif order == 'back':
        if len(dq) > 0 :
            result.append(str(dq[-1]))
        else:
            result.append(str(-1))

    elif order == 'size':
        result.append(str(len(dq)))

    elif order == 'empty':
        if len(dq) > 0:
            result.append(str(0))
        else:
            result.append(str(1))

sys.stdout.write('\n'.join(result) + '\n')