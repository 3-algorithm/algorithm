import sys
input = sys.stdin.readline
N,M = map(int,input().split())

arr = list(map(int,input().split()))
prefix_sum=[0]*(N+1)

for i in range(N):
    prefix_sum[i+1] = prefix_sum[i] + arr[i]

for _ in range(M):
    start,end=map(int,input().split())
    print(prefix_sum[end] - prefix_sum[start-1])
    


