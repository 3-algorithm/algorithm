# 바킹독 - 스택 - 제로
# https://www.acmicpc.net/problem/10773
from collections import deque

K = int(input())

stack = []
for k in range(K):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

if stack:
    print(sum(stack))
else:
    print(0)
