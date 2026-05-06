# 바킹독 - 연결리스트 - 에디터
# https://www.acmicpc.net/problem/1406
import sys
input = sys.stdin.readline

LHS = list(input())
LHS.pop() #리드라인쓰면 맨 뒤에 엔터까지 들어감. 빼줘야 함
num = int(input())

# 커서 중심으로 왼쪽
# 오른쪽
RHS = []

for i in range(num):
    temp = list(input().split())
    if LHS and temp[0] == 'L':
        RHS.append(LHS.pop())
    if RHS and temp[0] == 'D':
        LHS.append(RHS.pop())
    if LHS and temp[0] =='B':
        LHS.pop()
    if temp[0] == 'P':
        LHS.append(temp[1])

for j in range(len(RHS)-1, -1, -1):
    LHS.append(RHS[j])

print(''.join(LHS))
