import sys
input = sys.stdin.readline

N=int(input())

arr = [list(map(int,input().split())) for _ in range(N)]

arr.sort(key=lambda x:(x[1],x[0]))

cnt=0
last_end_time=0
for i in range(N):
    if arr[i][0] > last_end_time:
        last_end_time = arr[i][1] 
        cnt+=1

print(cnt)