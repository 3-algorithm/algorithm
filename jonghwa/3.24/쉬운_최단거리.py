import sys
from collections import deque

input=sys.stdin.readline

N,M = map(int,input().split())

queue=deque()

dc= [-1,1,0,0]
dr= [0,0,-1,1]

land = [list(map(int,input().split())) for _ in range(N)]
dist=[[-1]*M for _ in range(N)]

start_c=0
start_r=0

for i in range(N):
    for j in range(M):
        if land[i][j]==2:
            dist[i][j]=0
            start_c,start_r=i,j
        if land[i][j]==0:
            dist[i][j]=0

queue.append([start_c,start_r])

while queue:
    c,r=queue.popleft()
    for i in range(4):
        nc= c+dc[i]
        nr= r+dr[i]

        if 0<=nc<N and 0<=nr<M:
            if not land[nc][nr]==0 and land[nc][nr]==1 and dist[nc][nr]==-1:
                dist[nc][nr] = dist[c][r]+1
                queue.append((nc,nr))
for row in dist:
    print(*row)



        



