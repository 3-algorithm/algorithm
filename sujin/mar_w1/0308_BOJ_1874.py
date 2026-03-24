# 바킹독 - 스택 수열
# https://www.acmicpc.net/problem/1874

N = int(input())
operators = []
stack = []

current = 1
flag = True

for _ in range(N):
    num = int(input())
    while current <= num:
        stack.append(current)
        operators.append('+')
        current +=1
    if stack[-1] == num:
        stack.pop()
        operators.append('-')
    elif stack[-1] != num:
        flag = False
if flag:
    for i in operators:
        print(i)
else:
    print('NO')