# 바킹독 - 백트래킹 - N과M (3)
# https://www.acmicpc.net/problem/15651

N, M = map(int, input().split())
arr=[]
for i in range(1, N+1):
    arr.append(i)
# 중복되는 수열도 넣어야 함
final = []

def subseq(idx):
    if idx == M:
        print(*final)
        return
    for j in range(0, N):
        final.append(arr[j])
        subseq(idx+1)
        final.pop()

subseq(0)