import sys
from collections import deque
input=sys.stdin.readline

N=int(input())

paint = [list(input().strip()) for _ in range(N)]
visited = [[False]*N for _ in range(N)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

#일반인
def bfs(r,c):
    queue = deque()
    queue.append((r,c))
    visited[r][c]=True
    while queue:
        cr,cc = queue.popleft()
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0<=nr<N and 0<=nc<N :
                if paint[r][c] == paint[nr][nc] and not visited[nr][nc]:
                    visited[nr][nc]=True
                    queue.append((nr,nc))
    
cnt1=0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i,j)
            cnt1+=1

visited = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if paint[i][j]=='G':
            paint[i][j]='R'

cnt2=0
for i in range(N):
    for j in range(N):
         if not visited[i][j]:
            bfs(i,j)
            cnt2+=1

print(f'{cnt1} {cnt2}')
