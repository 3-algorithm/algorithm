# 바킹독 - 연결리스트 - 키로거
# https://www.acmicpc.net/problem/5397
import sys
input = sys.stdin.readline

num = int(input())
for i in range(num):
    arr = list(input())
    LHS = []
    RHS = []
    for j in range(len(arr)):
        if arr[j].isalnum():
            LHS.append(arr[j])
        if LHS and arr[j] == '<':
            RHS.append(LHS.pop())
        if RHS and arr[j] == '>':
            LHS.append(RHS.pop())
        if LHS and arr[j] == '-':
            LHS.pop()
    for j in range(len(RHS)-1, -1, -1):
        LHS.append(RHS[j])

    print(''.join(LHS))