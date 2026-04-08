# https://www.acmicpc.net/problem/1158

from collections import deque

n, k = map(int, input().split())

dq = deque()

for i in range(n, 0, -1):
    dq.append(i)

result = []
while dq:
    for _ in range(k - 1):
        dq.appendleft(dq.pop())
    result.append(str(dq.pop()))
    result.append(', ')

print(f"<{', '.join(map(str, result))}>")
