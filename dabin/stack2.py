N = int(input())
stack = []
num = [int(input()) for _ in range(N)]

for i in range(N):
    if num[i] != 0:
        stack.append(num[i])
    else:
        stack.pop()

if stack:
    print(sum(stack))
else:
    print(0)
