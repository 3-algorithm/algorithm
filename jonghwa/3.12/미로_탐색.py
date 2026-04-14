import sys
from collections import deque

input=sys.stdin.readline

N,M=map(int,input().split())
maze=[list(map(int,input().strip())) for _ in range(N)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

queue=deque()
queue.append((0,0))

while queue:
    r,c=queue.popleft()
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<N and 0<=nc<M:
            if maze[nr][nc]==1 :
                maze[nr][nc]=maze[r][c]+1
                queue.append((nr,nc))

print(maze[N-1][M-1])

