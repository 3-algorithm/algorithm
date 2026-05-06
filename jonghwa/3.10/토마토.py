import sys
from collections import deque
input = sys.stdin.readline

M,N=map(int,input().split())

arr=[list(map(int,input().split()))for _ in range(N)]

queue = deque()

for r in range(N):
    for c in range(M):
        if arr[r][c] == 1:
            queue.append((r,c))

dr = [-1,1,0,0]
dc = [0,0,-1,1]


while queue:
    r,c=queue.popleft()
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<N and 0<=nc<M and arr[nr][nc]==0:
            arr[nr][nc]=arr[r][c]+1
            queue.append((nr,nc))

day=0
flag = False
for r in range(N):
    for c in range(M):
        if arr[r][c]==0:
            flag=True
        else:
            day= max(day,arr[r][c])
    

if flag:
    print(-1)
else:
    print(day-1)
        

