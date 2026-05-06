from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
targets = list(map(int, sys.stdin.readline().split()))

dq = deque([i for i in range(1, n + 1)])

total_moves = 0

for target in targets:
    while True:
        if dq[0] == target:
            dq.popleft()
            break
        else:
            target_idx = dq.index(target)
            
            if target_idx <= len(dq) // 2:
                dq.rotate(-1)
                total_moves += 1

            else:
                dq.rotate(1)
                total_moves += 1

print(total_moves)