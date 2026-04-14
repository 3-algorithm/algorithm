import sys
input = sys.stdin.readline

N=int(input())

arr=list(map(int,input().split()))

arr=sorted(list(set(arr)))

start = arr[0]
cnt = 0
for i in arr:
    if i>=start:
        start=i
        cnt+=1

print(cnt)
